# Function: Analyze Stock Prediction Accuracy
def analyze_stock_accuracy(stock_name, min_acc, max_acc, avg_acc):
    
    accuracy_range = max_acc - min_acc
    insights = {}

    # Determine Stock Stability
    if avg_acc >= 90 and min_acc >= 85:
        insights["Stability"] = "Very High (Stock is stable with minimal risk)"
        insights["Investment Advice"] = "Best for long-term and passive investors."
    elif avg_acc >= 85 and min_acc >= 75 and max_acc >= 95:
        insights["Stability"] = "High (Stock is generally stable but has occasional spikes)"
        insights["Investment Advice"] = "Good for long-term, can also be used for swing trading."
    elif avg_acc >= 80 and min_acc >= 70:
        insights["Stability"] = "Moderate (Predictable but with some fluctuations)"
        insights["Investment Advice"] = "Safe for long-term but requires periodic review."
    elif avg_acc >= 75 and (min_acc >= 65 or max_acc >= 95):
        insights["Stability"] = "Low-Moderate (Stock fluctuates but has growth potential)"
        insights["Investment Advice"] = "Risky for long-term but good for short-term trading."
    else:
        insights["Stability"] = "Low (Highly Unpredictable, risky for long-term holding)"
        insights["Investment Advice"] = "Best suited for short-term, day trading, or options."

    # Volatility Analysis (Considering max, min, and range)
    if accuracy_range < 5 and avg_acc >= 85:
        insights["Volatility"] = "Very Low (Highly stable, predictable stock)"
        insights["Trading Advice"] = "Safe for long-term SIPs and passive investments."
    elif accuracy_range < 10 and avg_acc >= 80:
        insights["Volatility"] = "Low (Mild fluctuations, good for holding)"
        insights["Trading Advice"] = "Best for holding 3+ years with low risk."
    elif accuracy_range < 20 and avg_acc >= 75:
        insights["Volatility"] = "Moderate (Stock moves but within reasonable limits)"
        insights["Trading Advice"] = "Can be used for swing trading and medium-term strategies."
    elif accuracy_range >= 20 and avg_acc >= 70:
        insights["Volatility"] = "High (Frequent price swings, needs active monitoring)"
        insights["Trading Advice"] = "Ideal for short-term traders using RSI & MACD."
    else:
        insights["Volatility"] = "Very High (Extremely unpredictable, risky)"
        insights["Trading Advice"] = "Best for aggressive traders, avoid long-term holding."


    return insights
