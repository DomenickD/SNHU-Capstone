"""This page will have information on the data with graphs, what model and what model was used. """

import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Page title
st.title("FAANG Stock Data")

# List of FAANG stocks with their corresponding ticker symbols
faang_stocks = {
    "Facebook (Meta)": "META",
    "Amazon": "AMZN",
    "Apple": "AAPL",
    "Netflix": "NFLX",
    "Google (Alphabet)": "GOOGL",
}

# Add a select box to choose a FAANG stock
selected_stock = st.selectbox("Select a FAANG stock", list(faang_stocks.keys()))

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
selected_period = st.selectbox(
    "Select time period", period_options, index=5
)  # Default to "1y"

# Add a submit button
if st.button("Submit"):
    # Set the ticker symbol based on the selected stock
    ticker_symbol = faang_stocks[selected_stock]

    # Define the ticker using the selected stock
    ticker = yf.Ticker(ticker_symbol)

    # Get historical data for the selected period
    historical_data = ticker.history(period=selected_period)

    if not historical_data.empty:
        # Display the selected ticker symbol and historical data
        st.subheader(
            f"Stock Data for {selected_stock} ({ticker_symbol}) - {selected_period}"
        )
        st.write(historical_data)

        # Plot the historical data
        st.subheader(f"Price History for {selected_stock} ({ticker_symbol})")

        # Create the plot for the stock data
        plt.figure(figsize=(10, 6))

        # Plot closing prices
        plt.plot(historical_data.index, historical_data["Close"], label="Close Price")

        # Add labels and title
        plt.title(
            f"{selected_stock} Stock Price ({ticker_symbol}) over {selected_period}"
        )
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.grid(True)
        plt.legend()

        # Display the plot in Streamlit
        st.pyplot(plt)
    else:
        st.write("No data available for the selected time period.")
