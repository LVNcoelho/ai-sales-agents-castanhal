import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Inicializa a Ferramenta de Busca (Nome correto para a biblioteca atual)
search_tool = DuckDuckGoSearchRun()

# 2. Inicializa o Gemini 3.5 Flash
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", # Mantendo o identificador estável para o SDK
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 3. AGENTE PESQUISADOR (SDR)
mapeador = Agent(
    role='Especialista em Inteligência de Mercado Norte',
    goal='Localizar distribuidoras reais de {nicho} na região de {localizacao}',
    backstory="""Você é um expert em prospecção no Pará. Sua missão é encontrar nomes, 
    localização e o que essas empresas fazem de fato. Você usa a internet para validar os dados.""",
    tools=[search_tool],
    verbose=True,
    llm=llm
)

# 4. AGENTE VENDEDOR (COPYWRITER)
vendedor = Agent(
    role='Especialista em Outreach e Vendas',
    goal='Criar e-mails de parceria para os leads encontrados, focando no nicho de {nicho}',
    backstory="""Você cria mensagens que respeitam a cultura do Pará e mostram como a 
    Conecta TI pode ajudar essas empresas.""",
    verbose=True,
    llm=llm
)

# 5. TAREFAS
task_mapear = Task(
    description="""Pesquise no DuckDuckGo por 5 distribuidoras de {nicho} em {localizacao} e cidades próximas.
    Para cada uma, estime o tamanho (pequena, média, grande) e pegue o diferencial.""",
    agent=mapeador,
    expected_output="Uma lista com Nome, Cidade e Estimativa de Tamanho.",
    tools=[search_tool]
)

task_vender = Task(
    description="""Crie um e-mail personalizado para cada empresa da lista, 
    destacando que temos soluções de automação e produtos para o setor de {nicho}.""",
    agent=vendedor,
    expected_output="Os e-mails prontos para envio."
)

# 6. A EQUIPE
projeto_conecta_ti = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential,
    verbose=True
)

# 7. EXECUÇÃO
if __name__ == "__main__":
    inputs = {
        'nicho': 'Cosméticos e Estética',
        'localizacao': 'Castanhal e Belém - PA'
    }

    print(f"### Iniciando Prospecção para: {inputs['nicho']} ###")
    resultado = projeto_conecta_ti.kickoff(inputs=inputs)
    print("\n\n########################")
    print("## RESULTADO DA PROSPECÇÃO ##")
    print(resultado)