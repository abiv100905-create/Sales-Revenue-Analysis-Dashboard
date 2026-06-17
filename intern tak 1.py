import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Sales & Revenue Analysis Dashboard")

# Upload CSV or Excel File
file = st.file_uploader("Upload Sales Data", type=["csv", "xlsx"])

if file is not None:

    # Read file
    if file.name.endswith("task1 intern.csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.subheader("Dataset Preview")
    st.dataframe(df)

    # KPIs
    total_sales = df["Sales"].sum()
    total_revenue = df["Revenue"].sum()

    col1, col2 = st.columns(2)
    col1.metric("Total Sales", f"{total_sales}")
    col2.metric("Total Revenue", f"₹{total_revenue:,.2f}")

    # Revenue Trend
    st.subheader("Revenue Trend")
    revenue_trend = df.groupby("Date")["Revenue"].sum().reset_index()

    fig1 = px.line(
        revenue_trend,
        x="Date",
        y="Revenue",
        title="Revenue Over Time"
    )
    st.plotly_chart(fig1)

    # Top Products
    st.subheader("Top Performing Products")
    top_products = (
        df.groupby("Product")["Revenue"]
        .sum()
        .reset_index()
        .sort_values(by="Revenue", ascending=False)
    )

    fig2 = px.bar(
        top_products,
        x="Product",
        y="Revenue",
        title="Product Revenue"
    )
    st.plotly_chart(fig2)

else:
    st.info("Please upload a CSV or Excel file.")