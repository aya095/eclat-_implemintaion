
import pandas as pd
import math

from data_preprocessing import data_process
from eclat import eclat
from Association_rules import generate_association_rules
from rule_evaluation import evaluate_rules, summarize_results


# ==============================
# Helper Functions
# ==============================

def format_itemset(itemset):
    items = sorted(str(item) for item in itemset)
    return "{" + ", ".join(items) + "}"



def display_rules(title, rules):
    print(f"\n========== {title} ==========")

    if not rules:
        print("No rules found.")
        return

    print(
        f"{'Rule':<28}"
        f"{'Support':<13}"
        f"{'Confidence':<15}"
        f"{'Lift':<12}"
        f"{'Rule Status':<15}"
    )

    for rule in rules:

        rule_name = (
            format_itemset(rule["antecedent"])
            + " -> "
            + format_itemset(rule["consequent"])
        )

        status = "Strong" if rule["is_strong"] else "Not Strong"

        print(
            f"{rule_name:<28}"
            f"{rule['support']:<13.4f}"
            f"{rule['confidence']:<15.4f}"
            f"{rule['lift']:<12.4f}"
            f"{status:<15}"
        )

# ==============================
# 1. Read Dataset
# ==============================

data = pd.read_excel("Horizontal_Format.xlsx")

if len(data.columns) != 2:
    raise ValueError(
        "Excel file must contain exactly two columns: "
        "Transaction ID and Items."
    )

if data.empty:
    raise ValueError("The dataset contains no transactions.")

data.columns = ["TID", "Items"]

if data["TID"].isna().any():
    raise ValueError("Transaction IDs cannot be empty.")

if data["Items"].isna().any():
    raise ValueError("Items cannot be empty.")

if data["TID"].duplicated().any():
    raise ValueError("Transaction IDs must be unique.")

data["Items"] = data["Items"].astype(str)

if data["Items"].str.strip().eq("").any():
    raise ValueError("Every transaction must contain at least one item.")

transactions_number = len(data)


# ==============================
# 2. Read Minimum Thresholds
# ==============================

min_support = float(input("Enter Minimum Support (%): "))
min_confidence = float(input("Enter Minimum Confidence (%): "))

if min_support <= 0 or min_support > 100:
    raise ValueError("Minimum Support must be greater than 0 and at most 100.")

if min_confidence < 0 or min_confidence > 100:
    raise ValueError("Minimum Confidence must be between 0 and 100.")

min_support_count = math.ceil(
    (min_support / 100) * transactions_number
)

min_confidence_ratio = min_confidence / 100

print("\n========== DATASET INFORMATION ==========")
print("Number of Transactions:", transactions_number)
print("Minimum Support:", min_support, "%")
print("Minimum Support Count:", min_support_count)
print("Minimum Confidence:", min_confidence, "%")


# ==============================
# 3. Data Preprocessing
# ==============================

items = data_process(data)


# ==============================
# 4. ECLAT - Frequent Itemsets
# ==============================

all_levels = eclat(items, min_support_count)

print("\n========== FREQUENT ITEMSETS ==========")

print(
    f"{'Level':<12}"
    f"{'Itemset':<30}"
    f"{'Support Count':<15}"
)

frequent_itemsets_count = 0

for idx, level in enumerate(all_levels, start=1):

    for itemset, tids in level.items():

        print(
            f"{'L' + str(idx):<12}"
            f"{format_itemset(itemset):<30}"
            f"{len(tids):<15}"
        )

        frequent_itemsets_count += 1

if frequent_itemsets_count == 0:
    print("No frequent itemsets found.")

print("\nTotal Frequent Itemsets:", frequent_itemsets_count)


# ==============================
# 5. Generate Association Rules
# ==============================

rules = generate_association_rules(
    all_levels,
    transactions_number
)


# ==============================
# 6. Evaluate Rules
# ==============================

evaluated_rules, strong_rules = evaluate_rules(
    rules,
    min_confidence_ratio
)


# ==============================
# 7. Display All Association Rules
# ==============================

display_rules("ALL ASSOCIATION RULES", evaluated_rules)


# ==============================
# 8. Display Strong Association Rules
# ==============================

display_rules("STRONG ASSOCIATION RULES", strong_rules)


# ==============================
# 9. Summary
# ==============================

summary = summarize_results(
    all_levels,
    evaluated_rules,
    strong_rules
)

print("\n========== SUMMARY ==========")

print("Total Frequent Itemsets:",
      summary["frequent_itemsets_count"])

print("Total Association Rules:",
      summary["association_rules_count"])

print("Total Strong Rules:",
      summary["strong_rules_count"])


# ==============================
# 10. Minimum Support Experiments
# ==============================

support_values = [20, 40, 60, 80]

if min_support not in support_values:
    support_values.append(min_support)

support_values.sort()

print("\n========== MINIMUM SUPPORT EXPERIMENTS ==========")

print(
    f"{'Min Support':<18}"
    f"{'Frequent Itemsets':<22}"
    f"{'Association Rules':<20}"
    f"{'Strong Rules':<15}"
)

for support_percent in support_values:

    support_count = math.ceil(
        (support_percent / 100) * transactions_number
    )

    experiment_levels = eclat(items, support_count)

    experiment_rules = generate_association_rules(
        experiment_levels,
        transactions_number
    )

    experiment_evaluated, experiment_strong = evaluate_rules(
        experiment_rules,
        min_confidence_ratio
    )

    itemsets_count = sum(
        len(level) for level in experiment_levels
    )

    print(
        f"{str(support_percent) + '%':<18}"
        f"{itemsets_count:<22}"
        f"{len(experiment_evaluated):<20}"
        f"{len(experiment_strong):<15}"
    )


# ==============================
# 11. Minimum Confidence Experiments
# ==============================

confidence_values = [50, 70, 90]

if min_confidence not in confidence_values:
    confidence_values.append(min_confidence)

confidence_values.sort()

print("\n========== MINIMUM CONFIDENCE EXPERIMENTS ==========")

print(
    f"{'Min Confidence':<20}"
    f"{'Total Rules':<18}"
    f"{'Strong Rules':<15}"
)

for confidence_percent in confidence_values:

    confidence_ratio = confidence_percent / 100

    _, experiment_strong = evaluate_rules(
        rules,
        confidence_ratio
    )

    print(
        f"{str(confidence_percent) + '%':<20}"
        f"{len(rules):<18}"
        f"{len(experiment_strong):<15}"
    )
