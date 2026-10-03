import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px



data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}
pd.set_option('display.max_colwidth',None)
pd.set_option('display.max_columns', None)
df = pd.DataFrame(data)

df['Salário']=df['Salário'].astype(float)
df['Limite_Credito']=df['Limite_Credito'].astype(float)

print(df.info())


#grafico de barrra
plt.figure(figsize=(12,8))
contagem=df['Profissão'].value_counts()

plt.bar(contagem.index,contagem.values)
plt.title('grafico de bar profissoes')
plt.xlabel('profissao')
plt.ylabel('fequencia')
plt.show()

#grafico de pizza
x=df['Estado_Civil'].value_counts().index
y=df['Estado_Civil'].value_counts().values
plt.pie(y,labels=x,autopct='%1.1f%%',startangle=90)
plt.title('pizza de estado civil')
plt.show()

#Grafico de bar pelo express
salario_por_profissao=df.groupby('Profissão')['Salário'].mean().reset_index

fig=px.bar(salario_por_profissao, x='Salário',y ='Profissão',orientation='h')
fig.show()


