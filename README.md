
# 💊 AI-Powered Pharma Demand Forecasting Dashboard

## 📌 Project Overview

The **AI-Powered Pharma Demand Forecasting Dashboard** is an intelligent pharmaceutical sales analytics and demand forecasting system built using **Python, Streamlit, and Facebook Prophet**.

This project analyzes pharmaceutical sales trends, predicts future medicine demand using **time series forecasting**, and provides **business insights and recommendations** for inventory planning and sales optimization.

The dashboard helps pharmaceutical companies, healthcare providers, and supply chain teams make **data-driven decisions** by identifying demand patterns and forecasting future medicine requirements.

---

## 🚀 Live Demo

🔗 Streamlit App:  
https://pharma-sales-forecasting-ai-edjsq8twa6ebk3pyad53rf.streamlit.app

---

## 📂 GitHub Repository

🔗 GitHub Link:  
https://github.com/TuvishaBabu/Pharma-Sales-Forecasting-AI

---

# ✨ Key Features

## 📊 1. Dashboard Overview
Provides a quick snapshot of pharmaceutical business performance.

Features:
- 💰 Total pharmaceutical sales
- 🏆 Highest selling medicine category
- 📈 Sales growth percentage
- 🔮 Forecasted demand insights

---

## 📉 2. Sales Analysis
Helps analyze medicine sales performance.

Features:
- Daily sales trend visualization
- Monthly sales trend analysis
- Drug correlation heatmap
- Medicine category comparison

---

## 🤖 3. AI Demand Forecasting
Uses **Prophet Time Series Forecasting** to predict medicine demand.

Features:
- Medicine category selection
- 12-month future forecasting
- Trend and seasonality analysis
- AI-generated prediction insights
- Downloadable forecast CSV

---

## 🧠 4. Business Insights
Provides intelligent pharmaceutical business recommendations.

Features:
- Highest selling medicine identification
- Lowest selling medicine detection
- Sales growth analysis
- Inventory optimization recommendations
- Procurement planning suggestions

---

# 🛠 Technology Stack

### Programming Language
- Python

### Data Analysis & Processing
- Pandas
- NumPy

### Visualization
- Matplotlib
- Seaborn

### Machine Learning / Forecasting
- Prophet (Facebook Prophet)

### Web Framework
- Streamlit

### Version Control
- Git
- GitHub

### Deployment
- Streamlit Cloud

---

# 🧪 Machine Learning Technique Used

### Time Series Forecasting using Prophet

The project uses the **Prophet forecasting model** to predict future pharmaceutical demand.

Why Prophet?
- Handles seasonality effectively
- Works well with time-series data
- Automatically detects trends
- Easy forecasting for future demand planning

Forecasting Process:
1. Historical monthly sales data collected
2. Data preprocessed and formatted
3. Prophet model trained
4. Future sales demand predicted
5. Trend and seasonality analyzed

---

# 📁 Dataset Information

The project uses pharmaceutical sales datasets:

| File Name | Description |
|------------|-------------|
| `salesdaily.csv` | Daily medicine sales |
| `salesweekly.csv` | Weekly medicine sales |
| `salesmonthly.csv` | Monthly medicine sales |
| `saleshourly.csv` | Hourly medicine sales |

### Medicine Categories Used
- M01AB
- M01AE
- N02BA
- N02BE
- N05B
- N05C
- R03
- R06

---

# 📂 Project Structure

```text
Pharma-Sales-Forecasting-AI/
│── dashboard/
│   └── app.py
│
│── data/
│   ├── salesdaily.csv
│   ├── salesweekly.csv
│   ├── salesmonthly.csv
│   └── saleshourly.csv
│
│── outputs/
│   └── pharma_sales_forecast.csv
│
│── 01_data_analysis.ipynb
│── requirements.txt
│── README.md
````

---

# ⚙️ Installation & Local Setup

Follow these steps to run the project locally.

## Step 1: Clone Repository

```bash
git clone https://github.com/TuvishaBabu/Pharma-Sales-Forecasting-AI.git
```

---

## Step 2: Navigate to Project Folder

```bash
cd Pharma-Sales-Forecasting-AI
```

---

## Step 3: Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate Virtual Environment:

```bash
venv\Scripts\activate
```

---

## Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## Step 5: Run Streamlit Application

```bash
streamlit run dashboard/app.py
```

---

## Step 6: Open in Browser

The application will run at:

```text
http://localhost:8501
```


# 📈 Business Impact

This project can help pharmaceutical businesses:

✅ Predict future medicine demand

✅ Reduce stock shortages

✅ Prevent overstocking

✅ Improve inventory planning

✅ Optimize supply chain management

✅ Make data-driven business decisions

---

# 🔮 Future Improvements

Planned enhancements include:

* Real-time pharmaceutical sales integration
* Advanced machine learning forecasting models (LSTM, XGBoost)
* Medicine-wise filtering system
* Interactive dashboards with advanced analytics
* Cloud database integration
* User authentication system
* Export dashboard reports as PDF
* Role-based admin dashboard
* API integration for live pharmaceutical data

---

# 🧑‍💻 Author

## Tuvisha B

**B.Tech – Artificial Intelligence & Data Science**
RMK College of Engineering and Technology

### Connect With Me

GitHub:
[https://github.com/TuvishaBabu](https://github.com/TuvishaBabu)

LinkedIn:
www.linkedin.com/in/tuvisha-babu 

---

# ⭐ If you found this project useful, give it a star on GitHub!

````

Then push it:

```powershell
git add .
git commit -m "Updated professional README"
git push
````

This version looks much stronger for recruiters and portfolio reviews.
