import pandas as pd

def analyze_data(df):
    analysis = {}

    # Detect numeric and categorical columns
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    cat_cols = df.select_dtypes(exclude=["number"]).columns.tolist()

    if numeric_cols:
        analysis["numeric_summary"] = df[numeric_cols].mean().to_dict()
        analysis["correlations"] = df[numeric_cols].corr().to_dict()
    if cat_cols:
        analysis["categorical_counts"] = {col: df[col].value_counts().to_dict() for col in cat_cols}

    return analysis
