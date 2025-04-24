import pandas as pd

# Load the dataset
df = pd.read_csv('./data/creditcard.csv')

# Filter rows where class value is 1
filtered_df = df[df['Class'] == 1]

# Save the filtered data to a new CSV file
filtered_df.to_csv('filtered_creditcard.csv', index=False)