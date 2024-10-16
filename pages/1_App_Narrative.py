"""Narrative for Capstone assignment"""

import streamlit as st

st.title("Artifact: Stock Prediction App")

st.header("Overview")
st.write(
    """
The artifact I selected for my portfolio is a **Stock Prediction App** \
        built with Streamlit. This app uses a Long Short-Term Memory \
        (LSTM) neural network to predict stock prices based on historical data. 
Created toward the end of my Computer Science program, this app demonstrates \
        my ability to apply machine learning techniques—specifically \
        LSTMs—to real-world problems like stock forecasting. 

The app connects with real-time stock data using the `yfinance` \
        API (a pip install), allowing users to explore stock \
        trends and predictions through an intuitive interface. \
        This artifact reflects my growth in data science, 
machine learning, and web development, showcasing a full \
        data engineering pipeline applied in practice.
"""
)

st.header("Enhancements and Key Features")
st.write(
    """
- **SQL Injection Prevention**: One of the most critical improvements \
        I made was implementing parameterized queries to protect the \
        app from SQL Injection (SQLi) attacks. 
Initially, I wasn't sure how to enhance the app further, but upon \
        being reminded of SQLi vulnerabilities, I researched solutions. 
I adapted examples from different databases (like Postgres) and \
        modified them to work with SQLite in Python. 
Now, the app properly handles user input, ensuring it is treated \
        as data rather than executable code. The app also logs any \
        failed attempts to inject malicious SQL commands, improving \
        transparency for users.
"""
)
st.write(
    """
- **Dynamic Stock Data Queries**: The app allows users to \
        dynamically query the stock data stored in an SQLite database. 
By adding a feature to log the last API pull date, I provided \
        users with transparency regarding the freshness of the \
        data they are working with. 
The SQL queries are optimized for efficient data retrieval, which \
        is crucial given the volume of stock data involved.
"""
)
st.write(
    """
- **LSTM Model Implementation**: The app incorporates an LSTM \
        neural network, which is well-suited for time-series data \
        like stock prices. 
The data is preprocessed using scaling and a sliding window to \
        prepare it for the model. 
The LSTM architecture has multiple layers to capture long-term \
        dependencies in the data, showing my understanding of \
        deep learning principles. 
The model’s accuracy is evaluated using Mean Absolute Percentage \
        Error (MAPE), a standard metric for time-series forecasting.
"""
)
st.write(
    """
- **Logging and User Experience Improvements**: To further enhance \
        the user experience, I added a logging feature that tracks \
        when stock data was last pulled from the API. 
This log provides transparency, allowing users to know how recent \
        the data is. Additionally, I modularized many of the functions, 
creating a `repeated.py` file for easier debugging and updates.
"""
)

st.header("Justification for Inclusion in ePortfolio")
st.write(
    """
This artifact was selected because it highlights my proficiency in \
        multiple areas of computer science, including machine \
        learning, web development, database management, and security. 
By focusing on the prevention of SQLi attacks, I showcased my \
        ability to design secure software. The integration of \
        real-time data from `yfinance` and the use of an LSTM \
        neural network to predict stock prices 
demonstrates my ability to build complex machine learning models \
        and use APIs in real-world applications.
"""
)
st.write(
    """
The app also demonstrates my understanding of best practices, \
        such as modularization and clean coding. After adding \
        functions to the `repeated.py` file, 
I was able to streamline the prediction process and make the \
        code easier to maintain. Linting the code ensured it \
        adhered to industry standards.
"""
)

st.header("Challenges and Learning Outcomes")
st.write(
    """
One of the primary challenges was optimizing the LSTM model for \
        various stocks with different volatility. Initially, \
        the model worked well for some stocks but struggled with others. 
I spent a significant amount of time experimenting with \
        hyperparameters and regularization techniques to \
        improve the model’s performance across different \
        stock data. 
I also encountered a bug where the stock data pull for 3 \
        months (denoted "3mo") was being read incorrectly \
        due to a typo ("3m"). Fixing this and extending \
        the data pull to 6 months resulted in more consistent \
        and accurate predictions.
"""
)
st.write(
    """
Additionally, integrating SQLi prevention required careful \
        research and adaptation, as I was initially unfamiliar \
        with the differences between how various databases handle \
        such vulnerabilities. 
I learned how to use parameterized queries effectively and ensure \
        that the app would only accept safe SQL commands, such as \
        `SELECT`, preventing any destructive actions like `DROP TABLE`.
"""
)
st.write(
    """
Throughout the enhancement process, I gained deeper insights \
        into how small changes in data preprocessing and model \
        design can significantly impact performance and accuracy. 
I also learned more about building user-friendly applications \
        by ensuring that the data being displayed was \
        up-to-date and transparently sourced.
"""
)

st.header("Meeting Course Outcomes")
st.write(
    """
This artifact demonstrates my growth in several key areas of \
        the Computer Science program:
1. **Software Design and Engineering**: The app showcases my \
        ability to design and develop a secure web application.\
         The integration of dynamic queries and SQLi prevention \
        demonstrates secure coding practices and database management.
2. **Algorithms and Data Structures**: The LSTM neural network and \
        sliding window preprocessing highlight my understanding of \
        algorithmic principles, especially those tailored to \
        time-series forecasting.
3. **Databases**: The app effectively uses an SQLite database for \
        managing and querying stock data, showcasing my ability \
        to work with databases, secure data handling, and logging.
"""
)

st.header("Reflection")
st.write(
    """
Enhancing this artifact was a rewarding experience. It pushed me to \
        explore new techniques for security, improve the accuracy \
        of machine learning models, and refine my data preprocessing \
        skills. 
The project also solidified my understanding of integrating external \
        APIs and working with real-time data. By focusing on both \
        backend (SQL and security) and frontend (Streamlit interface) \
        improvements, 
I built a more complete and robust application that will serve as a \
        key example of my capabilities in my ePortfolio.
"""
)
