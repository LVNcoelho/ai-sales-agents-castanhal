import os
from crewai import Agent, Task, Crew, Process
# 💡 Correção 1: Importações corretas do LangChain e CrewAI Tools
from langchain_google_genai import ChatGoogleGenerativeAI
from crewai_tools import DuckDuckGoSearchTool

# Configura a chave de ambiente global para o CrewAI e o Gemini
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY", "")

# 1. Configuração do Gemini 
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3, # Abaixamos a temperatura para dados mais exatos na busca
)

# 💡 Correção 2: Instanciação única da ferramenta de busca oficial do CrewAI
search_tool = DuckDuckGoSearchTool()

# 2. AGENTE PESQUISADOR (SDR) - Agora com "Olhos" na internet
mapeador = Agent(
    role='Especialista em Inteligência de Mercado Norte',
    goal='Localizar distribuidoras reais de {nicho} na região de {localizacao}',
    backstory="""Você é um expert em prospecção no Pará. Sua missão é encontrar nomes, 
    localização e o que essas empresas fazem de fato. Você usa a internet para validar os dados.""",
    tools=[search_tool], 
    verbose=True,
    allow_delegation=False,
    llm=llm # 💡 Correção 3: Passando o objeto LLM correto configurado acima
)

# 3. AGENTE VENDEDOR (COPYWRITER)
vendedor = Agent(
    role='Especialista em Outreach e Vendas',
    goal='Criar e-mails de parceria para os leads encontrados, focando no nicho de {nicho}',
    backstory="""Você cria mensagens que respeitam a cultura do Pará e mostram como a 
    Conecta TI pode ajudar essas empresas com automação e inteligência.""",
    verbose=True,
    allow_delegation=False,
    llm=llm # 💡 Correção 3: Passando o objeto LLM correto configurado acima
)

# 4. TAREFAS
task_mapear = Task(
    description="""Pesquise usando a ferramenta de busca por 10 distribuidoras reais de {nicho} em {localizacao} e cidades próximas.
    Para cada uma, identifique o Nome, a Cidade, estime o tamanho (pequena, média, grande) e capture o principal diferencial deles.""",
    agent=mapeador,
    expected_output="Uma lista estruturada contendo: Nome da Empresa, Cidade, Estimativa de Tamanho e Diferencial Comercial."
)

#task_vender = Task(
   # description="""Com base EXCLUSIVAMENTE na lista de empresas reais gerada pela tarefa anterior, 
   # crie um e-mail de outreach personalizado para cada uma delas. O e-mail deve saudar o cliente respeitando 
   # o tom de negócios do Pará, citar o diferencial que encontramos dele para gerar conexão, e oferecer as 
   # soluções de automação comercial e funcionários digitais da Conecta TI.""",
   # agent=vendedor,
   # expected_output="Os e-mails personalizados prontos para envio, separados por empresa."
)

# 5. A EQUIPE
projeto_conecta_ti = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential,
    verbose=True
)

# 6. EXECUÇÃO MULTI-NICHO
if __name__ == "__main__":
    inputs = {
        'nicho': 'Cosméticos e Estética',
        'localizacao': 'Castanhal e Belém - PA'
    }

    print(f"\n### 🚀 Iniciando Prospecção Conecta TI para: {inputs['nicho']} ###\n")
    resultado = projeto_conecta_ti.kickoff(inputs=inputs)
    print("\n\n########################")
    print("## RESULTADO DA PROSPECÇÃO ##")
    print(resultado)
