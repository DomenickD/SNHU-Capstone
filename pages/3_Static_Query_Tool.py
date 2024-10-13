"""The page for querying from the db file for a sqlite query of past data \
from 9/6/2024"""

import sqlite3
from datetime import datetime
import streamlit as st
import pandas as pd

# from repeated import fetch_and_save_stock_data


def get_latest_pull_date(ticker):
    """
    Function to get the latest pull date for a specific ticker.
    """
    conn = sqlite3.connect("stock_data.db")
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(pull_date) FROM log WHERE ticker = ?", (ticker,))
    latest_pull_date = cursor.fetchone()[0]
    conn.close()
    return latest_pull_date


st.title("Query Tool example display.")

# Radio buttons for single table selection
table_option = st.radio(
    "Select dataset:",
    ("Facebook(META)", "Amazon", "Apple", "Netflix", "Google"),
    key="table_option",
)


ticker_map = {
    "Facebook(META)": "META",
    "Amazon": "AMZN",
    "Apple": "AAPL",
    "Netflix": "NFLX",
    "Google": "GOOGL",
}
selected_ticker = ticker_map[table_option]

INPUT_QUERY = f"SELECT * FROM {selected_ticker};"

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

    last_pull_date = get_latest_pull_date(selected_ticker)

    if last_pull_date:
        # Convert the string to a datetime object
        last_pull_date = datetime.strptime(last_pull_date, "%Y-%m-%d %H:%M:%S.%f")

        # Format the datetime object for display
        formatted_date = last_pull_date.strftime("%m/%d/%Y %H:%M:%S")

        # Display the last update date for the selected ticker
        st.write(f"The data for {table_option} was last updated on: {formatted_date}")
    else:
        st.write(f"No data available for {table_option}.")

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
