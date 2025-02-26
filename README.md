# Prophet-Driven Quant Forecasting.

## Introduction

This is the Next Version of my Prophet based Stock Forecasting (https://github.com/Rajcr2/Prophet-Forecasting) Project.

So, In this project, I have developed a scalable time-series forecasting pipeline using Prophet, designed for quantitative financial forecasting to predict the future stock price of a given company or entity, specifically focusing on its performance month/year ahead. The pipeline integrates critical features such as seasonality, holiday effects, and trend analysis to predict future stock price movements and to provide accurate and actionable forecasts.

### Key Features

1. **Prophet-based time series forecasting**
2. **Incorporates MACD, Change %, RSI (7) as regressors**
3. **Significant error reduction from ~400-500 points (old version) to ~200-250 points in the improved model.**

### Objectives

The primary goal of this project is to create a time-series forecasting system that can:

1. Analyze historical data to predict future trends.
2. Provide Investor a realistic Forecast.
3. Based on the metrics to generate insights that will provide investor a assistance.

### Prerequisites
To run this project, you need to install the following libraries:
### Required Libraries

- **Python 3.12+**
- **Pandas**: This library performs data manipulation and analysis also provides powerful data structures like dataframes.
- **Prophet**: A forecasting tool for time-series data, designed to handle trends, seasonality and holidat effects.
- **Scikit-Learn**: Scikit-learn library provides tools for machine learning, including scalling, classification, regression, clustering, and dimensionality reduction.
- **Streamlit**: Streamlit is a framework that builds interactive, data-driven web applications directly in python.  

Other Utility Libraries : **matplotlib**, **numpy**.

### Installation

   ```
   pip install pandas
   pip install prophet
   pip install numpy
   pip install streamlit
   pip install scikit-learn
   pip install matplotlib
   ```

### Procedure

1.   Create new directory **'Quant Prophet'**.
2.   Inside that directory/folder create new environment.
   
   ```
   python -m venv qp
   ```

  Now, activate this **'qp'** venv.
  
4.   Clone this Repository :

   ```
   git clone https://github.com/RJ2ndgit/NGAIF-Stories_Chatbot.git
   ```
5.   Now, Install all mentioned required libraries in your environment.
6.   After, that Run **'QP_main.py'** file from Terminal. To activate the dashboard on your browser.
   ```
   streamlit run QP_main.py
   ``` 
7. Now, move to your browser.
8. Upload the csv file from your local machine or you can use sample csv file given here.
9. After, uploading set the model parameters such as changepoint or forecast period.
10. Then within few minutes prophet will train the model after that you will see forecast results along with insights.



### Output

1. #### ADANI Green Ltd.

**Forecast** :

![image](https://github.com/user-attachments/assets/c29a90f7-676e-4b98-90cf-34b2e729bda2)

**Insight** :

![image](https://github.com/user-attachments/assets/e1b843f2-d87c-47be-8e6e-c4bd0a0df9bc)


2. #### Reliance Industries Ltd.

**Forecast** :

![image](https://github.com/user-attachments/assets/8419597c-558f-454a-aac4-f2d0600c5160)

**Insight** :

![image](https://github.com/user-attachments/assets/40cb3ef5-19db-4101-af07-3f96ec9ab123)


3. #### INFOSYS

 **Forecast** :

![image](https://github.com/user-attachments/assets/cb39d095-c768-4ff6-8eba-5971e7372ab9)


**Insight** :  

![image](https://github.com/user-attachments/assets/2856e767-73da-4380-9281-ff2d374339f7)


### Conclusion

Based on error metrics, the model has provided valuable insights. Additionally, it has captured the trend effectively, achieving approximately 60% accuracy in actual forecasts.


