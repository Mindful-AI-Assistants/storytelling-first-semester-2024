
# Este código cria um gráfico de barras animado que atualiza a cada
# segundo. A função animate é chamada a cada frame da animação.
# Ela limpa o gráfico atual e desenha um novo gráfico de barras.
# As barras são coloridas de azul claro, têm uma largura de 0.5 e os
# rótulos de dados são adicionados no topo de cada barra.
# A animação dura 10 segundos (10 frames com um intervalo de 1 segundo
# entre cada frame).


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Carregar o dataset
df = pd.read_csv('Furto_celular_2022.csv', sep=';')

# Remover linhas com dados faltantes nas colunas de interesse
df = df.dropna(subset=['BAIRRO', 'CIDADE', 'UF', 'QUANT_CELULAR'])

# Filtrar apenas as capitais
capitais = ['Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas']
df = df[df['CIDADE'].isin(capitais)]

# Agregar os dados por bairro
df_agg = df.groupby('BAIRRO')['QUANT_CELULAR'].sum().sort_values(
    ascending=False)

# Gerar o gráfico
fig, ax = plt.subplots(figsize=(10, 5))

def animate(i):
    ax.clear()
    df_agg.head(10).plot(kind='bar', ax=ax, color='skyblue', width=0.5)
    plt.title('Top 10 Bairros com Maior Número de Furtos de Celulares')
    plt.xlabel('Bairro')
    plt.ylabel('Número de Furtos')
    plt.xticks(fontsize=14)
    for i, v in enumerate(df_agg.head(10).values):
        ax.text(i, v + 0.2, int(v), ha='center', va='bottom', fontsize=10)


ani = animation.FuncAnimation(fig, animate, frames=10, interval=1000, repeat=False)

plt.show()

