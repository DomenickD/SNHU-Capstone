"""The page for querying from the db file for a sqlite query of past data \
from 9/6/2024"""

import sqlite3
import streamlit as st
import pandas as pd

st.title("Query Tool example display.")

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


# The SQLITE DB query
def query_database(query_intake):
    """
    This is the function to do the actual database querying.
    """
    conn = sqlite3.connect("stock_data.db")
    cursor = conn.cursor()
    cursor.execute(query_intake)
    columns = [description[0] for description in cursor.description]  # Get column names
    data = cursor.fetchall()
    conn.close()
    return pd.DataFrame(data, columns=columns)  # Return a DataFrame directly


if st.button("Submit"):
    result = query_database(query)
    st.dataframe(result)  # Display the DataFrame in Streamlit
