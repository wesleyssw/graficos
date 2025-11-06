import matplotlib.pyplot as plt

categorias = ['Eletronicos', 'Vestuario', 'Alimentos']
valores = [15000, 8000, 5000]

explode = (0.05, 0, 0)

plt.pie(valores,
        labels=categorias,
        autopct='%1.1f%%',
        startangle=90,
        shadow=True,
        explode=explode,
        wedgeprops={"edgecolor":"black", 'linewidth':1,'antialiased':True})

plt.title("Produção de Valor Total de estoque por Categoria", fontsize=14)
plt.axis('equal')
plt.show()
