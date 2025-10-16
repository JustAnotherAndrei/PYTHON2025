def prob_4() -> None:
    count, total = map(int, input("Input: ").split())
    pairs = [(x, total - x) for x in range(1, count + 1)]

    print(pairs)
print (prob_4())
