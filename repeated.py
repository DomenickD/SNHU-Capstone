"""Repeated lists, dictionaries, ad functions to help with code \
    maintaianbaility, repeatability and linting"""

import yfinance as yf
from sklearn.metrics import mean_absolute_percentage_error
import numpy as np

faang_stocks = {
    "Facebook (Meta)": "META",
    "Amazon": "AMZN",
    "Apple": "AAPL",
    "Netflix": "NFLX",
    "Google (Alphabet)": "GOOG",
}


def fetch_stock_data(ticker_symbol, period="6mo"):
    """Fetch the last 3 months of stock data"""
    ticker = yf.Ticker(ticker_symbol)
    data = ticker.history(period=period)
    return data


def prepare_data_for_prediction(data, scaler):
    """Get the Close prices and scale them"""
    if data.empty:
        raise ValueError("The fetched data is empty.")

    if "Close" not in data.columns:
        raise ValueError("The 'Close' column is missing from the stock data.")

    if data["Close"].isnull().all():
        raise ValueError("The 'Close' column contains only NaN values.")

    # Debugging: Print the number of valid rows in the Close column
    valid_close_rows = data["Close"].dropna().shape[0]
    print(f"Number of valid 'Close' rows: {valid_close_rows}")

    if valid_close_rows < 90:
        raise ValueError(
            f"Not enough valid 'Close' price data to make \
                a prediction. Found {valid_close_rows} rows."
        )

    # Get the Close prices and scale them
    close_prices = data["Close"].values.reshape(-1, 1)
    scaled_data = scaler.transform(close_prices)

    # Prepare the input for the model, using the last 90 days
    last_90_days = scaled_data[-90:].reshape(1, -1, 1)

    return last_90_days


def predict_next_day_close(ticker_symbol, model, scaler):
    """Predict the next day's close price"""
    # Fetch stock data
    stock_data = fetch_stock_data(ticker_symbol)

    # Prepare data for prediction
    prepared_data = prepare_data_for_prediction(stock_data, scaler)

    # Predict the next day's close price
    predicted_scaled_close = model.predict(prepared_data)

    # Inverse transform the predicted value to get the actual closing price
    predicted_close = scaler.inverse_transform(predicted_scaled_close)

    return predicted_close[0][0]


def calculate_mape(model, scaler, data, sequence_length=90):
    """Calculate MAPE for the model based on the data provided."""
    if data.empty:
        raise ValueError("The fetched data is empty.")

    data_close = data["Close"].values.reshape(-1, 1)
    data_close_scaled = scaler.transform(data_close)

    # Create sequences and corresponding targets
    X = []
    y = []
    for i in range(sequence_length, len(data_close_scaled)):
        X.append(data_close_scaled[i - sequence_length : i, 0])
        y.append(data_close_scaled[i, 0])

    X = np.array(X)
    y = np.array(y)

    # Reshape X for LSTM input
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Split the data into training and testing sets
    train_size = int(len(X) * 0.8)
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Make predictions on the test set
    y_pred_scaled = model.predict(X_test)

    # Inverse transform the scaled predictions and actual values
    y_pred = scaler.inverse_transform(y_pred_scaled)
    y_test_actual = scaler.inverse_transform(y_test.reshape(-1, 1))

    # Calculate MAPE
    mape = (
        mean_absolute_percentage_error(y_test_actual, y_pred) * 100
    )  # Convert to percentage

    return mape
