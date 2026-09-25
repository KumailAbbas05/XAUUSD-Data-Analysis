import pandas as pd
import matplotlib.pyplot as plt

# Change the file name if your dataset uses a different name.
file_path = "data/xauusd_historical.csv"

df = pd.read_csv(file_path)

print("First 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# Convert Date column if present
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

# Daily return
if "Close" in df.columns:
    df["Daily_Return"] = df["Close"].pct_change() * 100

# Plot closing price
if "Date" in df.columns and "Close" in df.columns:
    plt.figure(figsize=(12, 6))
    plt.plot(df["Date"], df["Close"])
    plt.title("XAUUSD Closing Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.grid(True)
    plt.show()
