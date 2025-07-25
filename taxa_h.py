
import matplotlib.pyplot as plt

# Dados fictícios: taxa de homicídios por 100 mil habitantes por estado
homicidios_por_estado = {
    "AC": 28.5, "AL": 42.3, "AM": 35.1, "AP": 30.7, "BA": 47.8,
    "CE": 39.2, "DF": 22.4, "ES": 36.9, "GO": 33.1, "MA": 29.0,
    "MG": 18.7, "MS": 25.9, "MT": 27.3, "PA": 45.2, "PB": 38.4,
    "PE": 41.0, "PI": 24.6, "PR": 20.5, "RJ": 31.7, "RN": 44.6,
    "RO": 26.0, "RR": 32.1, "RS": 19.8, "SC": 16.2, "SE": 37.5,
    "SP": 10.8, "TO": 23.3
}

# Preparar dados para o gráfico
estados = list(homicidios_por_estado.keys())
valores = list(homicidios_por_estado.values())

# Criar o gráfico de barras
plt.figure(figsize=(15, 7))
plt.bar(estados, valores, color='indianred')

plt.title("Taxa de Homicídios por Estado no Brasil (por 100 mil habitantes)", fontsize=14)
plt.xlabel("Estados")
plt.ylabel("Taxa de Homicídios")
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Exibir valores nas barras
for i, valor in enumerate(valores):
    plt.text(i, valor + 0.8, f'{valor:.1f}', ha='center', fontsize=8)

plt.tight_layout()
plt.savefig("taxa_homicidios_por_estado.png", dpi=300)
plt.show()
