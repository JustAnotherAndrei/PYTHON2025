def prob_5() -> None:
    lst = None

    while True:
        cmd = input("Comanda: ").strip().split()

        if not cmd:
            continue
        operation = cmd[0].upper()

        if operation == "INIT":
            lst = []
        elif operation == "APPEND":
            if lst is None:
                print("Lista neinitializata")
                continue
            value = cmd[1]
            lst.append(value)
        elif operation == "INSERT":
            if lst is None:
                print("Lista neinitializata")
                continue
            value = cmd[1]
            index = int(cmd[2])
            if index >= len(lst):
                lst.append(value)
            else:
                lst.insert(index, value)
        elif operation == "REMOVE":
            if lst is None:
                print("Lista neinitializata")
                continue
            value = cmd[1]
            if value in lst:
                lst.remove(value)
            else:
                print("Nu exista")
        elif operation == "PRINT":
            if lst is None:
                print("Lista neinitializata")
                continue
            print(lst)
        elif operation == "EXIT":
            break
        else:
            print("Comanda invalida")

print (prob_5())
