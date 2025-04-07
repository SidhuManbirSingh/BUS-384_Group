# Employee Satisfaction Score Transformation

This script transforms employee satisfaction scores based on whether employees support a 4-day work week.

## Requirements

- Python 3.8 or higher
- Required packages are listed in `requirements.txt`

## Installation

Install the required packages using:

```bash
pip install -r requirements.txt
```

## Usage

1. Ensure your input CSV file `draft2.csv` is in the same directory as the script
2. Run the script:

```bash
python transform_satisfaction.py
```

3. The script will:
   - Read the original CSV file
   - Transform satisfaction scores based on 4-day work week support
   - Round all satisfaction scores to 2 significant figures
   - Create visualizations of the original and new distributions
   - Save the transformed data to `transformed_data.csv`
   - Save distribution plots to the `output` directory

## Transformation Details

- For employees who support the 4-day work week:
  - Satisfaction scores range from 3.7 to 5.0
  - Normal distribution with most values between 4.2 to 4.8
  - Rounded to 2 significant figures (e.g., 4.5, 3.7, 4.0)

- For employees who don't support the 4-day work week:
  - Satisfaction scores range from 2.5 to 4.0
  - Normal distribution weighted toward the lower end
  - Rounded to 2 significant figures (e.g., 3.0, 2.5, 3.8)

## Output

- `transformed_data.csv`: CSV file with the updated satisfaction scores
- `output/satisfaction_distribution.png`: Visual comparison of original and new distributions 