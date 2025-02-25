from prophet import Prophet
from prophet.diagnostics import cross_validation, performance_metrics
import numpy as np

# Function: Train Prophet Model with MACD, Signal Line, Change %, and RSI Smooth
def train_prophet_model(data, forecast_period=90, changepoint_scale=0.1):
    """Trains a Prophet model with MACD, Signal Line, Change %, and RSI Smooth as regressors."""

    # Define Prophet Model
    model = Prophet(
        seasonality_mode="additive",
        changepoint_prior_scale=changepoint_scale,
        n_changepoints=30,
        weekly_seasonality=False,
        yearly_seasonality=False
    )

    # Adding Monthly & Quarterly Seasonality
    model.add_seasonality(name="monthly", period=30.5, fourier_order=5)
    model.add_seasonality(name="quarterly", period=91.25, fourier_order=7)

    # Adding regressors
    model.add_regressor('MACD')
    model.add_regressor('Signal_Line')
    model.add_regressor('change_scaled')
    model.add_regressor('rsi_smooth')  # Add the smoothed RSI

    # Fit Model
    model.fit(data)

    # Forecasting Future Data
    future = model.make_future_dataframe(periods=forecast_period, freq="D")

    # Extend MACD and Signal Line for future dates
    last_macd = data['MACD'].iloc[-1]
    last_signal = data['Signal_Line'].iloc[-1]
    future['MACD'] = list(data['MACD'].values) + [last_macd] * (len(future) - len(data))
    future['Signal_Line'] = list(data['Signal_Line'].values) + [last_signal] * (len(future) - len(data))
    
    # Ensure 'change_scaled' and 'rsi_smooth' match future dataframe length
    last_value_change = data['change_scaled'].iloc[-1]
    future['change_scaled'] = list(data['change_scaled'].values) + [last_value_change] * (len(future) - len(data))
    
    last_value_rsi_smooth = data['rsi_smooth'].iloc[-1]
    future['rsi_smooth'] = list(data['rsi_smooth'].values) + [last_value_rsi_smooth] * (len(future) - len(data))

    forecast = model.predict(future)

    # Cross-Validation (Testing on last 90 days)
    df_cv = cross_validation(model, horizon="90 days")
    df_p = performance_metrics(df_cv)

    # Evaluate Forecast Performance
    accuracy_results = evaluate_forecast_performance(df_p["rmse"], df_p["mape"], df_p["mse"])

    return model, forecast, df_p, accuracy_results

# Function: Evaluate Forecast Accuracy
def evaluate_forecast_performance(rmse_values, mape_values, mse_values):
    """
    Calculates accuracy based on MAPE values.

    Returns:
        dict: Dictionary containing min, max, and average accuracy percentages.
    """
    accuracy_values = [100 - (mape * 100) for mape in mape_values]

    return {
        "Min Accuracy (%)": round(np.min(accuracy_values), 2),
        "Max Accuracy (%)": round(np.max(accuracy_values), 2),
        "Average Accuracy (%)": round(np.mean(accuracy_values), 2)
    }