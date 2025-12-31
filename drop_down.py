# streamlit_drag_drop_dashboard.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Drag & Drop Marketing Dashboard", layout="wide")

st.title("📊 Drag & Drop Marketing Performance Dashboard")
st.markdown("Upload your CSV file with columns like `Date`, `Channel`, `Campaign`, `Creative`, `Spend`, `Revenue`, `Orders`.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload CSV", type=['csv', 'xlsx'])

if uploaded_file:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success("✅ File uploaded successfully!")
        st.dataframe(df.head(5))

        # --- Automatic Column Detection ---
        expected_cols = ['Date','Channel','Campaign','Creative','Spend','Revenue','Orders']
        missing_cols = [c for c in expected_cols if c not in df.columns]
        if missing_cols:
            st.warning(f"Columns missing in the uploaded file: {missing_cols}")
        
        # --- Preprocess Data ---
        df['Date'] = pd.to_datetime(df['Date'])
        df['ROAS'] = df['Revenue'] / df['Spend']
        df['CAC'] = df['Spend'] / df['Orders'].replace(0,1)
        
        # --- KPI Cards ---
        st.markdown("## Key Metrics")
        total_revenue = df['Revenue'].sum()
        total_spend = df['Spend'].sum()
        total_roas = round(total_revenue / total_spend, 2)
        total_cac = round(df['CAC'].mean(), 2)
        total_orders = df['Orders'].sum()
        total_profit = total_revenue - total_spend
        
        kpi1, kpi2, kpi3, kpi4, kpi5, kpi6 = st.columns(6)
        kpi1.metric("Total Revenue", f"${total_revenue:,.0f}")
        kpi2.metric("Total Ad Spend", f"${total_spend:,.0f}")
        kpi3.metric("ROAS", f"{total_roas}x")
        kpi4.metric("CAC", f"${total_cac}")
        kpi5.metric("Orders / Leads", f"{total_orders}")
        kpi6.metric("Net Profit", f"${total_profit:,.0f}")
        
        st.markdown("---")
        
        # --- Time Series Chart ---
        st.markdown("## Revenue & Spend Over Time")
        time_df = df.groupby('Date')[['Revenue','Spend']].sum().reset_index()
        fig_time = px.line(time_df, x='Date', y=['Revenue','Spend'], title="Revenue vs Spend Over Time")
        st.plotly_chart(fig_time, use_container_width=True)
        
        st.markdown("---")
        
        # --- Channel Performance ---
        st.markdown("## Channel Performance")
        channel_df = df.groupby('Channel')[['Revenue','Spend']].sum().reset_index()
        channel_df['ROAS'] = channel_df['Revenue'] / channel_df['Spend']
        channel_df['CAC'] = channel_df['Spend'] / df.groupby('Channel')['Orders'].sum().replace(0,1).values
        
        c1, c2 = st.columns([2,1])
        c1.dataframe(channel_df)
        fig_channel = px.bar(channel_df, x='Channel', y='Revenue', title="Revenue by Channel")
        c2.plotly_chart(fig_channel, use_container_width=True)
        
        st.markdown("---")
        
        # --- Campaign Performance ---
        st.markdown("## Campaign Performance")
        campaign_df = df.groupby('Campaign')[['Revenue','Spend']].sum().reset_index()
        campaign_df['ROAS'] = campaign_df['Revenue'] / campaign_df['Spend']
        top_campaigns = campaign_df.nlargest(5,'Revenue')
        bottom_campaigns = campaign_df.nsmallest(5,'ROAS')
        
        cp1, cp2 = st.columns(2)
        fig_top_campaigns = px.bar(top_campaigns, x='Revenue', y='Campaign', orientation='h', title="Top 5 Campaigns by Revenue")
        fig_bottom_campaigns = px.bar(bottom_campaigns, x='ROAS', y='Campaign', orientation='h', title="Bottom 5 Campaigns by ROAS")
        cp1.plotly_chart(fig_top_campaigns, use_container_width=True)
        cp2.plotly_chart(fig_bottom_campaigns, use_container_width=True)
        
        st.markdown("---")
        
        # --- Creative Performance ---
        st.markdown("## Creative Performance")
        creative_df = df.groupby('Creative')[['Revenue','Spend']].sum().reset_index()
        creative_df['ROAS'] = creative_df['Revenue'] / creative_df['Spend']
        creative_df['Status'] = np.where(creative_df['ROAS'] > 2, 'Good','Needs Review')
        st.dataframe(creative_df)
        
        st.markdown("---")
        
        # --- Spend & Revenue Distribution ---
        st.markdown("## Spend & Revenue Distribution")
        dist1, dist2 = st.columns(2)
        fig_spend = px.pie(channel_df, names='Channel', values='Spend', title="Spend Distribution")
        fig_revenue = px.pie(channel_df, names='Channel', values='Revenue', title="Revenue Distribution")
        dist1.plotly_chart(fig_spend, use_container_width=True)
        dist2.plotly_chart(fig_revenue, use_container_width=True)
        
        st.markdown("---")
        
        # --- Automated Insight Box ---
        st.markdown("## Key Insights")
        top_channel = channel_df.loc[channel_df['Revenue'].idxmax()]['Channel']
        top_roas = channel_df['ROAS'].max()
        st.info(f"Top performing channel: {top_channel} with ROAS {top_roas:.2f}x")
        
    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
else:
    st.info("Upload your CSV/Excel file to generate the dashboard.")
