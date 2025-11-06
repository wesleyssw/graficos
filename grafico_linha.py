import matplotlib.pyplot as plt

dias = [1, 2, 3, 4, 5]
entrada = [10, 20, 15, 25, 30]
saida = [5, 10, 8, 20, 18]

plt.plot(dias, entrada, label="Entradas", color="green")
plt.plot(dias, saida, label="Saídas", color="red")
plt.title("Movimentações de Estoque")
plt.xlabel("Dias")
plt.ylabel("Quantidade")
plt.legend()
plt.show()
