# ReguData — Interactive Data Analysis Dashboard

## Overview
ReguData is an interactive Streamlit dashboard for exploring, analyzing, and summarizing datasets.  
Upload any CSV file to visualize trends, inspect statistics, and generate automated insights.

## Key Features
- Data upload and preview
- Automatic statistical summaries
- Numeric and categorical column detection
- Dynamic bar charts and correlation heatmaps
- Downloadable analysis report

## Tech Stack
| Layer | Technology | Purpose |
|-------|-------------|----------|
| Backend | Python 3.11 | Data analysis |
| Framework | Streamlit | Web app interface |
| Libraries | Pandas, Seaborn, Matplotlib | Data visualization and insights |
| Environment | Conda (`regudata`) | Isolated environment for reproducibility |

## Folder Structure
ReguData/
│
├── app.py               # Streamlit interface
├── analyzer.py          # Analysis logic
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── data/                # (Optional) Example datasets

## Getting Started
1. Activate your environment:
   ```bash
   conda activate regudata
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
4. Open your browser at `http://localhost:8501`

## Future Enhancements
- Add advanced visualizations (boxplots, scatter matrices)
- Integrate machine learning insights (regression, clustering)
- Expand export options (PDF, HTML reports)

## License
This project is licensed under the MIT License. See the LICENSE file for details.
