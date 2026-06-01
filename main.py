import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import DuckDuckGoSearchTool

# Configura a chave de ambiente
# Certifique-se de que a variável GEMINI_API_KEY esteja no seu ambiente
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY", "")

# 1. Configuração do Gemini 
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
)

search_tool = DuckDuckGoSearchTool()

# 2. AGENTE PESQUISADOR (Focado em Escolas e Alunos)
mapeador = Agent(
    role='Especialista em Inteligência Educacional',
    goal='Identificar potenciais alunos e parceiros para curso de informática em {localizacao}',
    backstory="""Você é um expert em encontrar leads quentes em cidades pequenas. 
    Sua missão é localizar jovens, comércios e grupos locais em Curuçá que precisam 
    urgentemente de qualificação em informática para emprego e gestão.""",
    tools=[search_tool], 
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. TAREFA: Mapear Leads (Alunos e Parceiros)
task_mapear = Task(
    description="""Pesquise ativamente na internet e redes sociais por:
    1. Grupos de vagas de emprego ou oportunidades em Curuçá-PA.
    2. Comerciantes locais que buscam profissionais qualificados.
    3. Perfis ou comunidades onde jovens discutem primeiro emprego ou cursos.
    
    PARA CADA LEAD IDENTIFICADO, gere: Nome do Lead/Grupo, Fonte (onde foi achado), 
    e um 'Sinal de Necessidade' (por que ele precisa de curso de informática agora).""",
    agent=mapeador,
    expected_output="Uma lista estruturada contendo: Nome do Lead/Grupo, Fonte da busca, Sinal de Necessidade e Script de abordagem sugerido."
)

# 4. A EQUIPE
projeto_conecta_ti = Crew(
    agents=[mapeador],           
    tasks=[task_mapear],         
    process=Process.sequential,
    verbose=True
)

# 5. EXECUÇÃO FOCO: CURUÇÁ
if __name__ == "__main__":
    inputs = {
        'nicho': 'Cursos de Informática Básica e Profissionalizante',
        'localizacao': 'Curuçá - Pará'
    }

    print(f"\n### 🚀 Iniciando Prospecção Conecta TI para: {inputs['nicho']} em {inputs['localizacao']} ###\n")
    resultado = projeto_conecta_ti.kickoff(inputs=inputs)
    print("\n\n########################")
    print("## RESULTADO DA PROSPECÇÃO ##")
    print(resultado)
