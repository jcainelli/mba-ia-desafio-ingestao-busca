import os
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from search import search_prompt
from dotenv import load_dotenv

load_dotenv()
for k in ("PDF_PATH", "OPENAI_EMBEDDING_MODEL","OPENAI_API_KEY","PG_VECTOR_COLLECTION_NAME", "DATABASE_URL"):
    if not os.getenv(k):
        raise RuntimeError(f"Environment variable {k} is not set")

def main():
    chain = search_prompt()

    if not chain:
        print("Não foi possível iniciar o chat. Verifique os erros de inicialização.")
        return
    
    template = PromptTemplate(
        input_variables=["contexto", "pergunta"],
        template=chain
    )

    embeddings = OpenAIEmbeddings(model=os.getenv("OPENAI_EMBEDDING_MODEL"))

    store = PGVector(
        embeddings=embeddings,
        collection_name=os.getenv("PG_VECTOR_COLLECTION_NAME"),
        connection=os.getenv("DATABASE_URL"),
        use_jsonb=True,
    )

    llm = ChatOpenAI(model="gpt-5-nano", temperature=0)
    pipeline = template | llm | StrOutputParser()

    print("Informa a sua pergunta (para emcerrar digite, quit ou exit)")
    while True:
        query = input('> ')
        if query.strip().lower() in ("exit", "quit"): 
            print("Obrigado. Finalizando o chat.")
            break
        result = executeChain(store, pipeline, query)
        print(result)

    pass

def executeChain(store, pipeline, query):
    results = store.similarity_search_with_score(query, k=10)
    context = "\n".join([doc.page_content for doc, _ in results])
    result = pipeline.invoke({"contexto": context, "pergunta": query})
    return result

if __name__ == "__main__":
    main()