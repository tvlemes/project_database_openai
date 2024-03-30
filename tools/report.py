'''
Projeto para Banco de Dados 
Autor: Thiago Vilarinho Lemes
Data: 2024-03-30
'''
from langchain.tools import StructuredTool
from pydantic.v1 import BaseModel

def write_report(filename, html):
    with open(filename, 'w') as f:
        f.write(html)

class WriteReportArgsSchema(BaseModel):
    filename: str
    html: str
write_report_tool = StructuredTool.from_function(
    name        ="write_report",
    description ="Grave um arquivo HTML no disco. Utilize esta ferramenta sempre que alguém solicitar um relatório.",
    func        = write_report,
    args_schema = WriteReportArgsSchema
)
