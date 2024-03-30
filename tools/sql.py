'''
Projeto para Banco de Dados 
Autor: Thiago Vilarinho Lemes
Data: 2024-03-30
'''
from langchain.tools import Tool
from pydantic.v1 import BaseModel
import sqlite3

############################ Conector do BD ###########################
try:
    # Conectar ao banco de dados SQLite
    path_db = './instancias/db.sqlite'
    conn = sqlite3.connect(path_db)
    # Criar um cursor para executar comandos SQL
    cursor = conn.cursor()
except Exception as err:
    print(f"Ocorreu um erro ao estabelecer conexão com SQLite: {err}")

############################ Lista as tabelas do BD ###########################
def return_tables():
    # Consulta SQL para selecionar o número de tabelas
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    # Executar a consulta
    cursor.execute(query)
    # Obter o resultado
    tables = cursor.fetchall() #fetchone()[0]
    tabelas = [i[0] for i in tables]
    return tabelas

############################ Executa consultas query ###########################
def run_sqlite_query(query):
    try:        
        cursor.execute(query)
        # resultado = cursor.fetchone()
        resultado = cursor.fetchall()
        if len(resultado) > 1:
            return resultado
        else:
            return resultado[0]
        
    except Exception as ex:
        print(f'O seguinte erro ocorreu: {str(ex)} erro no run_sqlite_query')

class RunQueryArgsSchema(BaseModel):
    query: str

run_query_tool      = Tool.from_function(
    name            = 'run_sql_lite_query', 
    description     = 'Execute uma consulta SQLite', 
    func            = run_sqlite_query,
    args_schema     = RunQueryArgsSchema
)

############################ Verificando a estrutura das tabelas ###########################
def describe_tables(tables_name):
    try:
        cursor.execute(f"SELECT * FROM pragma_table_info('{tables_name}');")
        sch = cursor.fetchall() 
        return sch
    except Exception as ex:
        print(f'O seguinte erro ocorreu: {str(ex)} erro no describe_tables')

class DescribeTablesArgsSchema(BaseModel):
    tables_name: list[str]

describe_tables_tool = Tool.from_function(
    name             = 'describe_tables',
    description      = "Dado o nome da tabela retorna os campos da tabela",
    func             = describe_tables,
    args_schema      = DescribeTablesArgsSchema
)
