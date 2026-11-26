# ECLAT Algorithm Implementation

## Overview

This project implements the **ECLAT (Equivalence Class Clustering and bottom-up Lattice Traversal)** algorithm for Frequent Itemset Mining and Association Rule Mining.

It processes transactional datasets, discovers frequent itemsets, generates association rules, and evaluates them using Support, Confidence, and Lift.

## Features

- Read transactional data from Excel files.
- Convert Horizontal Format into Vertical Format using TID Sets.
- Generate frequent itemsets using ECLAT.
- Generate association rules from frequent itemsets.
- Calculate Support, Confidence, and Lift.
- Classify rules as Strong or Not Strong.
- Experiment with different Minimum Support and Minimum Confidence values.

## Project Structure

 File | Description 
 `main.py` | Runs the complete workflow and displays results. 
 `data_preprocessing.py` | Reads and converts transactional data into Vertical Format. 
 `eclat.py` | Implements the ECLAT algorithm and generates frequent itemsets. 
 `association_rules.py` | Generates association rules and calculates Support and Confidence. 
`rule_evaluation.py` | Calculates Lift, classifies rules, and evaluates results. 

## Dataset Format

The input Excel file must contain two columns:

| TID | Items |
|---|---|
| T1 | A, B, C |
| T2 | A, C |
| T3 | B, C |

Each row represents one transaction. Transaction IDs must be unique, and items should be comma-separated.

## Installation

Requirements: Python 3, Pandas, and OpenPyXL.

Install dependencies:

```bash
pip install pandas openpyxl
```

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/aya095/eclat-_implemintaion.git
```

2. Navigate to the project folder:

```bash
cd eclat-_implemintaion
```

3. Place the Excel dataset in the project directory.

4. Run the program:

```bash
python main.py
```

5. Enter the desired Minimum Support and Minimum Confidence percentages.

## Evaluation

The project evaluates association rules using:

- **Support:** Measures how frequently an itemset occurs.
- **Confidence:** Measures the reliability of an association rule.
- **Lift:** Measures the strength of the relationship between the antecedent and consequent.

Rules are classified as **Strong** or **Not Strong** based on the Minimum Confidence threshold.

The program also runs experiments with different Minimum Support and Minimum Confidence values to analyze their impact on frequent itemsets and strong rules.

## Technologies Used

- Python
- Pandas
- OpenPyXL

