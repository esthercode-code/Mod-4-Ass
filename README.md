README.md

# 🎬 Netflix Data Visualization Assignment

This repository/zipped file contains the Python and R code used to analyze the provided Netflix dataset, fulfilling the requirements of the assignment.

## ⚙️ Prerequisites

To run the code, you need to have the following installed:

1.  **Python 3.x**
    * Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`
2.  **R**
    * Libraries: `tidyverse` (includes `readr` and `ggplot2`)

You can install the Python dependencies using pip:
```bash
pip install pandas numpy matplotlib seaborn
You can install the R dependencies within the R console:
install.packages("tidyverse")


File Structure
netflix_shows_movies.py: Contains the Python code for Data Preparation, Cleaning, Exploration, and Visualization.

netflix_shows_movies.R: Contains the R code for integrating the Ratings Distribution chart.

README.md: This instruction file.

Original data file: Netflix_shows_movies.csv).

Execution Instructions
1. Python Code
Place the Dataset: Ensure your unzipped dataset is accessible. Update the file path in netflix_shows_movies.py if necessary.

Note: The code assumes the file is named Netflix_shows_movies.csv.

Run the script:

Bash

python netflix_shows_movies.py
The script will print data exploration results to the console and display the Genre and Ratings visualizations. It will also export a cleaned CSV file (cleaned_netflix_data.csv) for the R integration.

2. R Code
Prerequisite: The Python script must be run first to generate the cleaned_netflix_data.csv file.

Open R/RStudio or run the script from the command line:

Bash

Rscript netflix_shows_movies.R
The script will load the cleaned data and generate the Ratings Distribution bar chart using ggplot2.