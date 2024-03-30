'''
Projeto para Banco de Dados 
Autor: Thiago Vilarinho Lemes
Data: 2024-03-30
'''
############################ Bibliotecas ###########################
from langchain.prompts import MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryMemory
from langchain.schema import SystemMessage
from langchain.agents import OpenAIFunctionsAgent, AgentExecutor
import os
from dotenv import load_dotenv
from tools.sql import run_query_tool, return_tables, describe_tables_tool
from tools.report import write_report_tool
import warnings

############################ Configurações ###########################
warnings.filterwarnings('ignore')
load_dotenv()
chat    = ChatOpenAI()
# memory  = ConversationSummaryMemory( # memoria cache
#     memory_key      = 'messages', 
#     return_messages = True,
#     llm             = chat
# )
tables = return_tables()
############################ Prompt ###########################
prompt      = ChatPromptTemplate(
    messages=[
        SystemMessage(content=
                      (
                            "You are an AI that has access to a SQLite.\n" 
                            f"The database has tables of: {tables}\n."
                    )),
        HumanMessagePromptTemplate.from_template('{input}'), # mensagem enviada pelo humano, armazenada na variavel input
        MessagesPlaceholder(variable_name='agent_scratchpad') # serve como lembrate das mensagens anteriores
    ]
)

############################ Agente ###########################
tools       = [run_query_tool, describe_tables_tool, write_report_tool]

agent       = OpenAIFunctionsAgent(
    llm     = chat,
    prompt  = prompt,
    tools   = tools
)

agent_executor = AgentExecutor(
    agent   = agent,
    verbose =True,
    tools   = tools
)

############################ Chat ###########################
os.system('cls')
while True:

    input_chat = input('>> ')
    if input_chat != 'sair':
        agent_executor(input_chat)
    else:
        break
