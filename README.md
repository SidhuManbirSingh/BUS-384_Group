# Understanding the Employee Data Analysis

This document explains what the computer programs (scripts) do and what the results mean, in simple terms, without needing any technical background. It's important to note that alongside these automated steps, some manual work was also involved in preparing and reviewing the data.

## What are these scripts doing?

We have three main computer programs (we call them "scripts"):

1.  **Script 1: Creating Biased Data (`script1.py`)**
    * **What it does:** This script takes an initial file called `draft2.csv` (think of it as a spreadsheet of employee information). It then *intentionally* changes some of the employee satisfaction and performance scores. It makes it so that employees who support a 4-day work week tend to have slightly higher satisfaction and performance scores in the new data. This is called "adding bias".
    * **Why it's important:** This script helps us see what the data might look like if there's a tendency for people who like the 4-day work week to also feel more satisfied or be rated higher in performance. It's like creating a "what if" scenario.
    * **What it produces:**
        * A new file called `biased_data.csv` which contains the original employee information but with the adjusted satisfaction and performance scores.
        * Several image files (like pictures) in a folder called `output`. These images show graphs of the original and the new, biased satisfaction and performance scores, making it easier to see the differences. One of the images, `comprehensive_bias_analysis.png`, shows a more detailed comparison.

2.  **Script 2: Transforming Data (`script2.py`)**
    * **What it does:** This script also starts with the `draft2.csv` file. However, instead of just adding bias, it focuses on creating *new* satisfaction scores based on whether an employee supports a 4-day work week or not. It uses a bit of randomness but generally gives slightly higher satisfaction scores to supporters and slightly lower scores to non-supporters.
    * **Why it's important:** This helps us see a potential link between support for the 4-day work week and how employees might rate their own satisfaction.
    * **What it produces:**
        * A new file called `transformed_data.csv` with the original information but with the newly generated satisfaction scores.
        * An image file in the `output` folder called `satisfaction_distribution.png`. This image shows a graph comparing how the satisfaction scores were distributed originally and how they are distributed after the transformation.

3.  **Script 3: Visualizing Transformed Data (`script3.py`)**
    * **What it does:** This script takes the `transformed_data.csv` file (created by Script 2) and creates various charts and graphs to help us understand the data better. It looks at things like:
        * How satisfaction scores relate to age.
        * How satisfaction scores relate to how long someone has worked at the company.
        * The average satisfaction scores for different job titles.
        * How satisfaction scores relate to performance scores.
        * The overall distribution of satisfaction scores for supporters and non-supporters of the 4-day work week.
        * Whether satisfaction scores are linked to other factors like salary or work hours.
        * If there's a difference in satisfaction scores between genders based on their support for the 4-day work week.
    * **Why it's important:** This script helps us find patterns and relationships in the data through visual representations, making it easier to draw conclusions.
    * **What it produces:** Several image files in the `output` folder (like `satisfaction_scatter_plots.png`, `satisfaction_distribution_by_support.png`, etc.). Each image shows a different aspect of the data in a graphical format.

## Manual Work Involved

It's important to understand that the process wasn't fully automatic. Before running these scripts, there was some manual work involved, such as:

* **Reviewing the initial data:** Someone looked at the raw `draft2.csv` file to understand the information it contained and ensure it was in a usable format.
* **Potentially cleaning the data:** This might have involved fixing any errors, inconsistencies, or missing information in the original data file by hand.
* **Deciding on the analysis:** The types of comparisons and visualizations that the scripts were designed to create were likely decided upon through careful thought and planning by someone.

## Where to Find the Results

After running these scripts, you will find a new folder called `output` in the same place where the scripts are saved. This folder will contain all the image files (the graphs and charts) created by the scripts. You will also find the new data files: `biased_data.csv` (from Script 1) and `transformed_data.csv` (from Script 2) in the same location as the scripts.

**Important Note:** The `output` directory might contain some image files that were generated during the process but were not ultimately needed for the final analysis. These can be considered unused graphics and can be disregarded.

Additionally, you will find a folder named `DUMP`. This folder contains extra files that were used or considered during the analysis process. These files might include initial drafts, alternative data manipulations, or other resources that supported the work done by the scripts. You don't necessarily need to look at these files to understand the main results, but they are there for transparency and if a more detailed understanding of the process is required.

## Looking at the Results (Without Being Technical)

To understand the results, you just need to open the image files in the `output` folder. Each image has a title that explains what it shows. For example:

* An image titled "Original Satisfaction Score Distribution" shows how happy employees were in the original data.
* An image titled "New Biased Satisfaction Score Distribution" (from Script 1) shows how the satisfaction scores look after the program intentionally made supporters seem slightly happier.
* An image titled "Satisfaction Score vs Age" (from Script 3) will show if there's any visual trend between an employee's age and their satisfaction level.

By looking at these graphs, you can get a visual sense of any potential relationships or differences in the data. You don't need to understand the code to interpret the pictures!

The `.csv` files (`biased_data.csv` and `transformed_data.csv`) are like spreadsheets. If you open them, you'll see the raw data, but the images are usually easier to understand for getting an overview.

In summary, these scripts help us explore employee data related to a 4-day work week by creating modified data and then visualizing it in different ways. Remember that this automated process was supported by some initial manual work. The key findings can be understood by simply looking at the relevant charts and graphs produced in the `output` folder, keeping in mind that some unused graphics might also be present there. The `DUMP` folder contains additional files that provide context to the overall analysis. 

Will be uploading the more modified scripts for better visual. (Actually used in the Project) Delay is caused because I am in different computer and my main work is not backed in the cloud. 