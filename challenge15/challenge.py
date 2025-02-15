import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd


data = {
    "Date": pd.date_range(start="2023-01-01", periods=30, freq='D'),
    "Temperature": [round(16.1 + (i % 5) * 1.5, 1) for i in range(30)],
    "Humidity": [round(29 + (i % 3) * 25, 1) for i in range(30)],
    "Atmospheric Pressure": [round(992 + (i % 4) * 10, 1) for i in range(30)]
}

df = pd.DataFrame(data)
df.head()

df = pd.DataFrame(data)


df.to_csv("weather_data.csv", index=False)


df = pd.read_csv("weather_data.csv", parse_dates=["Date"])


print("Average Temperature:", df["Temperature"].mean())
print("Average Humidity:", df["Humidity"].mean())
print("Average Pressure:", df["Pressure"].mean())


def plot_weather_data():
    plt.figure(figsize=(10, 5))
    plt.plot(df["Date"], df["Temperature"], label="Temperature (°C)", marker='o')
    plt.plot(df["Date"], df["Humidity"], label="Humidity (%)", marker='s')
    plt.plot(df["Date"], df["Atmospheric Pressure"], label="Atmospheric Pressure (hPa)", marker='^')
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title("Weather Trends Over Time")
    plt.legend()
    plt.grid()
    plt.show()
