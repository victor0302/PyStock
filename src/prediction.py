import pandas as pd

from src.data_processing import weekly_df
from src.news_sentiment import sentiment_df
from src.machine_learning import model

new_weekly_df = weekly_df.loc['2022-09-25':'2023-02-19']

sentiment_df.reset_index(inplace=True)
new_sentiment_df = sentiment_df.loc[sentiment_df['date'].isin(new_weekly_df.index)]

# Merge the new data with the existing data
merged_weekly_df = pd.concat([weekly_df, new_weekly_df])
merged_sentiment_df = pd.concat([sentiment_df, new_sentiment_df])
merged_weekly_df = pd.merge(merged_weekly_df, merged_sentiment_df, left_index=True, right_on='date', how='outer')
merged_weekly_df.set_index('date', inplace=True)
merged_weekly_df.fillna(0, inplace=True)

# Make predictions using the machine learning model
X_new = merged_weekly_df[['1. open', '2. high', '3. low', '4. close', '6. volume', '10-day MA', 'title_polarity',
                          'description_polarity', 'content_polarity']]
y_new_pred = model.predict(X_new)

print(y_new_pred)
