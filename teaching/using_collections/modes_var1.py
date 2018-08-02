from collections import Counter

def modes(data):
    counted = Counter(data)
    ordered = counted.most_common()

    if not ordered:
        return []

    max_occ = ordered[0]
    min_occ = ordered[-1]

    if max_occ == min_occ:
        return []

    return sorted([k for k,v in counted.items() if v == max_occ])
