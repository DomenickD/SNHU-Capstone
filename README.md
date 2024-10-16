# Stock Prediction App

This project is part of my Computer Science Capstone at Southern New Hampshire University (CS 499). The **Stock Prediction App** is a web-based application built with **Streamlit** that allows users to predict stock prices using a **Long Short-Term Memory (LSTM)** neural network model. The app connects to real-time stock data via the **yfinance API** and provides users with an intuitive interface for querying stock data and making predictions.

You can access the live app here: [Stock Prediction App](https://snhu-capstone-domenickd.streamlit.app/)

## Features
- **Real-time Stock Data**: Query stock data for FAANG stocks using the yfinance API.
- **LSTM Model for Prediction**: Predict stock prices using an LSTM neural network trained on historical data.
- **Dynamic Queries**: Query stock data stored in an SQLite database and view the most recent API data pull.
- **SQL Injection Prevention**: Secure SQL queries using parameterized queries to protect against SQL Injection (SQLi) attacks.
- **User-friendly Interface**: Built with Streamlit, the app is easy to navigate and interact with.
- **Logging and Transparency**: Logs the time of the last API pull and ensures data is up to date.

## Project Structure

- **`app.py`**: Main Streamlit app file that handles user interaction, data querying, and LSTM predictions.
- **`repeated.py`**: Contains modular functions that are imported into `app.py` for preprocessing, querying, and logging.
- **`requirements.txt`**: Lists the Python packages required to run the app.
  
## How to Run the Project Locally

### Prerequisites
To run the app locally, you need to have the following installed:
- Python 3.8+
- Pip (Python package installer)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/stock-prediction-app.git
   cd stock-prediction-app
    ```
2. Create a virtual environment (optional but recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:
```bash
streamlit run app.py
```

5. Access the app by visiting http://localhost:8501 in your browser.

## Technologies Used
- **Streamlit**: For building the interactive web interface.
- **Python**: Core programming language for the app.
- **yfinance API**: Used to retrieve real-time stock data.
- **SQLite**: Database for storing stock data.
- **TensorFlow/Keras**: Used for building and training the LSTM neural network.
- **Matplotlib/Plotly**: For visualizing stock data and predictions.

## Key Functionalities
1. **Stock Data Queries**: Users can query stock data from an SQLite database. The app displays the most recent API pull date to ensure users are working with fresh data.
   
2. **Stock Price Predictions**: The app allows users to predict stock prices using a trained LSTM model. The model is built to capture long-term dependencies in the stock data.

3. **Security Features**: The app uses parameterized queries to protect against SQL Injection (SQLi) attacks, ensuring the database remains secure.

4. **Logging**: The app logs API pulls and user queries for transparency, allowing users to view the time of the last stock data pull.

## Challenges and Enhancements
This project reflects my growth in data science, machine learning, and web development. Some challenges I faced included optimizing the LSTM model for different stock volatility and preventing SQL Injection attacks by researching parameterized queries.

## Future Enhancements
- Expand the app to support a wider range of stocks beyond FAANG.
- Improve model accuracy by experimenting with additional time-series forecasting models.
- Add user authentication and data caching for better scalability.
