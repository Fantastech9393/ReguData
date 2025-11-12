
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
from analyzer import analyze_data

st.set_page_config(page_title="ReguData — AI-Powered Data Analysis Tool", layout="wide")

st.title("ReguData — Data Analysis Dashboard")

st.sidebar.header("Upload Your Dataset")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    # Fix column display names
    df.columns = [col.replace("YearsAtCompany", "Years At Company") for col in df.columns]

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Visual Insights")
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    if len(numeric_cols) > 0:
        st.write(f"Numeric columns detected: {len(numeric_cols)}")

        # ✅ Bar chart of raw data (not mean)
        st.write("### Numeric Comparison by Employee")
        df_melted = df.melt(id_vars=df.columns[0], value_vars=numeric_cols)
        fig, ax = plt.subplots()
        sns.barplot(x=df_melted.columns[0], y="value", hue="variable", data=df_melted, ax=ax)
        ax.set_ylabel("Values")
        ax.set_xlabel("Employee")
        ax.set_title("Raw Data Comparison")
        st.pyplot(fig)

        # Correlation heatmap
        st.write("Heatmap of numeric correlations:")
        fig, ax = plt.subplots()
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("No numeric columns detected.")

    st.subheader("Automated Insights")
    analysis = analyze_data(df)
    st.write(analysis)

    # Excel export
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        # Sheet 1: Summary (stats)
        summary = df.describe(include="all").transpose()
        summary.to_excel(writer, index=True, sheet_name="Summary")

        # Sheet 2: Insights (text)
        insights_df = pd.DataFrame({"Insights": [analysis]})
        insights_df.to_excel(writer, index=False, sheet_name="Insights")

    st.download_button(
        label="📊 Download Excel Report",
        data=output.getvalue(),
        file_name="data_analysis_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.info("Upload a CSV file from the sidebar to get started.")
