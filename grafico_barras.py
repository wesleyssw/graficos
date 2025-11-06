import matplotlib.pyplot as plt

produtos = ['Teclado', 'Mouse', 'Monitor', 'Webcam']
quantidades = [50,70,30,60]

plt.bar (produtos, quantidades, color=['skyblue', 'lightcoral', 'lightgreen', 'gold'])

plt.title("Comparação de Produtos em Estoque")
plt.xlabel("Produtos")
plt.ylabel("Quantidade em Estoque")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
