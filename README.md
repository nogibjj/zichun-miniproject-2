# Mini Project 2

This project performs descriptive statistics and generates a data visualization for the total medals won by countries in the Paris 2024 Olympic Games. The dataset is sourced from Kaggle.

## Dataset

The dataset used for this analysis is the 'medals_total.csv' file, which contains the total medals won by various countries in the Paris 2024 Olympic Games.

## Features

1. **Descriptive Statistics**:
   - Count, mean, standard deviation, min, max, and percentiles of total medals won by all countries.

2. **Data Visualization**:
   - A bar chart showing the total medals won by the top 50 countries.

3. **Output**:
   - Summary statistics for the entire dataset saved as `summary_report.md`.
   - A visualization saved as `total_medals_by_top_50_countries.png` for the top 50 countries by total medal count.

## Instructions

1. **Clone the repository**:
    ```bash
    git clone <your-repo-url>
    cd <repo-directory>
    ```

2. **Install the required dependencies**:
    Ensure you have Python 3.6+ installed. Then, install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the script**:
    Run the Python script to generate the summary statistics and the visualization.
    ```bash
    python src/main.py
    ```

4. **CI/CD Pipeline**:
    The CI/CD pipeline automatically runs the script, generates the markdown report and visualization, and pushes them to the repository if there are changes.

## Deliverables

1. **Repository URL**: [Link to the public repository](https://github.com/nogibjj/zichun-miniproject-2/)

2. **Summary Report**: The `summary_report.md` file containing descriptive statistics.

3. **Visualization**: The `total_medals_by_top_50_countries.png` showing the total medals won by the top 50 countries.
