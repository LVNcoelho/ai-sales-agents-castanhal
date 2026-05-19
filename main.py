import os
from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Configura o LLM de um jeito que o CrewAI não rejeite
# Usamos o prefixo 'gemini/' que o CrewAI entende nativamente agora
os.environ["OPENAI_API_KEY"] = "NA" # Truque para o CrewAI não pedir chave da OpenAI
minha_ia = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# 2. Ferramenta de Busca
busca = DuckDuckGoSearchRun()

# 3. AGENTE PESQUISADOR
mapeador = Agent(
    role='SDR de Tecnologia',
    goal='Encontrar 5 distribuidoras de {nicho} em {localizacao}',
    backstory='Você é um especialista em prospecção de mercado no Pará.',
    tools=[busca],
    llm="gemini/gemini-3.5-flash",
    verbose=True,
    allow_delegation=False,
    memory=False # Desativando memória para evitar erro de validação
)

# 4. AGENTE VENDEDOR
vendedor = Agent(
    role='Copywriter de Vendas',
    goal='Escrever e-mails de parceria para os leads encontrados',
    backstory='Você é o braço direito da fundadora da Conecta TI.',
    llm=minha_ia,
    verbose=True,
    allow_delegation=False,
    memory=False
)

# 5. TAREFAS
task_mapear = Task(
    description='Pesquise distribuidoras de {nicho} em {localizacao}. Liste nome e cidade.',
    expected_output='Uma lista com o nome de 5 empresas e suas cidades.',
    agent=mapeador
)

task_vender = Task(
    description='Crie e-mails curtos e profissionais para cada empresa da lista.',
    expected_output='Os textos dos e-mails formatados.',
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
    print("\n### CONECTA TI: INICIANDO OPERAÇÃO ###\n")
    projeto.kickoff(inputs={'nicho': 'Cosméticos', 'localizacao': 'Castanhal e Belém - PA'})