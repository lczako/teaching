from collections import Counter

# unwasteful

def modes(data):
    counted = Counter(data)
    ordered = counted.most_common()

    max_occ = ordered[0]
    min_occ = ordered[-1]

    res = []
    if max_occ == min_occ:
        return res

    for k,v in ordered:
        if v == max_occ:
            res.append(k)
        else:
            break

    return sorted(res)
