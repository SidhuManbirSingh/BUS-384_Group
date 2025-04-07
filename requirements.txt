**requirements.txt - Understanding the Necessary Software**

This document lists the software packages that need to be installed on your computer for the provided scripts to run correctly. Think of these packages as extra tools that the scripts need to perform their tasks, like reading spreadsheets, doing calculations, and creating graphs.

Here's a breakdown of each package listed:

* **pandas:** Imagine a very powerful and easy-to-use tool for working with tables of data (like spreadsheets). The `pandas` package helps the scripts read, organize, and manipulate the employee data from the `.csv` files.

* **numpy:** This package provides the scripts with the ability to do mathematical operations efficiently, especially with numbers and arrays (think of lists of numbers). It's used for calculations like generating random scores and statistical analysis.

* **matplotlib:** This is a fundamental tool for creating basic charts and graphs. The scripts use `matplotlib` to draw things like histograms and scatter plots to visualize the data.

* **seaborn:** Think of `seaborn` as a more advanced and visually appealing extension of `matplotlib`. It helps create more sophisticated statistical graphics, like the distribution plots and heatmaps, making it easier to see patterns and relationships in the data.

**Why are these listed?**

These packages contain pre-written code and functions that the scripts rely on. Without them, the scripts wouldn't be able to perform tasks like reading the data files, doing the necessary calculations, or generating the visual results you see in the `output` folder.

**How to Install These Packages**

The following command is used to install all the packages listed in this `requirements.txt` file at once:

```bash
pip install -r requirements.txt
