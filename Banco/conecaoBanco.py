import pyodbc
import pandas as pd

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-MA9TV66\SQLEXPRESS;"
    "Database=REVOSOFT;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conectado")

cursor = conexao.cursor()

comando ="""INSERT INTO teste (id_vendas, cliente) VAlUES (2, 'tu') """

comando1 = """
select * from teste"""



df = pd.read_sql(comando1, conexao)

print (df.head())

