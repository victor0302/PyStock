# PyStock

## Authors

Victor Salazar

## Description
PyStock is a project for retrieving and analyzing stock data using Python. The project is still in progress and aims to develop a machine learning model to predict stock prices based on various features.

The project includes several files:

alpha_vantage_api.py: a Python module containing a function to make an API call to Alpha Vantage to retrieve stock data.
data_processing.py: a Python module containing code to preprocess stock data obtained from the Alpha Vantage API, including filtering data to the last year and resampling data to weekly intervals and aggregate using different summary statistics.
data_splitting.py: a Python module containing code to split the preprocessed data into training and testing sets using Scikit-Learn's train_test_split function.
news_sentiment.py: a Python module containing code to retrieve news articles related to a particular company using the News API and calculate the sentiment of each article using TextBlob.
machine_learning.py: a Python module containing code to build and evaluate machine learning models using Scikit-Learn.
## Future Plans
In the future, the project aims to build a machine learning model to predict stock prices using the preprocessed data, and to further refine the model by incorporating additional data sources and improving feature selection and engineering. The model will be evaluated using various metrics and tested using out-of-sample data.

## Learning Goals
The primary goal of this project is to gain experience in data analysis, machine learning, and web APIs, as well as to learn how to integrate various Python libraries and modules for data analysis and machine learning
