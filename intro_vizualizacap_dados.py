import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from scipy.stats import alpha

df=pd.read_csv('C:/Users/leandro/Downloads/clientes-v3-preparado.csv')
print(df.head().to_string())

#histograma
plt.hist(df['salario'])
plt.show()

#histograma- parametros
plt.figure(figsize=(10,6))
plt.hist(df['salario'], bins=100, color='green',alpha=0.8)
plt.title('Histograma - Distribuiçao de Salários')
plt.xlabel('Salário')
plt.xticks(ticks=range(0, int(df['salario'].max())+2000,2000))
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

#multplos
plt.figure(figsize=(10,6))
plt.subplot(2,2,1) # 2 linha, 2 colunas , 1* grafico
#grafico de dispersao
plt.scatter(df['salario'],df['salario'])
plt.title('Dispersao - salario e salário')
plt.xlabel('salário')
plt.ylabel('salário')


plt.subplot(1,2,2) # 1 linha, 2 colunas ,2* grafico
plt.scatter(df['salario'],df['anos_experiencia'],color='green',alpha=0.6,s=30)
plt.title('Dispersao - idade e anos de experiencia')
plt.xlabel('Salario')
plt.ylabel('anos e experiencia')

#mapa de calor
corr=df[['salario','anos_experiencia']].corr()
plt.subplot(2,2,3) # 1 linha , 2 coluna 3 grafico
sns.heatmap(corr,annot=True, cmap='coolwarm')
plt.title('Correlaçao salario e idade')

plt.tight_layout()
# plt.show()