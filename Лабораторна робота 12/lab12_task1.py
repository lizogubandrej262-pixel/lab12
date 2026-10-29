def mult_table(n):
    print("\nТаблиця множення:")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(i, "x", j, "=", i * j)

def pifagor_table(n):
    print("\nТаблиця Піфагора:")
    for i in range(1, n + 1):
        row = ""
        for j in range(1, n + 1):
            row = row + str(i * j) + " "
        print(row)

N = int(input("Введіть число N: "))

mult_table(N)
pifagor_table(N)