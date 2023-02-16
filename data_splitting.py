from sklearn.model_selection import train_test_split
from data_processing import weekly_df

# Set the input features and target variable
X = weekly_df[['1. open', '2. high', '3. low', '4. close', '6. volume', '10-day MA']]
y = weekly_df['4. close']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Training data shape:", X_train.shape, y_train.shape)
print("Testing data shape:", X_test.shape, y_test.shape)
