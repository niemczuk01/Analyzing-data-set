# Analyzing-data-set
# Pandas CSV Analysis Project

**Author:** Ryan Niemczuk  
**Course:** INST 326  
**Assignment:** Pandas Data Analysis HW 4

## Project Overview
This project demonstrates my understanding of pandas by analyzing a CSV dataset using indexing, filtering, column manipulation, and groupby operations. The dataset consists of elite competitive swimmers, their countries, the events they swam, and their race times converted into total seconds for easier analysis. The goal of the assignment was to practice reading data, inspecting DataFrames, selecting rows and columns, filtering with Boolean expressions, adding and dropping columns, and performing split-apply-combine operations.

## What the Script Does
The Python script `analyze_data.py` completes all required steps:

- Reads a CSV file into a pandas DataFrame  
- Displays:
  - The first five rows using `head()`
  - DataFrame structure using `info()`
  - Summary statistics with `describe()`
- Demonstrates indexing:
  - A row by label (`loc`)
  - A row by position (`iloc`)
  - Row slices by label and position  
  - Selecting a single column  
  - Selecting a single cell  
- Shows filtering:
  - One filter using a single Boolean comparison  
  - One filter combining multiple conditions with `&`
- Adds a new column and removes an old one  
- Performs a `groupby()` to compute the average race time by country  
- Prints all results clearly labeled  


## How to Run the Project

### 1. Install pandas

### **2. Run the Python script
