import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
# Assuming the CSV file has a column named 'Date' for dates and 'Volume' for trading volume
df = pd.read_csv("C:/Users/HP/Downloads/GOOG.csv")

# Convert the 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Define the two specific dates
start_date = '2023-02-20'
end_date = '2024-02-20'

# Filter the DataFrame to include only the rows between the two specific dates
filtered_df = df[(df['Date'] >= start_date) & (df['Date'] <= end_date)]

# Plot the trading volume
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['Date'], filtered_df['Volume'], color='skyblue')
plt.title('Trading Volume of Alphabet Inc.')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
