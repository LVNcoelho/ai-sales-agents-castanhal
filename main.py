import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# 1. Configuração de Ambiente
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["OPENAI_API_KEY"] = "NA"

# 2. Inicializa a ferramenta de busca de um jeito simples
busca_ferramenta = DuckDuckGoSearchRun()

# 3. AGENTE PESQUISADOR
mapeador = Agent(
    role='Pesquisador de Mercado',
    goal='Encontrar 5 distribuidoras de {nicho} em {localizacao}',
    backstory='Expert em prospecção no Pará.',
    # O SEGREDO: Tiramos a ferramenta daqui e colocamos direto na Task
    llm="gemini/gemini-1.5-flash", 
    verbose=True,
    allow_delegation=False
)

# 4. AGENTE VENDEDOR
vendedor = Agent(
    role='Vendedor Conecta TI',
    goal='Criar e-mails para as empresas de {nicho} encontradas',
    backstory='Copywriter focado em parcerias.',
    llm="gemini/gemini-1.5-flash",
    verbose=True,
    allow_delegation=False
)

# 5. TAREFAS
task_mapear = Task(
    description='Use a ferramenta de busca para achar 5 distribuidoras de {nicho} em {localizacao}.',
    expected_output='Lista com nomes e cidades.',
    agent=mapeador,
    tools=[busca_ferramenta] # A ferramenta fica APENAS aqui agora
)

task_vender = Task(
    description='Escreva os e-mails para as empresas achadas.',
    expected_output='E-mails prontos.',
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
    print("\n### CONECTA TI: RODANDO AGORA! ###\n")
    projeto.kickoff(inputs={'nicho': 'Cosméticos', 'localizacao': 'Castanhal e Belém - PA'})