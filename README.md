# ECLAT Algorithm for Frequent Itemset Mining and Association Rule Generation

## Project Overview

This project implements the **ECLAT (Equivalence Class Clustering and bottom-up Lattice Traversal)** algorithm for Frequent Itemset Mining and Association Rule Generation.

The system processes transaction data from an Excel file, converts it from Horizontal Format to Vertical Format, identifies frequent itemsets, generates association rules, and evaluates these rules using Confidence and Lift.

The project also allows users to experiment with different Minimum Support and Minimum Confidence thresholds.

## Project Objectives

- Read transaction data from Excel files.
- Convert Horizontal Transaction Format into Vertical Format.
- Generate frequent itemsets (L1, L2, ..., Lk) using ECLAT.
- Generate Association Rules from frequent itemsets.
- Calculate Support, Confidence, and Lift.
- Identify Strong Association Rules.
- Compare results using different Minimum Support and Minimum Confidence values.

## Technologies Used

- Python
- Pandas
- Excel (.xlsx)

## Project Structure

```text
ECLAT_Project/
│
├── data_preprocessing.py
├── eclat.py
├── association_rules.py
├── rule_evaluation.py
├── main.py
├── test_integration.py
├── dataset.xlsx
└── README.md
```

## Algorithm Workflow

1. **Data Preprocessing:** Read transactions and convert them into Vertical Format, where each item is associated with its transaction IDs.

2. **ECLAT Algorithm:** Generate frequent itemsets by intersecting transaction ID sets and checking the minimum support threshold.

3. **Association Rule Generation:** Generate possible association rules from frequent itemsets and calculate their Support and Confidence.

4. **Rule Evaluation:** Calculate Lift and identify Strong Rules based on the minimum confidence threshold.

5. **Integration and Experiments:** Connect all project modules, display results, and compare different support and confidence thresholds.

## Input Dataset Format

The input Excel file should contain at least two columns:


- `TID`: Unique transaction identifier.
- `Items`: Comma-separated items in each transaction.

## Installation

Install the required dependencies:

```bash
pip install pandas openpyxl
```


##OUTPUTS

The program displays:
- Frequent Itemsets.
- Association Rules.
- Strong Rules.
- Support, Confidence, and Lift values.
- Summary statistics.
- Support and Confidence experiment results.


## Evaluation Metrics

**Support**

The proportion of transactions containing an itemset.

**Confidence**

The probability of finding the consequent in transactions that contain the antecedent.

**Lift**

Measures the association between the antecedent and consequent.

- Lift > 1: Positive association.
- Lift = 1: No association beyond independence.
- Lift < 1: Negative association.

## Team Members

- Member 1: Data Preprocessing
- Member 2: ECLAT Algorithm Implementation
- Member 3: Association Rule Generation
- Member 4: Rule Evaluation (Lift and Strong Rules)
- Member 5: Integration, User Input, Output, and Testing

## Conclusion

This project demonstrates the implementation of the ECLAT algorithm and its application to frequent itemset mining and association rule discovery. It also explores how different Minimum Support and Minimum Confidence thresholds affect the generated results.
