# Desafio MBA Engenharia de Software com IA - Full Cycle

O projeto apresenta um modelo de Injestão e Busca Semântica com LangChain e PostgreSQL com a extensão PGVector.

Nesta versão as seguintes funcionalidades estão disponíveis:
1. Ingestão: Ler um arquivo PDF e salvar suas informações em um banco de dados PostgreSQL com extensão pgVector.
2. Busca: Permitir que o usuário faça perguntas via linha de comando (CLI) simulando um chat, com respostas baseadas apenas no conteúdo do PDF.

## Tecnologias
* Linguagem: Python
* Framework: LangChain
* Banco de dados: PostgreSQL com pgVector
* Execução do banco de dados: Docker & Docker Compose.

## Estrutura do projeto
```
├── docker-compose.yml
├── requirements.txt      # Dependências
├── .env.example          # Template da variável OPENAI_API_KEY
├── src/
│   ├── ingest.py         # Script de ingestão do PDF
│   ├── search.py         # Script de busca
│   ├── chat.py           # CLI para interação com usuário
├── document.pdf          # PDF para ingestão
└── README.md             # Instruções de execução
```

## Configuração do ambiente
1. Criar o ambiente python:

``` bash
python3 -m venv venv
source venv/bin/activate
```

2. Atualizar as dependências do arquivo requirements.txt

``` bash
pip3 install -r requirements.txt
```

3. Variáveis de ambiente
    - Duplique o arquivo `.env.example` e renomeie para `.env`
    - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais.

## Executando o projeto

1. Verifique se o arquivo PDF `document.pdf` na raiz do projet está com o conte;údo desejado. O arquivo pode ser alterado usando a Variável de Ambiente `PDF_PATH`.

2. Suba o Container com o Banco de Dados

``` bash 
docker compose up -d
```

3. Execute a Injestão de Documentos 
```bash 
python src/ingest.py
```

4. Execute o chat:
``` bash
python src/chat.py
```