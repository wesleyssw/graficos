import matplotlib.pyplot as plt

precos = [50,120,300,80,20]
estoque = [80,25,10,70,150]

plt.figure(figsize=(10,6))
plt.scatter(precos, estoque, color='blue', alpha=0.7)

plt.title("Relação entre Preço Unitário e Quantidade em Estoque", fontsize=15)
plt.xlabel("Preço Unitário (R$)", fontsize=12)
plt.ylabel("Quantidade em Estoque", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()