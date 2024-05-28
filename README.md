# Online Retail Data Analysis

This repository contains the code and instructions for analyzing and visualizing an online retail dataset, and mining association rules using the Apriori algorithm.

## Table of Contents

- [Project Overview](#project-overview)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Activity 1: Visualizing Online Retail Data](#activity-1-visualizing-online-retail-data)
- [Activity 2: Mining Association Rules from Online Retail Data](#activity-2-mining-association-rules-from-online-retail-data)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The project consists of two main activities:
1. **Visualizing Online Retail Data**: Perform exploratory data analysis (EDA) on the dataset to gain insights and create visualizations.
2. **Mining Association Rules**: Apply the Apriori algorithm to find frequent itemsets and mine association rules from the dataset.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

Make sure you have Python installed. You can install the necessary packages using `pip` and the provided `requirements.txt`.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/online-retail-analysis.git
    cd online-retail-analysis

2. Install the required packages:
    ```bash
    pip install -r requirements.txt

3. Ensure you have the dataset (`OnlineRetail.xlsx`) in the project directory.

## Requirements

The required Python packages are listed in the `requirements.txt` file:

- jupyterlab==4.0.8
- mlxtend==0.23.0
- openpyxl==3.1.2
- pandas==2.1.3
- seaborn==0.13.0

Install them using:
```bash
pip install -r requirements.txt
```

## Activity 1: Visualizing Online Retail Data
### Description
In this activity, we perform exploratory data analysis on the online retail dataset to understand its structure, clean the data, and create visualizations.

### Steps
- Load the dataset:
- Display initial data:
- Describe the dataset:
- Clean the dataset:
- Extract and group data:
- Visualize top 5 selling countries:
- Visualize top 20 selling products:
- Visualize gross revenue by month and year:
- Save UK transactions pickle: UK.pkl

## Activity 2: Mining Association Rules from Online Retail Data
### Description
In this activity, we use the Apriori algorithm to find frequent itemsets and mine association rules from the UK transactions in the dataset.

### Steps
- Load UK transactions:
- Convert data for Apriori algorithm:
- Apply Apriori algorithm:
- Analyze frequent itemsets:
- Extract most frequent itemsets:
- Generate association rules:
- Visualize support vs confidence:
- Visualize support vs lift:

### Contributing
Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

### License
Distributed under the MIT License. See LICENSE for more information.


