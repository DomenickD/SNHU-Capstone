"""Page for predictions streamlit to streamlit cloud"""

import streamlit as st

# import yfinance as yf

# import matplotlib.pyplot as plt

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
selected_stock = st.selectbox(
    "Select a FAANG stock to see the prediction based on our models",
    list(faang_stocks.keys()),
)
st.caption("Only Google & Meta is supported currently.")
# Add a submit button
if st.button("Submit"):

    # Set the ticker symbol based on the selected stock
    ticker_symbol = faang_stocks[selected_stock]

    if ticker_symbol == "GOOGL":
        st.subheader("Google stock vs. LSTM Model")
        st.image(r"images/Google_LSTM_predict.png")
        st.caption("The closer the lines, the better the model will predict.")

    if ticker_symbol == "META":
        st.subheader("Facebook (Meta) stock vs. LSTM Model")
        st.image(r"images/Meta_LSTM_predict.png")

    st.write(f"{ticker_symbol}")
