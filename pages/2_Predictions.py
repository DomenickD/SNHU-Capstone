"""Page for predictions streamlit to streamlit cloud"""

import streamlit as st
import keras
from joblib import load
from repeated import (
    faang_stocks,
    predict_next_day_close,
    fetch_and_save_stock_data,
    calculate_mape,
)

# import yfinance as yf

# import matplotlib.pyplot as plt

# Page title
st.title("FAANG Stock Data")

# Add a select box to choose a FAANG stock
selected_stock = st.selectbox(
    "Select a FAANG stock to see the prediction based on our models",
    list(faang_stocks.keys()),
)

R2 = 0.00
MODEL = None
SCALER = None
# Add a submit button
if st.button("Submit"):

    # Set the ticker symbol based on the selected stock
    ticker_symbol = faang_stocks[selected_stock]

    if ticker_symbol == "GOOGL":
        st.subheader("Google stock vs. LSTM Model")
        st.image(r"images/Google_LSTM_predict.png")

        FILE_NAME_GOOGLE = r"models/best_model_google.keras"
        with open(FILE_NAME_GOOGLE, "rb") as f:
            MODEL = keras.models.load_model(FILE_NAME_GOOGLE)
        SCALER = load("scalers/scaler_google.gz")
        R2 = 0.9875 * 100  # this is correct

    if ticker_symbol == "META":
        st.subheader("Facebook (Meta) stock vs. LSTM Model")
        st.image(r"images/Meta_LSTM_predict.png")

        FILE_NAME_META = r"models/best_model_meta.keras"
        with open(FILE_NAME_META, "rb") as f:
            MODEL = keras.models.load_model(FILE_NAME_META)
        SCALER = load("scalers/scaler_meta.gz")
        R2 = 0.9944 * 100  # this is correct

    if ticker_symbol == "AMZN":
        st.subheader("Amazon stock vs. LSTM Model")
        st.image(r"images/Amazon_LSTM_predict.png")

        FILE_NAME_AMZN = r"models/best_model_amazon.keras"
        with open(FILE_NAME_AMZN, "rb") as f:
            MODEL = keras.models.load_model(FILE_NAME_AMZN)
        SCALER = load("scalers/scaler_amazon.gz")
        R2 = 0.9679 * 100  # this is correct

    if ticker_symbol == "AAPL":
        st.subheader("Apple stock vs. LSTM Model")
        st.image(r"images/Apple_LSTM_predict.png")

        FILE_NAME_AAPL = r"models/best_model_apple.keras"
        with open(FILE_NAME_AAPL, "rb") as f:
            MODEL = keras.models.load_model(FILE_NAME_AAPL)
        SCALER = load("scalers/scaler_apple.gz")
        R2 = 0.9071 * 100  # this is correct

    if ticker_symbol == "NFLX":
        st.subheader("Netflix stock vs. LSTM Model")
        st.image(r"images/Netflix_LSTM_predict.png")

        FILE_NAME_NFLX = r"models/best_model_netflix.keras"
        with open(FILE_NAME_NFLX, "rb") as f:
            MODEL = keras.models.load_model(FILE_NAME_NFLX)
        SCALER = load("scalers/scaler_netflix.gz")
        R2 = 0.9486 * 100  # this is correct

    st.caption(
        "The closer the lines, the better the model will predict.\
               In order to get better predictions, we need access to news\
               data to account for a wide range of variables."
    )

    # st.caption(
    #     "The graph displays how the model performed epoch for epoch.\
    #            As we can see, the first 80% of the graph is predicting much closer \
    #            to the actual stock price than the last 20% of the graph."
    # )

    # Fetch historical data for the selected stock
    data = fetch_and_save_stock_data(ticker_symbol)

    if not data.empty:
        # Calculate the MAPE using the new function
        try:
            mape = calculate_mape(MODEL, SCALER, data)
            st.write(
                f"Model's Mean Absolute Percentage Error (MAPE) on test data: {mape:.2f}%."
            )
            st.caption("**Remember**: MAPE - (The lower the better.)")
        except ValueError as e:
            st.error(f"Error calculating MAPE: {e}")
            st.stop()

        # Predict the next day's closing price
        try:
            predicted_close = predict_next_day_close(ticker_symbol, MODEL, SCALER)
            last_close_price = data["Close"].iloc[-1]

            # Determine if the stock is predicted to go up or down
            if predicted_close > last_close_price:
                MOVEMENT = "up 📈"
            elif predicted_close < last_close_price:
                MOVEMENT = "down 📉"
            else:
                MOVEMENT = "remain the same"

            st.write(
                f"Predicted next day's close price for {selected_stock} ({ticker_symbol}): ${predicted_close:.2f}"
            )
            st.write(
                f"The model predicts the stock will go **{MOVEMENT}** from \${last_close_price:.2f} to \${predicted_close:.2f}."
            )
        except ValueError as e:
            st.error(f"Error predicting next day's close price: {e}")
            st.stop()

    else:
        st.error("No data available for the selected stock.")

    # st.write(f"{ticker_symbol}")
    # Use the prediction function

    # predicted_close = predict_next_day_close(ticker_symbol, MODEL, SCALER)
    # st.write(
    #     f"Predicted next day's close price for {ticker_symbol}: ${predicted_close:.2f}"
    # )
    # st.write(
    #     f"The R2 score of the training data (the first 80% of the graph) is: {R2:.2f}%"
    # )
