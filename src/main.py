import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Set matplotlib to use 'Agg' backend to work in headless environments
matplotlib.use('Agg')

# Ensure the output directory exists
output_dir = 'output'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load the dataset
data = pd.read_csv('data/medals_total.csv')

# Sort the data by 'Total' column in descending order and take the top 50 countries
top_countries = data.sort_values(by='Total', ascending=False).head(50)

# Generate summary statistics for Total Medals
summary_stats = top_countries['Total'].describe()

# Create a bar chart for total medals by top 50 countries
plt.figure(figsize=(10, 6))
plt.bar(top_countries['country'], top_countries['Total'], color='skyblue')
plt.title('Total Medals by Top 50 Countries')
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.tight_layout()

# Save the plot
plt.savefig(f'{output_dir}/total_medals_by_top_50_countries.png')

# Explicitly close the plot
plt.close()

# Save summary statistics to markdown file
with open(f'{output_dir}/summary_report_top_50.md', 'w') as f:
    f.write("# Summary Statistics Report (Top 50 Countries)\n\n")
    f.write("## Summary Statistics for Total Medals (Top 50 Countries)\n")
    f.write(summary_stats.to_markdown() + "\n\n")
    f.write(f"## Mean Total Medals: \n{summary_stats['mean']}\n")
    f.write(f"## Median Total Medals: \n{summary_stats['50%']}\n")
    f.write(f"## Standard Deviation of Total Medals: \n{summary_stats['std']}\n")
    f.write("## Data Visualization\n")
    f.write("![Total Medals by Top 50 Countries](total_medals_by_top_50_countries.png)\n")

# Print summary statistics for verification
print(summary_stats)
