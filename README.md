# Python Job Scraping and Analysis

## Overview

This project involves web scraping job listings from `work.ua` to analyze Python job market trends. The project uses Scrapy for scraping, Pandas for data analysis, and visualization tools like Matplotlib for generating insights.

## Features

- **Data Scraping**: Extract job listings from `work.ua` using Scrapy.
- **Data Cleaning**: Process and clean the data, handling missing values and formatting issues.
- **Salary Analysis**: Calculate and visualize average salaries, highlighting top companies and job titles.
- **Technology Analysis**: Identify the most common technologies required for Python jobs and their correlation with salary.
- **Visualization**: Generate graphs and charts to represent data insights effectively.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    ```

2. Navigate to the project directory:
    ```bash
    cd yourproject
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Scrapy Spider**:
    Navigate to the Scrapy project directory and run:
    ```bash
    scrapy crawl works -o works_info.json
    ```

2. **Analyze the Data**:
    Open a Jupyter notebook and execute the analysis code.

## Contributing

Feel free to fork the repository and submit pull requests. Ensure your changes adhere to the project's coding standards and include relevant tests.

## Acknowledgments

- [Scrapy](https://scrapy.org/) - The web scraping framework used.
- [Pandas](https://pandas.pydata.org/) - Data analysis library.
- [Matplotlib](https://matplotlib.org/) - Visualization library.
