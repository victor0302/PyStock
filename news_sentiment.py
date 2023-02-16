from newsapi import NewsApiClient
from textblob import TextBlob
import pandas as pd
from data_processing import df, weekly_df

# Set up the News API client
api_key = '5c9b52e985b44b1a8c553d7935f66e8d'
newsapi = NewsApiClient(api_key)

# Define the company to search for
company = 'NVDA'

# Set up the request parameters for the News API
request_params = {
    'q': company,
    'language': 'en',
    'sort_by': 'relevancy',
    'page_size': 50,
}

# Make the request to the News API
response = newsapi.get_everything(**request_params)

# Get the articles from the response
articles = response['articles']

# Filter articles based on date range
today = pd.to_datetime('today').date()
last_year = (df.index >= today - pd.DateOffset(years=1))
articles = [article for article in articles if (pd.to_datetime(article['publishedAt']).date() >= today - pd.DateOffset(years=1))]

# Create a new DataFrame for the sentiment data
sentiment_df = pd.DataFrame(columns=['Ticker', 'title_polarity', 'description_polarity', 'content_polarity', 'date'])

# Analyze the sentiment of each article and add the data to the sentiment DataFrame
for article in articles:
    title = article['title']
    description = article['description']
    content = article['content']
    date = pd.to_datetime(article['publishedAt']).date()

    # Use TextBlob to calculate the polarity of the title and description
    title_polarity = TextBlob(title).sentiment.polarity
    description_polarity = TextBlob(description).sentiment.polarity

    # Use TextBlob to calculate the polarity of the content, if available
    if content:
        content_polarity = TextBlob(content).sentiment.polarity
    else:
        content_polarity = None

    # Add the polarity data to the sentiment DataFrame
    sentiment_df = sentiment_df.append({
        'Ticker': company,
        'title_polarity': title_polarity,
        'description_polarity': description_polarity,
        'content_polarity': content_polarity,
        'date': date
    }, ignore_index=True)

# Convert the date column to a DatetimeIndex
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])
sentiment_df.set_index('date', inplace=True)

# Resample the sentiment data by week and calculate the mean polarity for each week
sentiment_df = sentiment_df.resample('W').mean()

# Merge the sentiment DataFrame with your existing DataFrame
weekly_df = pd.merge(weekly_df, sentiment_df, left_index=True, right_index=True, how='outer')

weekly_df.fillna(0, inplace=True)

# Print the updated DataFrame
print(weekly_df)




