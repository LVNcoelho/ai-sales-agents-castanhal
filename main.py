import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun
from crewai.tools import tool 

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

if "GEMINI_API_KEY" not in os.environ:
    os.environ["GEMINI_API_KEY"] = os.getenv("GOOGLE_API_KEY", "")

# 1. Configuração do Gemini
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
)

# 2. Ferramenta de Busca
@tool("Ferramenta de Busca Web")
def web_search(search_query: str) -> str:
    """Utilize esta ferramenta para buscar informações sobre empresas e negócios locais na internet."""
    search = DuckDuckGoSearchRun()
    return search.run(search_query)

# 3. AGENTE PESQUISADOR (SDR)
mapeador = Agent(
    role='Analista de Inteligência de Mercado para PMEs',
    goal='Localizar PMEs brasileiras em crescimento que necessitam de automação comercial',
    backstory="""Você é um especialista em encontrar empresas de bairro, lojas familiares e 
    serviços locais (clínicas, petshops, moda) que estão em crescimento. 
    Sua prioridade absoluta é identificar empresas com presença profissional no Instagram ou 
    Google Maps, mas que operam de forma manual. 
    
    FILTROS RÍGIDOS E PROIBIÇÕES: 
    - Priorize estritamente lojas de bairro, empresas familiares e negócios locais.
    - É estritamente PROIBIDO listar grandes redes, franquias famosas, multinacionais ou startups.
    - EXCLUA RIGOROSAMENTE marcas como: Magazine Luiza, Renner, CVC, Casas Bahia, Riachuelo, 
      Petz, Cobasi, Cacau Show, ou qualquer rede de âmbito nacional.
    - Busque por empresas que precisam automatizar o atendimento para escalar.""",
    tools=[web_search], 
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 4. TAREFA
task_mapear = Task(
    description="""Pesquise 10 PMEs do nicho de {nicho} em todo o {localizacao}.
    FOCO: Empresas com presença ativa no Instagram ou Google Maps.
    
    CRITÉRIOS DE SELEÇÃO: 
    1. Empresas de bairro ou familiares com crescimento aparente.
    2. Sinais de crescimento: posts recentes, muitos comentários, novas unidades, promoções.
    
    EXCLUA: Startups, grandes redes de franquias, bancos ou indústrias.
    
    Para cada empresa, identifique: Nome, Cidade, Link (Instagram ou Site) e o 'Sinal de Crescimento' 
    que justifica o contato da Conecta TI.""",
    agent=mapeador,
    expected_output="Uma lista estruturada contendo: Nome da Empresa, Cidade, Link, Sinal de Crescimento e Por que precisa de automação.",
)

# 5. A EQUIPE (Corrigida: sem o argumento 'config' que gerou o erro de validação)
projeto_conecta_ti = Crew(
    agents=[mapeador],           
    tasks=[task_mapear],         
    process=Process.sequential,
    verbose=True
)

# 6. EXECUÇÃO
if __name__ == "__main__":
    inputs = {
        'nicho': 'Clínicas de Estética, Petshops e Varejo de Moda',
        'localizacao': 'Brasil'
    }

    print(f"\n### 🚀 Iniciando Prospecção Conecta TI para: {inputs['nicho']} ###\n")
    
    try:
        resultado = projeto_conecta_ti.kickoff(inputs=inputs)
        print("\n\n########################")
        print("## RESULTADO DA PROSPECÇÃO ##")
        print(resultado)
    except Exception as e:
        print(f"\n❌ Ocorreu um erro na execução: {e}")
