import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Set random seed for reproducibility
np.random.seed(42)

# Function to round to 2 significant figures
def round_to_2_sig_figs(x):
    return float('{:.2g}'.format(x))

# Define the file paths
input_file = 'draft2.csv'
output_file = 'transformed_data.csv'

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

# Plot original satisfaction score distribution
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.hist(df['Employee_Satisfaction_Score'], bins=20, alpha=0.7)
plt.title('Original Satisfaction Score Distribution')
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')

# Generate new satisfaction scores based on support for 4-day work week
def generate_supporter_score():
    # For supporters: Range 3.7-5.0, normal distribution focused on 4.2-4.8
    raw_score = np.clip(np.random.normal(4.5, 0.3), 3.7, 5.0)
    return round_to_2_sig_figs(raw_score)

def generate_non_supporter_score():
    # For non-supporters: Range 2.5-4.0, normal distribution weighted to lower end
    raw_score = np.clip(np.random.normal(3.0, 0.4), 2.5, 4.0)
    return round_to_2_sig_figs(raw_score)

# Create a new column for transformed satisfaction scores
df['New_Satisfaction_Score'] = df.apply(
    lambda row: generate_supporter_score() if row['Supporter 4 days a week'] == True 
    else generate_non_supporter_score(), axis=1
)

# Plot new satisfaction score distribution
plt.subplot(1, 2, 2)
plt.hist(df['New_Satisfaction_Score'], bins=20, alpha=0.7)
plt.title('New Satisfaction Score Distribution (2 Sig Figs)')
plt.xlabel('Satisfaction Score')
plt.ylabel('Frequency')
plt.tight_layout()

# Save the figure if output directory exists
if not os.path.exists('output'):
    os.makedirs('output')
plt.savefig('output/satisfaction_distribution.png')
print("\nSaved distribution plot to 'output/satisfaction_distribution.png'")

# Calculate statistics of new satisfaction scores
print("\nNew satisfaction score statistics (rounded to 2 significant figures):")
print(df['New_Satisfaction_Score'].describe())

# Update the original satisfaction scores with the new ones
df['Employee_Satisfaction_Score'] = df['New_Satisfaction_Score']

# Drop the temporary column
df = df.drop('New_Satisfaction_Score', axis=1)

# Save the transformed data
df.to_csv(output_file, index=False)
print(f"\nTransformed data saved to '{output_file}'")

# Additional statistics by supporter status
supporters = df[df['Supporter 4 days a week'] == True]
non_supporters = df[df['Supporter 4 days a week'] == False]

print("\nSatisfaction scores for supporters (2 significant figures):")
print(supporters['Employee_Satisfaction_Score'].describe())

print("\nSatisfaction scores for non-supporters (2 significant figures):")
print(non_supporters['Employee_Satisfaction_Score'].describe()) 