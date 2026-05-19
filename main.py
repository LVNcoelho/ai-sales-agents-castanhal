import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Ferramenta de busca
search_tool = DuckDuckGoSearchRun()

# 2. Configuração do Gemini (Garantindo que o CrewAI aceite o formato)
minha_ia = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 3. AGENTE PESQUISADOR
mapeador = Agent(
    role='Especialista em Inteligência de Mercado',
    goal='Localizar 5 distribuidoras de {nicho} em {localizacao}',
    backstory='Você é um expert em encontrar empresas no Pará.',
    tools=[search_tool],
    llm=minha_ia, # Atribuindo diretamente aqui
    verbose=True,
    allow_delegation=False
)

# 4. AGENTE VENDEDOR
vendedor = Agent(
    role='Especialista em Vendas',
    goal='Criar e-mails para as empresas de {nicho} encontradas',
    backstory='Você é um copywriter talentoso da Conecta TI.',
    llm=minha_ia,
    verbose=True
)

# 5. TAREFAS
task_mapear = Task(
    description='Pesquise distribuidoras de {nicho} em {localizacao}. Pegue nome e cidade.',
    expected_output='Uma lista com 5 empresas reais.',
    agent=mapeador,
    tools=[search_tool]
)

task_vender = Task(
    description='Escreva e-mails de parceria para os leads encontrados.',
    expected_output='Os e-mails prontos para envio.',
    agent=vendedor
)

# 6. EQUIPE
projeto = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("### CONECTA TI INICIANDO... ###")
    projeto.kickoff(inputs={'nicho': 'Cosméticos', 'localizacao': 'Castanhal e Belém - PA'})