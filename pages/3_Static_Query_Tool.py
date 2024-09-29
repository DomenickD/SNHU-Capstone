"""The page for querying from the db file for a sqlite query of past data \
from 9/6/2024"""

import sqlite3
import streamlit as st
import pandas as pd

st.title("Query Tool example display.")

st.write("The data here is stored in a SQLITE database and is static as of 9/6/2024.")

# Radio buttons for single table selection
table_option = st.radio(
    "Select dataset:",
    ("Facebook(META)", "Amazon", "Apple", "Netflix", "Google"),
    key="table_option",
)

INPUT_QUERY = ""
if table_option == "Facebook(META)":
    INPUT_QUERY = "SELECT * FROM META;"
elif table_option == "Amazon":
    INPUT_QUERY = "SELECT * FROM AMZN;"
elif table_option == "Apple":
    INPUT_QUERY = "SELECT * FROM AAPL;"
elif table_option == "Netflix":
    INPUT_QUERY = "SELECT * FROM NFLX;"
elif table_option == "Google":
    INPUT_QUERY = "SELECT * FROM GOOGL;"

query = st.text_area(label="Enter your SQL query here:", value=INPUT_QUERY)


# The SQLITE DB query with parameterized SQL
def query_database(query_intake):
    """
    This is the function to do the actual database querying.
    """
    conn = sqlite3.connect("stock_data.db")
    cursor = conn.cursor()
    try:
        # Use parameterized queries to avoid SQL injection
        cursor.execute(query_intake)
        columns = [
            description[0] for description in cursor.description
        ]  # Get column names
        data = cursor.fetchall()
    except sqlite3.Error as e:
        st.error(f"An error occurred: {e}")
        return pd.DataFrame()  # Return empty DataFrame on error
    finally:
        conn.close()

    return pd.DataFrame(data, columns=columns)  # Return a DataFrame directly


if st.button("Submit"):
    if not query.lower().startswith(
        "select"
    ):  # this should prevent drop table SQLi attacks
        st.error("Only SELECT queries are allowed for security reasons.")
    else:
        result = query_database(query)
        if not result.empty:
            st.dataframe(result)  # Display the DataFrame in Streamlit
        else:
            st.write("No results found.")
