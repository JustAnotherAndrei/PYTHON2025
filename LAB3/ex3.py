def set_operations(*sets):
    result = {}
    for i, a in enumerate(sets):
        for b in sets[i + 1:]:
            # facem string din seturi
            a_str = str(a)
            b_str = str(b)

            result[f"{a_str} | {b_str}"] = a | b
            result[f"{a_str} & {b_str}"] = a & b
            result[f"{a_str} - {b_str}"] = a - b
            result[f"{b_str} - {a_str}"] = b - a

    return result

s1 = {1, 2}
s2 = {2, 3}
s3 = {3, 4}

print(set_operations(s1, s2, s3))