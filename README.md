# 📊 Marketing Performance Dashboard

An interactive, data-driven dashboard built with **Streamlit** and **Plotly** to visualize marketing campaign performance. This tool allows users to upload marketing data (CSV or Excel) and instantly generate KPIs, time-series analysis, and channel-level insights.

## ✨ Features
* **Automated KPI Calculation:** Instantly view Total Revenue, Ad Spend, ROAS, CAC, and Net Profit.
* **Data Visualization:** * Revenue vs. Spend time-series charts.
    * Channel performance breakdown with bar charts.
    * Top 5 and Bottom 5 Campaign analysis.
    * Spend and Revenue distribution (Pie charts).
* **Creative Analysis:** Automatically flags creatives as "Good" or "Needs Review" based on ROAS.
* **Flexible Uploads:** Supports both `.csv` and `.xlsx` files.

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.8+ installed.

### 2. Installation
Clone this repository and install the required dependencies:

```bash
git clone [https://github.com/YOUR_USERNAME/marketing-performance-dashboard.git](https://github.com/YOUR_USERNAME/marketing-performance-dashboard.git)
cd marketing-performance-dashboard
pip install -r requirements.txt
Note: If you don't have a requirements.txt, create one with the following content:

Plaintext

streamlit
pandas
numpy
plotly
openpyxl
3. Running the App
Launch the dashboard using the Streamlit CLI:

Bash

streamlit run drop_down.py
📂 Data Format
To ensure the dashboard works correctly, your uploaded file should contain the following columns:

Date: (e.g., YYYY-MM-DD)

Channel: (e.g., Facebook, Google, TikTok)

Campaign: Name of the campaign

Creative: Name/ID of the ad creative

Spend: Advertising cost

Revenue: Sales generated

Orders: Number of conversions

🛠️ Built With
Streamlit - The fastest way to build and share data apps.

Pandas - Data manipulation and analysis.

Plotly - Interactive graphing library.

Developed for marketing teams to simplify data reporting.


---

