import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for better visualizations
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette('viridis')

# Create output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Load the transformed data
print("Loading transformed data...")
df = pd.read_csv('transformed_data.csv')

# Basic information about the data
print(f"Data shape: {df.shape}")
print("\nSatisfaction score distribution by 4-day work week support:")
print(df.groupby('Supporter 4 days a week')['Employee_Satisfaction_Score'].describe())

# Create figure with multiple plots
plt.figure(figsize=(16, 12))

# 1. Scatter plot: Satisfaction Score vs Age, colored by support for 4-day work week
plt.subplot(2, 2, 1)
supporters = df[df['Supporter 4 days a week'] == True]
non_supporters = df[df['Supporter 4 days a week'] == False]

plt.scatter(supporters['Age'], supporters['Employee_Satisfaction_Score'], 
            alpha=0.4, label='Supporters', c='green')
plt.scatter(non_supporters['Age'], non_supporters['Employee_Satisfaction_Score'], 
            alpha=0.6, label='Non-Supporters', c='red')
plt.xlabel('Age')
plt.ylabel('Satisfaction Score')
plt.title('Satisfaction Score vs Age')
plt.legend()
plt.grid(True, alpha=0.3)

# 2. Scatter plot: Satisfaction Score vs Years at Company
plt.subplot(2, 2, 2)
plt.scatter(df['Years_At_Company'], df['Employee_Satisfaction_Score'], 
            alpha=0.5, c=df['Supporter 4 days a week'].map({True: 'green', False: 'red'}))
plt.xlabel('Years at Company')
plt.ylabel('Satisfaction Score')
plt.title('Satisfaction Score vs Years at Company')
plt.grid(True, alpha=0.3)

# 3. Box plot of satisfaction scores by job title
plt.subplot(2, 2, 3)
job_satisfaction = df.groupby('Job_Title')['Employee_Satisfaction_Score'].agg(['mean', 'count']).sort_values('mean')
job_data = df[df['Job_Title'].isin(job_satisfaction.index[-6:])]  # Top 6 job titles by mean satisfaction
sns.boxplot(x='Job_Title', y='Employee_Satisfaction_Score', data=job_data, hue='Supporter 4 days a week')
plt.xticks(rotation=45, ha='right')
plt.title('Satisfaction Scores by Job Title')
plt.legend(title='4-day Week Supporter')

# 4. Scatter plot: Satisfaction Score vs Performance Score
plt.subplot(2, 2, 4)
for i in range(1, 6):  # Assuming Performance_Score is 1-5
    subset = df[df['Performance_Score'] == i]
    plt.scatter(subset['Performance_Score'] + np.random.normal(0, 0.1, size=len(subset)), 
                subset['Employee_Satisfaction_Score'], 
                alpha=0.4, label=f'Score {i}')
plt.xlabel('Performance Score (jittered)')
plt.ylabel('Satisfaction Score')
plt.title('Satisfaction Score vs Performance Score')
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.savefig('output/satisfaction_scatter_plots.png', dpi=300)
print("Saved scatter plots to 'output/satisfaction_scatter_plots.png'")

# Create a plot showing the distribution of satisfaction scores
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Employee_Satisfaction_Score', hue='Supporter 4 days a week', 
             element='step', stat='density', kde=True, common_norm=False)
plt.title('Distribution of Satisfaction Scores by 4-day Work Week Support')
plt.xlabel('Satisfaction Score')
plt.ylabel('Density')
plt.savefig('output/satisfaction_distribution_by_support.png', dpi=300)
print("Saved distribution plot to 'output/satisfaction_distribution_by_support.png'")

# Create heatmap showing correlation of satisfaction scores with other numeric variables
plt.figure(figsize=(12, 10))
numeric_cols = ['Age', 'Years_At_Company', 'Performance_Score', 'Monthly_Salary', 
                'Work_Hours_Per_Week', 'Sick_Days', 'Employee_Satisfaction_Score']
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Between Satisfaction Score and Other Variables')
plt.tight_layout()
plt.savefig('output/satisfaction_correlation_heatmap.png', dpi=300)
print("Saved correlation heatmap to 'output/satisfaction_correlation_heatmap.png'")

# Create a plot showing satisfaction score by gender and support status
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Employee_Satisfaction_Score', hue='Supporter 4 days a week', data=df)
plt.title('Satisfaction Score by Gender and 4-day Work Week Support')
plt.savefig('output/satisfaction_by_gender.png', dpi=300)
print("Saved gender comparison plot to 'output/satisfaction_by_gender.png'")

print("All visualizations complete!") 