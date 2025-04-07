import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set random seed for reproducibility
np.random.seed(42)

# Function to round to 2 significant figures
def round_to_2_sig_figs(x):
    return float('{:.2g}'.format(x))

# Define the file paths
input_file = 'draft2.csv'
output_file = 'biased_data.csv'

# Create output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Read the CSV file
print(f"Reading file: {input_file}")
df = pd.read_csv(input_file)

# Display basic information about the data
print(f"Original data shape: {df.shape}")
print("\nSample of original data:")
print(df.head())

# Check the distribution of supporters and non-supporters
supporter_counts = df['Supporter 4 days a week'].value_counts()
print("\nDistribution of 4-day work week supporters:")
print(supporter_counts)

# Calculate statistics of original satisfaction scores
print("\nOriginal satisfaction score statistics:")
print(df['Employee_Satisfaction_Score'].describe())
print("\nOriginal performance score statistics:")
print(df['Performance_Score'].describe())

# Analyze satisfaction by support status
print("\nOriginal satisfaction by support status:")
print(df.groupby('Supporter 4 days a week')['Employee_Satisfaction_Score'].describe())
print("\nOriginal performance by support status:")
print(df.groupby('Supporter 4 days a week')['Performance_Score'].describe())

# Plot original distributions
plt.figure(figsize=(16, 8))

# Satisfaction score plot
plt.subplot(1, 2, 1)
sns.histplot(data=df, x='Employee_Satisfaction_Score', hue='Supporter 4 days a week', 
             element='step', stat='density', kde=True, common_norm=False)
plt.title('Original Satisfaction Score Distribution')
plt.xlabel('Satisfaction Score')
plt.ylabel('Density')

# Performance score plot
plt.subplot(1, 2, 2)
sns.countplot(data=df, x='Performance_Score', hue='Supporter 4 days a week')
plt.title('Original Performance Score Distribution')
plt.xlabel('Performance Score')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('output/original_distributions.png')

# Generate new satisfaction scores based on support for 4-day work week
# INCREASING BIAS BY 20%
def generate_supporter_score():
    # For supporters: Range 3.7-5.0, normal distribution focused on 4.2-4.8
    # Increase bias by moving mean from 4.5 to 4.7 (20% closer to max of 5.0)
    raw_score = np.clip(np.random.normal(4.7, 0.25), 3.8, 5.0)
    return round_to_2_sig_figs(raw_score)

def generate_non_supporter_score():
    # For non-supporters: Range 2.5-4.0, normal distribution weighted to lower end
    # Increase bias by moving mean from 3.0 to 2.8 (20% closer to min of 2.5)
    raw_score = np.clip(np.random.normal(2.8, 0.35), 2.5, 3.9)
    return round_to_2_sig_figs(raw_score)

# Add bias to performance scores for supporters
def bias_performance_score(row):
    current_score = row['Performance_Score']
    is_supporter = row['Supporter 4 days a week']
    
    if is_supporter:
        # 50% chance of increasing performance score for supporters (if not already at max)
        if current_score < 5 and np.random.random() < 0.5:
            return current_score + 1
        return current_score
    else:
        # 20% chance of decreasing performance score for non-supporters (if not already at min)
        if current_score > 1 and np.random.random() < 0.2:
            return current_score - 1
        return current_score

# Create a new column for transformed satisfaction scores
df['New_Satisfaction_Score'] = df.apply(
    lambda row: generate_supporter_score() if row['Supporter 4 days a week'] == True 
    else generate_non_supporter_score(), axis=1
)

# Create a new column for biased performance scores
df['New_Performance_Score'] = df.apply(bias_performance_score, axis=1)

# Plot new distributions
plt.figure(figsize=(16, 8))

# Satisfaction score plot
plt.subplot(1, 2, 1)
sns.histplot(data=df, x='New_Satisfaction_Score', hue='Supporter 4 days a week', 
             element='step', stat='density', kde=True, common_norm=False)
plt.title('New Biased Satisfaction Score Distribution')
plt.xlabel('Satisfaction Score')
plt.ylabel('Density')

# Performance score plot
plt.subplot(1, 2, 2)
sns.countplot(data=df, x='New_Performance_Score', hue='Supporter 4 days a week')
plt.title('New Biased Performance Score Distribution')
plt.xlabel('Performance Score')
plt.ylabel('Count')

plt.tight_layout()
plt.savefig('output/biased_distributions.png')
print("\nSaved distribution plots to 'output/biased_distributions.png'")

# Calculate statistics of new satisfaction scores
print("\nNew biased satisfaction score statistics:")
print(df['New_Satisfaction_Score'].describe())
print("\nNew biased performance score statistics:")
print(df['New_Performance_Score'].describe())

# Analyze new scores by support status
print("\nNew satisfaction by support status:")
print(df.groupby('Supporter 4 days a week')['New_Satisfaction_Score'].describe())
print("\nNew performance by support status:")
print(df.groupby('Supporter 4 days a week')['New_Performance_Score'].describe())

# Update the original scores with the new ones
df['Employee_Satisfaction_Score'] = df['New_Satisfaction_Score']
df['Performance_Score'] = df['New_Performance_Score']

# Drop the temporary columns
df = df.drop(['New_Satisfaction_Score', 'New_Performance_Score'], axis=1)

# Save the transformed data
df.to_csv(output_file, index=False)
print(f"\nTransformed data with added bias saved to '{output_file}'")

# Create a comprehensive comparison plot
plt.figure(figsize=(15, 10))

# Define color palette
palette = {'Supporters': 'green', 'Non-Supporters': 'red'}

# Create a scatter plot comparing Satisfaction Score vs Performance Score
plt.subplot(2, 2, 1)
for support, label in [(True, 'Supporters'), (False, 'Non-Supporters')]:
    group = df[df['Supporter 4 days a week'] == support]
    # Add jitter to performance score for better visualization
    jittered_scores = group['Performance_Score'] + np.random.normal(0, 0.1, size=len(group))
    plt.scatter(jittered_scores, group['Employee_Satisfaction_Score'], 
                alpha=0.5, label=label, color=palette[label])
plt.xlabel('Performance Score (jittered)')
plt.ylabel('Satisfaction Score')
plt.title('Satisfaction Score vs Performance Score')
plt.legend()
plt.grid(True, alpha=0.3)

# Create a box plot of satisfaction scores by performance score and support status
plt.subplot(2, 2, 2)
performance_levels = df['Performance_Score'].unique()
box_data = []
for level in sorted(performance_levels):
    supporters_data = df[(df['Performance_Score'] == level) & (df['Supporter 4 days a week'] == True)]['Employee_Satisfaction_Score']
    non_supporters_data = df[(df['Performance_Score'] == level) & (df['Supporter 4 days a week'] == False)]['Employee_Satisfaction_Score']
    
    for score in supporters_data:
        box_data.append({'Performance': str(level), 'Satisfaction': score, 'Group': 'Supporters'})
    for score in non_supporters_data:
        box_data.append({'Performance': str(level), 'Satisfaction': score, 'Group': 'Non-Supporters'})

box_df = pd.DataFrame(box_data)
sns.boxplot(x='Performance', y='Satisfaction', hue='Group', data=box_df, palette=palette)
plt.title('Satisfaction Distribution by Performance Level')
plt.xlabel('Performance Score')
plt.ylabel('Satisfaction Score')

# Create a bar chart of average performance by job title and support status
plt.subplot(2, 2, 3)
job_perf = df.groupby(['Job_Title', 'Supporter 4 days a week'])['Performance_Score'].mean().reset_index()
job_perf['Support_Label'] = job_perf['Supporter 4 days a week'].map({True: 'Supporters', False: 'Non-Supporters'})
top_jobs = df['Job_Title'].value_counts().nlargest(6).index
job_perf_filtered = job_perf[job_perf['Job_Title'].isin(top_jobs)]

sns.barplot(x='Job_Title', y='Performance_Score', hue='Support_Label', data=job_perf_filtered, palette=palette)
plt.title('Average Performance Score by Job Title')
plt.xticks(rotation=45, ha='right')
plt.legend(title='')

# Create a bar chart of average satisfaction by education level and support status
plt.subplot(2, 2, 4)
edu_sat = df.groupby(['Education_Level', 'Supporter 4 days a week'])['Employee_Satisfaction_Score'].mean().reset_index()
edu_sat['Support_Label'] = edu_sat['Supporter 4 days a week'].map({True: 'Supporters', False: 'Non-Supporters'})

sns.barplot(x='Education_Level', y='Employee_Satisfaction_Score', hue='Support_Label', data=edu_sat, palette=palette)
plt.title('Average Satisfaction Score by Education Level')
plt.xticks(rotation=45, ha='right')
plt.legend(title='')

plt.tight_layout()
plt.savefig('output/comprehensive_bias_analysis.png', dpi=300)
print("Saved comprehensive analysis to 'output/comprehensive_bias_analysis.png'")

print("All transformations and visualizations complete!") 