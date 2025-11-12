import pandas as pd

def describe_data(df: pd.DataFrame) -> dict:
    return {
        "Shape": df.shape,
        "Columns": df.columns.tolist(),
        "Missing Values": df.isnull().sum().to_dict(),
        "Data Types": df.dtypes.astype(str).to_dict()
    }

def generate_report(df: pd.DataFrame, analysis: str) -> str:
    report = [
        "=== DATA REPORT ===",
        f"Shape: {df.shape}",
        "\n--- COLUMN TYPES ---\n",
        str(df.dtypes),
        "\n--- ANALYSIS ---\n",
        analysis
    ]
    return "\n".join(report)
