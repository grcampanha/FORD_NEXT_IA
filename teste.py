import pandas as pd
import pyodbc 
from joblib import dump, load

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-MA9TV66\SQLEXPRESS;"
    "Database=REVOSOFT;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conectado")

cursor = conexao.cursor()

query = """select * from veiculo"""

df = pd.read_sql(query, conexao)

lista = df.values.tolist()

modelo = load('modelo.joblib')

for veiculo in lista:
    model = modelo.predict([[veiculo[2],veiculo[3],veiculo[4], veiculo[5], veiculo[6]]])
    
    status = model[0]
    alocar = """INSERT INTO IA (veiculo_id, dia, status) VALUES 
      ({veiculo[0]}, '25/08/2022', '{status}')"""
    print(status)
    print(alocar)
    cursor.execute(alocar)
    cursor.commit()
    print("ve lá")
    