"""Page for predictions streamlit to streamlit cloud"""

import streamlit as st
import keras
from joblib import load
from repeated import faang_stocks, predict_next_day_close

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
MODEL = "No Model assigned."
SCALER = "No scaler assigned."
# Add a submit button
if st.button("Submit"):

    # Set the ticker symbol based on the selected stock
    ticker_symbol = faang_stocks[selected_stock]

    if ticker_symbol == "GOOG":
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

    # st.write(f"{ticker_symbol}")
    # Use the prediction function
    st.caption(
        "The closer the lines, the better the model will predict.\
               In order to get better predictions, we need access to news\
               data to account for a wide range of variables."
    )
    predicted_close = predict_next_day_close(ticker_symbol, MODEL, SCALER)
    st.write(
        f"Predicted next day's close price for {ticker_symbol}: ${predicted_close:.2f}"
    )
    st.write(f"The R2 score is: {R2:.2f}%")
