import os
from crewai import Agent, Task, Crew, Process

# 1. Configurações de Chave
# O CrewAI busca a chave com o nome 'GOOGLE_API_KEY'
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["OPENAI_API_KEY"] = "NA" 

# 2. DEFINIÇÃO DOS AGENTES
mapeador = Agent(
    role='Especialista em Mercado',
    goal='Identificar 5 distribuidoras de cosméticos em Castanhal e Belém (PA)',
    backstory='Você é um expert em prospecção de negócios no Pará.',
    # Este formato abaixo é o que resolve o erro 404:
    llm="gemini/gemini-1.5-flash", 
    verbose=True,
    allow_delegation=False
)

vendedor = Agent(
    role='Vendedor da Conecta TI',
    goal='Escrever e-mails de parceria profissionais para as empresas listadas',
    backstory='Você é especialista em copywriting para parcerias comerciais.',
    llm="gemini/gemini-1.5-flash",
    verbose=True,
    allow_delegation=False
)

# 3. DEFINIÇÃO DAS TAREFAS
task_mapear = Task(
    description="""Pense em 5 distribuidoras reais de cosméticos em Castanhal ou Belém. 
    Liste o nome da empresa e a cidade.""",
    expected_output="Uma lista com 5 nomes de empresas e suas respectivas cidades.",
    agent=mapeador
)

task_vender = Task(
    description="Crie e-mails curtos e persuasivos para as 5 empresas citadas.",
    expected_output="Os textos dos e-mails formatados e prontos para envio.",
    agent=vendedor
)

# 4. A EQUIPE (CREW)
projeto = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n### CONECTA TI: INICIANDO OPERAÇÃO FINAL ###\n")
    projeto.kickoff()