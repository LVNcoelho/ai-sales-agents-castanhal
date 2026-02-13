import os
from crewai import Agent, Task, Crew, Process

# Configuração dos Agentes de Prospecção - Região de Castanhal/PA
# Este projeto automatiza a localização e a primeira abordagem de distribuidoras

# 1. AGENTE PESQUISADOR (SDR)
mapeador = Agent(
    role='Especialista em Inteligência de Mercado Norte',
    goal='Localizar distribuidoras de produtos de estética em um raio de 300km de Castanhal-PA',
    backstory="""Você é um expert em logística e prospecção B2B no estado do Pará. 
    Conhece profundamente os polos comerciais de Belém, Capanema, Paragominas e cidades vizinhas. 
    Sua missão é encontrar empresas que tenham perfil para revenda de produtos de estética.""",
    allow_delegation=False,
    verbose=True
)

# 2. AGENTE VENDEDOR (COPYWRITER)
vendedor = Agent(
    role='Especialista em Outreach e Vendas',
    goal='Criar e-mails de parceria comercial altamente personalizados e persuasivos',
    backstory="""Você é o melhor copywriter de vendas da região. Sua habilidade é transformar 
    uma lista de nomes em reuniões agendadas. Você adapta o tom de voz para ser profissional, 
    porém próximo, respeitando a cultura comercial do Pará.""",
    allow_delegation=False,
    verbose=True
)

# -------------------------------------------------------------------------
# DEFINIÇÃO DAS TAREFAS
# -------------------------------------------------------------------------

task_mapear = Task(
    description="""Mapear 10 distribuidoras de cosméticos ou equipamentos de estética 
    em um raio de 300km de Castanhal, focando em hubs como Belém e municípios vizinhos. 
    Extraia o nome da empresa e o diferencial de mercado dela.""",
    agent=mapeador,
    expected_output="Um relatório detalhado com nomes de empresas, localização e perfil de atuação."
)

task_vender = Task(
    description="""Com base nas empresas encontradas, escreva um e-mail de prospecção 
    para cada uma, convidando para uma parceria. O e-mail deve mencionar que a empresa 
    é referência na região e que temos uma solução para aumentar o catálogo deles.""",
    agent=vendedor,
    expected_output="Uma lista de e-mails prontos para envio, com campos personalizados."
)

# -------------------------------------------------------------------------
# ORQUESTRAÇÃO DA EQUIPE (CREW)
# -------------------------------------------------------------------------

projeto_estetica = Crew(
    agents=[mapeador, vendedor],
    tasks=[task_mapear, task_vender],
    process=Process.sequential, # O mapeador termina e passa o bastão para o vendedor
    verbose=True
)

# Execução
if __name__ == "__main__":
    print("### Iniciando Operação Castanhal 300km ###")
    resultado = projeto_estetica.kickoff()
    print("\n\n########################")
    print("## RESULTADO FINAL ##")
    print("########################\n")
    print(resultado)
