def fibonacci(n):
    t1 = 0
    t2 = 1
    t3 = 0
    found = False

    print("Sequência de Fibonacci:", end=" ")
    while t3 <= n:
        print(f"{t3}", end=" ")
        if t3 == n:
            found = True
        t3 = t1 + t2
        t1 = t2
        t2 = t3

    if found:
        print(f"\nO número {n} faz parte da sequência de Fibonacci.")
    else:
        print(f"\nO número {n} não faz parte da sequência de Fibonacci.")

numero = int(input("Digite um número: "))
fibonacci(numero)