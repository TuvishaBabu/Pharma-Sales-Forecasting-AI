import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from prophet import Prophet

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="AI Pharma Demand Forecasting Dashboard",
    page_icon="💊",
    layout="wide"
)

# ---------------- CUSTOM UI STYLING ----------------
st.markdown("""
<style>

.main {
    background-color: #f8fafc;
}

h1, h2, h3 {
    color: #1e293b;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

section[data-testid="stSidebar"] {
    background-color: #eef2ff;
}

hr {
    margin-top: 30px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.title("💊 AI-Powered Pharma Demand Forecasting Dashboard")
st.markdown(
    "Forecast pharmaceutical demand using AI and time series forecasting."
)

# -------------------------------
# LOAD DATA
# -------------------------------
daily_sales = pd.read_csv("data/salesdaily.csv")
monthly_sales = pd.read_csv("data/salesmonthly.csv")

daily_sales['datum'] = pd.to_datetime(daily_sales['datum'])
monthly_sales['datum'] = pd.to_datetime(monthly_sales['datum'])

drug_columns = [
    'M01AB',
    'M01AE',
    'N02BA',
    'N02BE',
    'N05B',
    'N05C',
    'R03',
    'R06'
]

# -------------------------------
# TOTAL SALES
# -------------------------------
daily_sales['Total_Sales'] = daily_sales[
    drug_columns
].sum(axis=1)

monthly_sales['Total_Sales'] = monthly_sales[
    drug_columns
].sum(axis=1)

# -------------------------------
# SIDEBAR
# -------------------------------
st.sidebar.title("Dashboard Menu")

page = st.sidebar.radio(
    "Navigate",
    [
        "Dashboard Home",
        "Sales Analysis",
        "AI Forecasting",
        "Business Insights"
    ]
)

# ==================================================
# DASHBOARD HOME
# ==================================================
if page == "Dashboard Home":
    st.header("📊 Dashboard Overview")

    # KPI Calculations
    total_sales = round(
        daily_sales['Total_Sales'].sum(), 2
    )

    highest_drug = (
        daily_sales[drug_columns]
        .sum()
        .idxmax()
    )

    growth = round(
        (
            monthly_sales['Total_Sales'].iloc[-2]
            - monthly_sales['Total_Sales'].iloc[0]
        )
        /
        monthly_sales['Total_Sales'].iloc[0]
        * 100,
        2
    )

    # Forecasted demand
    forecast_data = monthly_sales[
        ['datum', 'Total_Sales']
    ].copy()

    forecast_data.columns = ['ds', 'y']

    model = Prophet()

    model.fit(forecast_data)

    future = model.make_future_dataframe(
        periods=1,
        freq='ME'
    )

    forecast = model.predict(future)

    forecasted_demand = round(
        forecast['yhat'].iloc[-1],
        0
    )

    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "💰 Total Sales",
        f"{total_sales:,.0f}"
    )

    col2.metric(
        "🏆 Highest Selling Drug",
        highest_drug
    )

    col3.metric(
        "📈 Growth %",
        f"{growth}%"
    )

    col4.metric(
        "🔮 Forecasted Demand",
        f"{forecasted_demand:,.0f}"
    )

    st.divider()

    # Monthly Trend
    st.subheader("📈 Monthly Sales Trend")

    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        monthly_sales['datum'],
        monthly_sales['Total_Sales'],
        marker='o'
    )

    ax.set_title(
        "Monthly Pharmaceutical Sales Trend"
    )

    ax.set_xlabel("Year")
    ax.set_ylabel("Sales")

    st.pyplot(fig)

    st.divider()

    # Category Comparison
    st.subheader(
        "💊 Medicine Category Comparison"
    )

    category_sales = (
        daily_sales[drug_columns]
        .sum()
        .sort_values(ascending=False)
    )

    fig2, ax2 = plt.subplots(
        figsize=(10,5)
    )

    ax2.bar(
        category_sales.index,
        category_sales.values
    )

    ax2.set_title(
        "Sales by Medicine Category"
    )

    ax2.set_xlabel("Medicine Category")
    ax2.set_ylabel("Sales")

    st.pyplot(fig2)
# ==================================================
# SALES ANALYSIS
# ==================================================
elif page == "Sales Analysis":

    st.header("📉 Sales Analysis")

    st.subheader(
        "Daily Sales Trend"
    )

    fig, ax = plt.subplots(
        figsize=(12, 5)
    )

    ax.plot(
        daily_sales['datum'],
        daily_sales['Total_Sales']
    )

    ax.set_title(
        "Daily Sales Trend"
    )

    st.pyplot(fig)

    st.subheader(
        "Drug Correlation Heatmap"
    )

    fig2, ax2 = plt.subplots(
        figsize=(10, 6)
    )

    sns.heatmap(
        daily_sales[
            drug_columns
        ].corr(),
        annot=True,
        cmap="coolwarm",
        ax=ax2
    )

    st.pyplot(fig2)

# ==================================================
# AI FORECASTING
# ==================================================
elif page == "AI Forecasting":

    st.header(
        "🤖 AI Demand Forecasting"
    )

    selected_drug = st.selectbox(
        "💊 Select Medicine Category",
        drug_columns
    )

    forecast_data = monthly_sales[
        ['datum', selected_drug]
    ].copy()

    forecast_data.columns = [
        'ds',
        'y'
    ]

    model = Prophet()
    model.fit(forecast_data)

    future = model.make_future_dataframe(
        periods=12,
        freq='ME'
    )

    forecast = model.predict(
        future
    )

    st.subheader(
        f"📈 12-Month Forecast for {selected_drug}"
    )

    fig1 = model.plot(
        forecast
    )

    st.pyplot(fig1)

    st.divider()

    st.subheader(
        "📊 Trend & Seasonality Analysis"
    )

    fig2 = model.plot_components(
        forecast
    )

    st.pyplot(fig2)

    st.divider()

    st.subheader(
        "📋 Forecast Results"
    )

    forecast_output = forecast[
        [
            'ds',
            'yhat',
            'yhat_lower',
            'yhat_upper'
        ]
    ].tail(12)

    st.dataframe(
        forecast_output
    )

    next_month = round(
        forecast_output[
            'yhat'
        ].iloc[0],
        2
    )

    final_month = round(
        forecast_output[
            'yhat'
        ].iloc[-1],
        2
    )

    change = round(
        (
            final_month
            -
            next_month
        )
        /
        next_month
        * 100,
        2
    )

    st.subheader(
        "🧠 AI Prediction Insight"
    )

    if change > 0:
        st.success(
            f"Demand for {selected_drug} is expected to increase by {change}% over the next 12 months."
        )
    else:
        st.warning(
            f"Demand for {selected_drug} may decline by {abs(change)}% over the next 12 months."
        )

    csv = forecast_output.to_csv(
        index=False
    )

    st.download_button(
        label="⬇ Download Forecast CSV",
        data=csv,
        file_name=f"{selected_drug}_forecast.csv",
        mime="text/csv"
    )

# ==================================================
# BUSINESS INSIGHTS
# ==================================================
elif page == "Business Insights":

    st.header(
        "📊 Smart Business Insights"
    )

    st.markdown(
        "AI-generated pharmaceutical demand insights for better business decision-making."
    )

    st.divider()

    category_sales = {}

    for drug in drug_columns:
        category_sales[
            drug
        ] = daily_sales[
            drug
        ].sum()

    insights_df = pd.DataFrame(
        list(
            category_sales.items()
        ),
        columns=[
            "Medicine",
            "Total Sales"
        ]
    )

    highest_drug = insights_df.loc[
        insights_df[
            "Total Sales"
        ].idxmax()
    ]

    lowest_drug = insights_df.loc[
        insights_df[
            "Total Sales"
        ].idxmin()
    ]

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🏆 Highest Selling Medicine",
            highest_drug["Medicine"],
            f'{highest_drug["Total Sales"]:,.0f}'
        )

    with col2:
        st.metric(
            "📉 Lowest Selling Medicine",
            lowest_drug["Medicine"],
            f'{lowest_drug["Total Sales"]:,.0f}'
        )

    st.divider()

    st.subheader(
        "🧠 AI Business Recommendations"
    )

    st.info(
        f"""
### Key Recommendations

✅ Prioritize inventory for **{highest_drug["Medicine"]}**

⚠ Review strategy for **{lowest_drug["Medicine"]}**

📦 Use AI forecasting for stock optimization

📈 Monitor seasonal demand spikes

💡 Use forecasted trends for procurement planning
"""
    )

    st.divider()

    st.subheader(
        "💊 Sales Distribution by Medicine"
    )

    fig, ax = plt.subplots(
        figsize=(10, 5)
    )

    ax.bar(
        insights_df["Medicine"],
        insights_df["Total Sales"]
    )

    ax.set_title(
        "Medicine Category Sales Distribution"
    )

    ax.set_xlabel(
        "Medicine Category"
    )

    ax.set_ylabel(
        "Total Sales"
    )

    st.pyplot(fig)

    csv = insights_df.to_csv(
        index=False
    )

    st.download_button(
        label="⬇ Download Insights CSV",
        data=csv,
        file_name="business_insights.csv",
        mime="text/csv"
    )