# TASK 2: Unemployment Analysis with Python

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
# Replace 'Unemployment.csv' with your dataset file name
df = pd.read_csv("Unemployment.csv")

# Display First 5 Rows
print("First 5 Rows of Dataset:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()

# Display Column Names
print("\nColumn Names:")
print(df.columns)

# Convert Date Column to Datetime Format
# Replace 'Date' with your dataset date column name
df['Date'] = pd.to_datetime(df['Date'])

# Extract Month and Year
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

# Basic Statistics
print("\nStatistical Summary:")
print(df.describe())

# Average Unemployment Rate
# Replace 'Estimated Unemployment Rate (%)' with your column name
avg_rate = df['Estimated Unemployment Rate (%)'].mean()
print("\nAverage Unemployment Rate:", avg_rate)

# Unemployment Rate by Region
region_data = df.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

print("\nAverage Unemployment Rate by Region:")
print(region_data)

# Plot Unemployment Rate by Region
plt.figure(figsize=(10,5))
region_data.plot(kind='bar')
plt.title("Average Unemployment Rate by Region")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.show()

# Monthly Unemployment Trend
monthly_data = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(10,5))
monthly_data.plot(marker='o')
plt.title("Monthly Unemployment Trend")
plt.xlabel("Month")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# Yearly Unemployment Trend
yearly_data = df.groupby('Year')['Estimated Unemployment Rate (%)'].mean()

plt.figure(figsize=(8,5))
yearly_data.plot(marker='o')
plt.title("Yearly Unemployment Trend")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# Covid-19 Impact Analysis
covid_data = df[df['Year'] >= 2020]

plt.figure(figsize=(10,5))
plt.plot(covid_data['Date'],
         covid_data['Estimated Unemployment Rate (%)'])

plt.title("Covid-19 Impact on Unemployment")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)
plt.show()

# Highest Unemployment Region
highest_region = region_data.idxmax()
highest_value = region_data.max()

print("\nRegion with Highest Unemployment:")
print(highest_region, "-", highest_value)

# Save Cleaned Dataset
df.to_csv("Cleaned_Unemployment_Data.csv", index=False)

print("\nAnalysis Completed Successfully!")