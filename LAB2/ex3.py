def prob_3() -> tuple[list, list]:
    input_rows = []
    print("Introdu valorile, cu spatii intre ele:")
    while True:
        line = input().strip()
        if not line:
            break
        values = [float(x) if '.' in x else int(x) for x in line.split()]
        input_rows.append(values)

    def union(list1: list, list2: list) -> list:
        return list(set(list1) | set(list2))

    def intersection(list1: list, list2: list) -> list:
        return list(set(list1) & set(list2))

    if not input_rows:
        return ([], [])
    union_result = input_rows[0]
    intersection_result = input_rows[0]

    for row in input_rows[1:]:
        union_result = union(union_result, row)
        intersection_result = intersection(intersection_result, row)

        union_result.sort(reverse=True)
        intersection_result.sort(reverse=True)

        return (union_result, intersection_result)
print(prob_3())