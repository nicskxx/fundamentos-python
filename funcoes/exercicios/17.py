def troca():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    print("Antes:")
    print("A =", a)
    print("B =", b)

    a, b = b, a

    print("Depois:")
    print("A =", a)
    print("B =", b)

troca()
