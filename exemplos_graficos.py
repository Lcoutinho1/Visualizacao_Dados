import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df= pd.read_csv('C:/Users/leandro/Downloads/clientes-v3-preparado.csv')

df_corr= df[['salario','idade','anos_experiencia','numero_filhos','nivel_educacao_cod','area_atuacao_cod','estado_cod']].corr()
#heatmap de correlaçao
plt.figure(figsize=(10,10))
sns.heatmap(df_corr, annot=True, fmt=".2f")
plt.title('Mapa de calor de correalçao entre as variaveis')
plt.show()

#ja usei
# countplot
sns.countplot(x='estado_civil', data=df)
plt.title('distribuiçao do estado civil')
plt.xlabel('estado civil')
plt.ylabel('contagem')
plt.show()

#countplot com legenda
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df)
plt.title('distribuiçao do estado civil')
plt.xlabel('estado civil')
plt.ylabel('contagem')
plt.legend(title='Nivel de educacao')
plt.show()
