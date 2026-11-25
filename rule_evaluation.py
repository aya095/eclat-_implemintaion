
def calculate_lift(rule):

    support = rule["support"]
    ant_support = rule["antecedent_support"]
    cons_support = rule["consequent_support"]

    if ant_support == 0 or cons_support == 0:
        return 0

    lift = support / (ant_support * cons_support)

    return lift


def get_strong_rules(rules, min_confidence):

    strong_rules = []

    for rule in rules:

        if rule["confidence"] >= min_confidence:
            strong_rules.append(rule)

    return strong_rules


def evaluate_rules(rules, min_confidence):

    evaluated_rules = []

    for rule in rules:

        rule["lift"] = calculate_lift(rule)

        if rule["confidence"] >= min_confidence:
            rule["is_strong"] = True
        else:
            rule["is_strong"] = False

        evaluated_rules.append(rule)

    strong_rules = get_strong_rules(
        evaluated_rules, min_confidence
    )

    return evaluated_rules, strong_rules


def summarize_results(all_levels, rules, strong_rules):

    frequent_itemsets_count = 0

    for level in all_levels:
        frequent_itemsets_count += len(level)

    return {
        "frequent_itemsets_count": frequent_itemsets_count,
        "association_rules_count": len(rules),
        "strong_rules_count": len(strong_rules)
    }


def run_confidence_experiments(rules, confidence_values):

    experiments = []

    for min_confidence in confidence_values:

        evaluated_rules, strong_rules = evaluate_rules(
            rules, min_confidence
        )

        result = {
            "min_confidence": min_confidence,
            "total_rules": len(evaluated_rules),
            "strong_rules_count": len(strong_rules),
            "strong_rules": strong_rules
        }

        experiments.append(result)

    return experiments
