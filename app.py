# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

DATA_PATH = "data/superstore.csv"

@st.cache_data
def load_data():
    df = pd.read_csv(DATA_PATH, parse_dates=["Order Date"], dayfirst=False, low_memory=False)
    df["Order Month"] = df["Order Date"].dt.to_period("M").astype(str)
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce").fillna(0)
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce").fillna(0)
    return df

df = load_data()
st.set_page_config(page_title="Superstore Dashboard", layout="wide")
st.title("Superstore Sales Dashboard")

# KPI row
tot_sales = df["Sales"].sum()
tot_profit = df["Profit"].sum()
tot_orders = df["Order ID"].nunique()

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"${tot_sales:,.2f}")
col2.metric("Total Profit", f"${tot_profit:,.2f}")
col3.metric("Total Orders", f"{tot_orders:,}")

# Filters
region = st.sidebar.multiselect("Region", options=df["Region"].unique(), default=df["Region"].unique())
category = st.sidebar.multiselect("Category", options=df["Category"].unique(), default=df["Category"].unique())
df_filtered = df[(df["Region"].isin(region)) & (df["Category"].isin(category))]

# Sales over time
st.subheader("Sales & Profit Over Time")
sales_time = df_filtered.groupby("Order Month").agg({"Sales":"sum","Profit":"sum"}).reset_index()
fig1 = px.line(sales_time, x="Order Month", y=["Sales","Profit"], labels={"value":"Amount","Order Month":"Month"})
st.plotly_chart(fig1, use_container_width=True)

# Category breakdown
st.subheader("Category Breakdown")
cat = df_filtered.groupby("Category").agg({"Sales":"sum","Profit":"sum","Order ID":"nunique"}).reset_index().rename(columns={"Order ID":"Orders"})
fig2 = px.bar(cat, x="Category", y="Sales", text="Profit")
st.plotly_chart(fig2, use_container_width=True)

# Top products
st.subheader("Top Products by Sales")
top = df_filtered.groupby("Product ID").agg({"Sales":"sum","Profit":"sum"}).reset_index().sort_values("Sales", ascending=False).head(10)
st.dataframe(top)
