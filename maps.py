import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import title
from pandas.plotting import plot_params

df=pd.read_csv('C:/Users/leandro/Downloads/ecommerce_preparados.csv')
pd.set_option('display.max_columns',None)
# print(df.head())
# print('final do dados===================================================')
# print(df.tail())

# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# print(df.describe())

#criando um dicionario para padronizar algumas colunas
# print(df['Gênero'].value_counts())

organizacao_genero ={
    'Masculino': 'Homem',
    'Feminino':'Mulher',
    'short menina verao look mulher':'Mulher',
    'Bebês': 'Bebês',
    'Sem gênero': 'Sem gênero',
    'Meninas': 'Meninas',
    'Meninos': 'Meninos',
    'Sem gênero infantil': 'infantil',

    'roupa para gordinha pluss P ao 52' :'Mulher',
    'Unissex'  :'Unissex' ,
    'menino' : 'Meninos' ,
    'bermuda feminina brilho Blogueira':'Mulher'
}

df['Gênero']=df['Gênero'].replace(organizacao_genero)

print(df.head())
print(df['Gênero'].value_counts())


# HISTOGRAMA (dos preços oferecidos)
plt.figure(figsize=(10,6))
plt.hist(df['Preço'])
plt.title('Histograma dos preços oferecidos')
plt.xlabel('Preço ')
plt.ylabel('Unidades')
plt.show()

 # GRAFICO DE DISPERSAO ENTRE NUMERO DE VENDAS E DESCONTO
mapa = {
    'Nenhum': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '+5': 5,
    '+25': 25,
    '+50': 50,
    '+100': 100,
    '+500': 500,
    '+1000': 1000,
    '+5mil': 5000,
    '+10mil': 10000,
    '+50mil': 50000
}
df['Qtd_Num']= df['Qtd_Vendidos'].map(mapa)
plt.figure(figsize=(12,6))
plt.scatter(df['Desconto'],df['Qtd_Num'])
plt.yscale('log')
plt.xlabel('Desconto')
plt.ylabel('numero de vendas')

plt.show()

# #mapa de calor
corr=df[['Nota','N_Avaliações','Preço','Qtd_Vendidos_Cod','Desconto']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlaçao ')
plt.show()
#
# #grafico de barra
plt.figure(figsize=(10,10))
x=df['Gênero'].value_counts().index
y=df['Gênero'].value_counts().values


plt.bar(x,y,color='green')
plt.title('Gênero')
plt.xlabel('Vendas por genero')
plt.ylabel('genero')
plt.show()



# #grafico de pizza
plt.figure(figsize=(10,6))
plt.pie(y,labels=x, autopct='%.1f%%', startangle=360)
plt.title('genero')
plt.show()



# #grafico de densidade
plt.figure(figsize=(10,6))
sns.kdeplot(df['Nota'], fill=True,color='green')
plt.title('Densidade das notas')
plt.xlabel('Notas')
plt.show()




# #grafico de regressao

sns.regplot(x='Qtd_Num',y='Preço', data=df, color='#278f65', scatter_kws={'alpha':0.5, 'color':'#34c289'})
plt.title('Regressão de vendas por preço')
plt.xlabel('Vendas')
plt.ylabel('Notas')
plt.show()

sns.pairplot(df[['Qtd_Vendidos_Cod', 'Preço', 'Marca_Cod']])
plt.show()