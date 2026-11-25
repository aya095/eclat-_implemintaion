
def getL1(itemsets, min_support):
    L1 = {}
    for item in itemsets:
        if item.support >= min_support:
            L1[frozenset({item.name})] = set(item.transactions)
    return L1


def generate_next_level(prev_level, min_support):
    items = list(prev_level.keys())   
    k = len(items[0]) + 1            
    next_level = {}
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a = items[i]
            b = items[j]
            new_set = a | b
            if len(new_set) != k:
               continue
            new_tids = prev_level[a] & prev_level[b]
            if len(new_tids) >= min_support:
               next_level[new_set] = new_tids

    return next_level
def eclat(items, min_support):
    all_levels = []
    current = getL1(items, min_support)
    while current:
        all_levels.append(current)
        current = generate_next_level(current, min_support)

    return all_levels