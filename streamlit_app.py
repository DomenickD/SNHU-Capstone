"""Main splash page for the streamlit app"""

import streamlit as st

st.title("Predicting Stock data for FAANG stocks")

st.caption("By: Domenick Dobbs")

st.caption("Data obtained from the yfinance API.")

st.divider()

st.subheader("What is FAANG?")
st.write(
    "FAANG is an acronym referring to five leading tech companies: \
    Facebook (Meta), Amazon, Apple, Netflix, and Google (Alphabet). \
    These companies are influential in the stock market due to their \
    large market share, growth potential, and popularity with investors. \
    However, like any investment, FAANG stocks carry risks, and it's \
    important to conduct thorough research before investing."
)

st.divider()

st.subheader("What to expect:")

st.write(
    """
    This app will have a few parts:
         
- A data exploration tool for seeing the data.
         
- A page allowing for realtime prediction on the selected stock.

- A static query tool to display SQLite3 database integration.
         
- Acknowledgments for those you supported the project.
         
        """
)

st.divider()

st.subheader("About the model")

st.write(
    """
This model is an LSTM.
 An LSTM, or Long Short-Term Memory network, \
    is a type of recurrent neural network (RNN) \
    designed to address the limitations of traditional \
    RNNs in handling long-term dependencies in sequential data.
         
The data is scaled with a Min-Max Scaler. A MinMaxScaler works \
    by transforming features (columns) of your data so that \
    they are all scaled to a specific range, typically between 0 and 1.

```X_scaled = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) ```


"""
)

st.divider()

st.subheader("Scoring the model with Mean Absolute Percentage Error (MAPE)")

st.write(
    """
Why MAPE?

- **Interpretability**: MAPE expresses error as a percentage, which is easier for users to understand.
         
- **Scale Independence**: It provides a relative measure of the error, making it easier to compare across different stocks.
         
**Note**: MAPE can be undefined or misleading if actual values are zero or close to zero, but for stock prices, this isn't a concern.


"""
)

st.divider()

st.subheader("Limitations")

st.write(
    """
Some of the limitations present in this dataset and tackling this problem are:
         
- Only looking at limited data on stocks leads to not accounting for all the \
    variables that would lead to rise or fall in stocks. 

- Limiting the variables fed into the models to focus on close price can lead to\
    ignoring the reevaluation that is the open price of each day as well as any day \
    trading.

-  The yfinance data might contain inconsistencies, errors, or missing values, \
    which can negatively affect your model's performance. \
    Careful data cleaning and preprocessing are crucial.

-  LSTMs, like other deep learning models, are prone to overfitting, \
    especially when trained on limited or noisy data.

- LSTMs are often considered "black boxes," meaning it can be \
    challenging to interpret how they arrive at their predictions.
    This can make it difficult to understand the underlying factors \
    influencing the model's decisions.
"""
)
