import pandas as pd
from sklearn.model_selection import train_test_split
from src.data_processing import weekly_df
from src.news_sentiment import sentiment_df

# Merge the sentiment DataFrame with your existing DataFrame
weekly_df = pd.merge(weekly_df, sentiment_df, left_index=True, right_index=True, how='outer')

# Fill any missing values with 0
weekly_df.fillna(0, inplace=True)

# Set the input features and target variable
X = weekly_df[['1. open', '2. high', '3. low', '4. close', '6. volume', '10-day MA',
               'title_polarity', 'description_polarity', 'content_polarity']]
y = weekly_df['4. close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


