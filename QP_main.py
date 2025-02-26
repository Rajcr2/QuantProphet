import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from QP_model import train_prophet_model
from QP_insights import analyze_stock_accuracy
from QP_data import preferred_format

# Streamlit setup
st.set_page_config(page_title="Quantitative Market Forecasting Using Prophet & Indicators", layout="wide")

st.title("Quant Prophet")

# Sidebar: Upload Data
uploaded_file = st.sidebar.file_uploader("Upload CSV file", type=["csv"])

# Sidebar: Prophet Parameters
st.sidebar.title("Model Parameters")
changepoint_scale = st.sidebar.slider("Changepoint Prior Scale", 0.01, 0.5, 0.1)
seasonality = "additive"  # Fixed as per the new model
forecast_periods = st.sidebar.slider("Forecast Periods (days)", 1, 365, 90)
st.sidebar.write("by Raj Jangam.")

# Use session state to store data and avoid reloads
if "data" not in st.session_state:
    st.session_state.data = None
if "processed_data" not in st.session_state:
    st.session_state.processed_data = None

# If a file is uploaded, process it
if uploaded_file:
    # Step 1: Load the uploaded CSV file into a DataFrame
    st.session_state.data = pd.read_csv(uploaded_file)
    
    # Step 2: Convert the data to preferred format
    preferred_format()

    # Step 3: Display the processed data
    st.write("### Stock Data Preview")
    st.write(st.session_state.processed_data.head())

    # Step 4: Train Prophet Model and Generate Forecast using sidebar parameters
    st.write("### Prophet Stock Price Forecast")
    model, forecast, df_p, accuracy_results = train_prophet_model(
        st.session_state.processed_data, 
        forecast_period=forecast_periods, 
        changepoint_scale=changepoint_scale
    )

    # Display Forecasted Data
    st.write(forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail())

    # Display Forecast Accuracy
    st.write("### Forecast Accuracy Metrics")
    st.write(df_p[["rmse", "mape", "mse"]])
    st.write("### Forecast Accuracy Summary")
    st.write(accuracy_results)

    # Step 5: Analyze Stock Prediction Accuracy
    stock_name = uploaded_file.name.replace(".csv", "")  # Extract stock name from file name
    stock_insights = analyze_stock_accuracy(
        stock_name, 
        accuracy_results["Stability (Min) (%)"], 
        accuracy_results["Stability (Max) (%)"], 
        accuracy_results["Average Stability (%)"]
    )

    # Step 6: Display Stock Insights
    st.write("### Stock Prediction Insights")
    for key, value in stock_insights.items():
        st.write(f"**{key}:** {value}")

    # Step 7: Plot Forecast
    st.write("### Forecast Visualization")
    # Define x-axis limits: 40% past, 60% future
    start_date = forecast['ds'].iloc[int(len(forecast) * 0.4)]
    end_date = forecast['ds'].iloc[-1]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(forecast["ds"], forecast["yhat"], label="Predicted Price", color="blue")
    ax.fill_between(forecast["ds"], forecast["yhat_lower"], forecast["yhat_upper"], color="blue", alpha=0.2)
    # Format x-axis
    ax.set_xlim([start_date, end_date])
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.xticks(rotation=45)
    ax.set_title("Prophet Stock Price Forecast")
    ax.set_xlabel("Date")
    ax.set_ylabel("Stock Price")
    ax.legend()
    st.pyplot(fig)

    # Download forecast as CSV
    st.write("### Download Forecast Data")
    csv = forecast.to_csv(index=False)
    st.download_button("Download CSV", csv, "forecast.csv", "text/csv")
