
def build_support_dict(all_levels, total_transactions):

    support_dict = {}

    for level in all_levels:
        for itemset, tids in level.items():

            support_dict[frozenset(itemset)] = (
                len(tids) / total_transactions
            )

    return support_dict


def generate_combinations(items, r):

    result = []

    def generate(start, current):

        if len(current) == r:
            result.append(tuple(current))
            return

        for i in range(start, len(items)):

            current.append(items[i])

            generate(i + 1, current)

            current.pop()

    generate(0, [])

    return result


def generate_association_rules(all_levels, total_transactions):

    support_dict = build_support_dict(
        all_levels, total_transactions
    )

    rules = []

    for level in all_levels[1:]:

        for itemset in level.keys():

            itemset_key = frozenset(itemset)

            item_support = support_dict.get(itemset_key, 0.0)

            items = list(itemset_key)

            for r in range(1, len(items)):

                combinations_list = generate_combinations(items, r)

                for ant_tuple in combinations_list:

                    antecedent = frozenset(ant_tuple)

                    consequent = itemset_key - antecedent

                    ant_support = support_dict.get(
                        antecedent, 0.0
                    )

                    cons_support = support_dict.get(
                        consequent, 0.0
                    )

                    if ant_support == 0 or cons_support == 0:
                        continue

                    confidence = item_support / ant_support

                    rules.append({
                        "antecedent": set(antecedent),
                        "consequent": set(consequent),
                        "support": item_support,
                        "confidence": confidence,
                        "antecedent_support": ant_support,
                        "consequent_support": cons_support
                    })

    return rules
