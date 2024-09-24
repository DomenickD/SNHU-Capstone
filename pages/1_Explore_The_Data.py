"""This page will have information on the data with graphs, what model and what model was used. """

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

from repeated import faang_stocks

st.set_page_config(layout="wide")

# Page title
st.title("FAANG Stock Data")

# # Add a select box to choose a FAANG stock
# selected_stock = st.selectbox("Select a FAANG stock", list(faang_stocks.keys()))

# Add a select box to choose the period for historical data
period_options = [
    "5d",
    "1mo",
    "3mo",
    "6mo",
    "1y",
    "2y",
    "5y",
    "10y",
    "ytd",
    "max",
]
# selected_period = st.selectbox(
#     "Select time period", period_options, index=5
# )  # Default to "1y"

# # Add a submit button
# if st.button("Submit"):
#     # Set the ticker symbol based on the selected stock
#     ticker_symbol = faang_stocks[selected_stock]

#     # Define the ticker using the selected stock
#     ticker = yf.Ticker(ticker_symbol)

#     # Get historical data for the selected period
#     historical_data = ticker.history(period=selected_period)

#     if not historical_data.empty:
#         # Display the selected ticker symbol and historical data
#         st.subheader(
#             f"Stock Data for {selected_stock} ({ticker_symbol}) - {selected_period}"
#         )
#         st.write(historical_data)

#         # Plot the historical data
#         st.subheader(f"Price History for {selected_stock} ({ticker_symbol})")

#         # Create the plot for the stock data
#         plt.figure(figsize=(10, 6))

#         # Plot closing prices
#         plt.plot(historical_data.index, historical_data["Close"], label="Close Price")

#         # Add labels and title
#         plt.title(
#             f"{selected_stock} Stock Price ({ticker_symbol}) over {selected_period}"
#         )
#         plt.xlabel("Date")
#         plt.ylabel("Price")
#         plt.grid(True)
#         plt.legend()

#         # Display the plot in Streamlit
#         st.pyplot(plt)
#     else:
#         st.write("No data available for the selected time period.")

# Create two columns for stock selection
col1, col2 = st.columns(2)

with col1:
    st.header("Stock 1")
    selected_stock1 = st.selectbox(
        "Select the first FAANG stock", list(faang_stocks.keys()), key="stock1"
    )
    selected_period1 = st.selectbox(
        "Select time period", period_options, index=5, key="period1"
    )

with col2:
    st.header("Stock 2")
    selected_stock2 = st.selectbox(
        "Select the second FAANG stock", list(faang_stocks.keys()), key="stock2"
    )
    selected_period2 = st.selectbox(
        "Select time period", period_options, index=5, key="period2"
    )

# Add a submit button
if st.button("Submit"):
    # Fetch data for the first stock
    ticker_symbol1 = faang_stocks[selected_stock1]
    ticker1 = yf.Ticker(ticker_symbol1)
    historical_data1 = ticker1.history(period=selected_period1)

    # Fetch data for the second stock
    ticker_symbol2 = faang_stocks[selected_stock2]
    ticker2 = yf.Ticker(ticker_symbol2)
    historical_data2 = ticker2.history(period=selected_period2)

    # Create two columns for displaying data and plots
    data_col1, data_col2 = st.columns(2)

    # Display data and plot for the first stock
    with data_col1:
        if not historical_data1.empty:
            st.subheader(f"{selected_stock1} ({ticker_symbol1}) - {selected_period1}")
            st.write(historical_data1)

            # Plot for the first stock
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            ax1.plot(
                historical_data1.index,
                historical_data1["Close"],
                label="Close Price",
            )
            ax1.set_title(f"{selected_stock1} Price History")
            ax1.set_xlabel("Date")
            ax1.set_ylabel("Price")
            ax1.grid(True)
            ax1.legend()
            st.pyplot(fig1)
        else:
            st.write("No data available for the selected time period.")

    # Display data and plot for the second stock
    with data_col2:
        if not historical_data2.empty:
            st.subheader(f"{selected_stock2} ({ticker_symbol2}) - {selected_period2}")
            st.write(historical_data2)

            # Plot for the second stock
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            ax2.plot(
                historical_data2.index,
                historical_data2["Close"],
                label="Close Price",
            )
            ax2.set_title(f"{selected_stock2} Price History")
            ax2.set_xlabel("Date")
            ax2.set_ylabel("Price")
            ax2.grid(True)
            ax2.legend()
            st.pyplot(fig2)
        else:
            st.write("No data available for the selected time period.")
