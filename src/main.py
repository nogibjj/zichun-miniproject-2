import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('data/medals_total.csv')

# Generate summary statistics for Total Medals
summary_stats = data['Total'].describe()

# Additional statistics
mean_total = data['Total'].mean()
median_total = data['Total'].median()
std_total = data['Total'].std()

matplotlib.use('Agg')

# Create a bar chart for total medals by country
plt.figure(figsize=(10, 6))
plt.bar(data['country'], data['Total'], color='skyblue')
plt.title('Total Medals by Country')
plt.xlabel('Country')
plt.ylabel('Total Medals')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('output/total_medals_by_country.png')

plt.close()

# Save summary statistics to markdown file
with open('output/summary_report.md', 'w') as f:
    f.write("# Summary Statistics Report\n\n")
    f.write("## Summary Statistics for Total Medals\n")
    f.write(summary_stats.to_markdown() + "\n\n")
    f.write(f"## Mean Total Medals: \n{mean_total}\n")
    f.write(f"## Median Total Medals: \n{median_total}\n")
    f.write(f"## Standard Deviation of Total Medals: \n{std_total}\n")
    f.write("## Data Visualization\n")
    f.write("![Total Medals by Country](total_medals_by_country.png)\n")

# Print summary statistics
print(summary_stats)
