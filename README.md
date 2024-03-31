# Projeto Database OpenAI


 <img src="https://github.com/tvlemes/project_database_openai/blob/main/docs/img_1.PNG"> 
<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Indície</summary>
  <ol>
    <li>
      <a href="#objetivo">Objetivo</a>
      <ul>
        <li><a href="#bibliotecas-utilizadas">Bibliotecas utilizadas</a></li>
      </ul>
    </li>
    <li>
      <a href="#arquivos-e-pastas">Arquivos e Pastas</a>
    </li>
    <li>
      <a href="#sobre">Sobre</a>
    </li>
  </ol>
</details>

## Objetivo

Esté projeto tem como objetivo implementar a biblioteca <b>Langchain</b> para trabalhar com banco de dados locais, em especifico este, o <b>SQLite</b>.

<!-- programas-e-bibliotecas -->
### Bibliotecas utilizadas
Nele foi implementado as seguintes bibliotecas:

* langchain.prompt
* langchain.chat_models
* langchain.memory
* langchain.schema
* langchain.agents
* dotenv
* os
* warnings
* langchain.tools
* pydantic.v1
* sqlite3

<!-- arquivos-e-pastas -->
## Arquivos e Pastas

A estrutura física contém o arquivo <b>main.py</b> que é o arquivo que inicializa o app. Na pasta <b>tools</b> contém dois arquivos principais:

* <b>report.py</b> - arquivo responsável por gerar arquivos em <b>HTML</b> para relatórios;
* <b>sql.py</b> - arquivo responsável por realizar consultas <b>SQL</b>.

O arquivo <b>.env_example</b> é o arquivo que conterá a chave cadastrada no site da <a href="https://openai.com/">openai</a>. Este deverá ser renomeado para <b>.env</b>.

<!-- sobre -->
## Sobre

Autor: Thiago Vilarinho Lemes <br>
LinkedIn <a href="https://www.linkedin.com/in/thiago-v-lemes-b1232727">Thiago V. Lemes</a><br>
e-mail: contatothiagolemes@gmail.com | lemes_vilarinho@yahoo.com.br
