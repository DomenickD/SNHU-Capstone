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

st.subheader("What to expect:")

st.write(
    """
    This app will have a few parts:
         
- A data exploration tool for seeing the data.
         
- A page explaining the inner workings of the model.
         
- Acknowledgments for those you supported the project.
         
        """
)
