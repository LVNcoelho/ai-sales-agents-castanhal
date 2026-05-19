import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# 1. CONFIGURAÇÃO DE AMBIENTE (O SEGREDO PARA NÃO DAR ERRO)
# O CrewAI busca a chave com este nome exato:
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
# Evita que o sistema peça chaves que não estamos usando:
os.environ["OPENAI_API_KEY"] = "NA"

# 2. FERRAMENTA DE BUSCA
busca = DuckDuckGoSearchRun()

# 3. AGENTE PESQUISADOR (SDR)
mapeador = Agent(
    role='SDR de Tecnologia',
    goal='Encontrar 5 distribuidoras de {nicho} em {localizacao}',
    backstory='Você é um especialista em prospecção de mercado no Pará, focado em Castanhal e Belém.',
    tools=[busca],
    # Usando a string direta para evitar erro de validação do Pydantic
    llm="gemini/gemini-3.5-flash", 
    verbose=True,
    allow_delegation=False,
    memory=False
)

# 4. AGENTE VENDEDOR (COPYWRITER)
vendedor = Agent(
    role='Copywriter de Vendas',
    goal='Escrever e-mails de parceria para os leads encontrados',
    backstory='Você é o braço direito da fundadora da Conecta TI, criando mensagens profissionais e culturais.',
    llm="gemini/gemini-3.5-flash",
    verbose=True,
    allow_delegation=False,
    memory=False
)

# 5. TAREFAS
task_mapear = Task(
    description='Pesquise distribuidoras de {nicho} em {localizacao}. Liste nome e cidade.',
    expected_output='Uma lista formatada com o nome de 5 empresas reais e suas cidades.',
    agent=mapeador,
    tools=[busca]
)

task_vender = Task(
    description='Crie e-mails curtos e profissionais para cada empresa da lista, oferecendo automação da Conecta TI.',
    expected_output='Os textos dos e-mails prontos para revisão e envio.',
    agent=vendedor
)

# 6. EQUIPE (A CREW)
projeto = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n### CONECTA TI: INICIANDO OPERAÇÃO COM GEMINI 3.5 FLASH ###\n")
    
    # Executando a prospecção
    projeto.kickoff(inputs={
        'nicho': 'Cosméticos e Estética', 
        'localizacao': 'Castanhal e Belém - PA'
    })