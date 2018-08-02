# Solving problem without collections

def modes(data):
    counted = counter(data)
    max_occ = max(counted.values())
    min_occ = min(counted.values())

    if max_occ == min_occ:
        return []

    res = []
    for k, v in counted.items():
        if v == max_occ: res.append(k)
    return sorted(res)

def counter(data):
    counted = dict()
    for d in data:
        if d not in counted:
            counted[d] = 0
        counted[d] += 1
    return counted
