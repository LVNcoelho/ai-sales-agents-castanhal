import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import DuckDuckGoSearchTool
from langchain_google_genai import ChatGoogleGenerativeAI

# 1. Configuração do Gemini (Grátis via Google AI Studio)
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)

# Ferramenta de busca gratuita
search_tool = DuckDuckGoSearchTool()

# 2. AGENTE PESQUISADOR (SDR) - Agora com "Olhos" na internet
mapeador = Agent(
    role='Especialista em Inteligência de Mercado Norte',
    goal='Localizar distribuidoras reais de {nicho} na região de {localizacao}',
    backstory="""Você é um expert em prospecção no Pará. Sua missão é encontrar nomes, 
    localização e o que essas empresas fazem de fato. Você usa a internet para validar os dados.""",
    tools=[search_tool], # <--- Aqui ele ganha a visão!
    verbose=True,
    llm="gemini/gemini-1.5-flash"
)

# 3. AGENTE VENDEDOR (COPYWRITER)
vendedor = Agent(
    role='Especialista em Outreach e Vendas',
    goal='Criar e-mails de parceria para os leads encontrados, focando no nicho de {nicho}',
    backstory="""Você cria mensagens que respeitam a cultura do Pará e mostram como a 
    Conecta TI pode ajudar essas empresas.""",
    verbose=True,
    llm="gemini/gemini-1.5-flash"
)

# 4. TAREFAS
task_mapear = Task(
    description="""Pesquise no Google/DuckDuckGo por 5 distribuidoras de {nicho} em {localizacao} e cidades próximas.
    Para cada uma, estime o tamanho (pequena, média, grande) e pegue o diferencial.""",
    agent=mapeador,
    expected_output="Uma lista com Nome, Cidade e Estimativa de Tamanho."
)

task_vender = Task(
    description="""Crie um e-mail personalizado para cada empresa da lista, 
    destacando que temos soluções de automação e produtos para o setor de {nicho}.""",
    agent=vendedor,
    expected_output="Os e-mails prontos para envio."
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
    # Aqui você pode mudar o nicho e a localização para qualquer oportunidade que surgir!
    inputs = {
        'nicho': 'Cosméticos e Estética',
        'localizacao': 'Castanhal e Belém - PA'
    }

    print(f"### Iniciando Prospecção para: {inputs['nicho']} ###")
    resultado = projeto_conecta_ti.kickoff(inputs=inputs)
    print("\n\n########################")
    print("## RESULTADO DA PROSPECÇÃO ##")
    print(resultado)