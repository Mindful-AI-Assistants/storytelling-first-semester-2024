
# You can add data labels to the bars in a bar chart using the text
# function in matplotlib. Here's how you can modify your code to add 
# data labels to the bars:


import pandas as pd
import matplotlib.pyplot as plt

# Carregar o dataset
df = pd.read_csv('Furto_celular_2022.csv', sep=';')

# Remover linhas com dados faltantes nas colunas de interesse
df = df.dropna(subset=['BAIRRO', 'CIDADE', 'UF', 'QUANT_CELULAR'])

# Filtrar apenas as capitais
capitais = ['Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília', 'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte', 'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro', 'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis', 'São Paulo', 'Aracaju', 'Palmas']
df = df[df['CIDADE'].isin(capitais)]

# Agregar os dados por bairro
df_agg = df.groupby('BAIRRO')['QUANT_CELULAR'].sum().sort_values(ascending=False)

# Gerar o gráfico
plt.figure(figsize=(10,5))
bars = plt.bar(df_agg.head(10).index, df_agg.head(10).values)  # Change plot to bar and assign to a variable
plt.title('Top 10 Bairros com Maior Número de Furtos de Celulares')
plt.xlabel('Bairro')
plt.ylabel('Número de Furtos')

# Add data labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.05, yval, ha='center', va='bottom')

plt.show()