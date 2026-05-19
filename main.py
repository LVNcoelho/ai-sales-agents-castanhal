import os
from crewai import Agent, Task, Crew, Process

# 1. Configurações essenciais
os.environ["GOOGLE_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["OPENAI_API_KEY"] = "NA" # Bloqueia pedidos de chave da OpenAI

# 2. AGENTES (Note que removi o campo 'tools' daqui para o fiscal não reclamar)
mapeador = Agent(
    role='Especialista em Mercado',
    goal='Organizar uma lista de 5 distribuidoras de cosméticos no Pará',
    backstory='Você conhece muito bem o comércio de Belém e Castanhal.',
    llm="gemini/gemini-1.5-flash",
    verbose=True,
    allow_delegation=False
)

vendedor = Agent(
    role='Vendedor da Conecta TI',
    goal='Escrever e-mails de parceria para essas empresas',
    backstory='Você é especialista em parcerias comerciais tecnológicas.',
    llm="gemini/gemini-1.5-flash",
    verbose=True,
    allow_delegation=False
)

# 3. TAREFAS (Aqui pedimos para a IA usar o conhecimento dela, sem depender de ferramentas chatas)
task_mapear = Task(
    description="""Pense em 5 distribuidoras reais de cosméticos que atuam em Castanhal ou Belém (PA). 
    Liste o nome delas e a cidade.""",
    expected_output="Uma lista com 5 nomes de empresas e suas cidades.",
    agent=mapeador
)

task_vender = Task(
    description="Crie e-mails de prospecção para cada uma dessas empresas falando da Conecta TI.",
    expected_output="Os textos dos e-mails formatados.",
    agent=vendedor
)

# 4. A EQUIPE
projeto = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("\n### CONECTA TI: RODANDO EM MODO DE SEGURANÇA ###\n")
    projeto.kickoff()