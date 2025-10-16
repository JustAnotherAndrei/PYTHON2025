def prob1() -> list[int]:
    n = int(input("Input: "))
    prob1_la_patrat = lambda x: x * x
    rezultat = [prob1_la_patrat(i) for i in range(1, n + 1)]

    print("_".join(map(str, rezultat)))
    return rezultat

print(prob1())