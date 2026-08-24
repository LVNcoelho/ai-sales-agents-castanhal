# 🤖 ai-sales-agents-castanhal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-orange?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-blueviolet?style=for-the-badge&logo=openai)

Meu primeiro projeto explorando como a inteligência artificial pode sobrecarregar positivamente o setor comercial de pequenas e médias empresas regionais.

Este projeto utiliza **Multi-Agent Systems (CrewAI)** para automatizar todo o pipeline de prospecção e vendas B2B para empresas distribuidoras e comércios no polo de Castanhal - Pará e região (cobrindo um raio de atuação de até 300 km).

---

## 📐 Fluxo de Funcionamento (Arquitetura dos Agentes)

```mermaid
graph TD
    A[📍 Entrada: Região & Nicho Target] --> B[🔍 SDR Agent]
    B -->|Mineração e Qualificação de Leads| C[🧠 Análise de Gargalos & Dores]
    C --> D[✍️ Sales Copywriter Agent]
    D -->|Geração de E-mail Personalizado| E[📩 Cadência de Abordagem B2B]

    📋 Cenário e Desafio
A empresa possuía um processo de prospecção 100% manual, lento e dependente de abordagens genéricas por WhatsApp. O desafio era identificar distribuidoras e lojas em polos estratégicos (como Belém, Capanema, Paragominas e Castanhal) e realizar abordagens hiper-personalizadas em escala.

🛠️ A Solução Implementada
Implementei uma equipe de agentes autonômos de IA orquestrados para trabalhar em sequência:

🔍 SDR Agent (Search & Prospecting): Minera dados geográficos, identifica gargalos técnicos e operacionais de empresas locais e qualifica alvos prioritários em um raio de 300km.

✍️ Sales Copywriter Agent: Analisa os gargalos específicos de cada empresa (ex: dependência de atendimento manual, falta de CRM ou problemas de estoque) e redige abordagens comerciais personalizadas mantendo o tom de voz e contexto regional.

💻 Exemplo de Saída Gerada pelos Agentes

[SDR Agent - Lead Qualificado]
Empresa: Distribuidora de Cosméticos em Castanhal/PA
Gargalo Identificado: Atendimento 100% manual no WhatsApp em picos de demanda.

[Sales Copywriter Agent - Output]
Assunto: Eficiência no atendimento da [Nome da Empresa] em Castanhal

Olá, equipe da [Nome da Empresa]!

Acompanho a forte presença de vocês no fornecimento para salões em Castanhal e região. 
Percebi que o volume de pedidos via WhatsApp no horário de pico costuma ser alto, o que pode sobrecarregar a equipe e atrasar confirmações de estoque.

Desenvolvemos uma solução de IA que automatiza a triagem inicial desses pedidos e conecta direto ao seu controle interno, sem perder o tom humano do atendimento.

Teria 10 minutos nesta quinta-feira para vermos como reduzir esse tempo de resposta a zero?


🛠️ Tecnologias Utilizadas
Python 3.10+

CrewAI (Orquestração de Agentes Multi-tarefas)

LangChain / OpenAI (Inteligência e raciocínio dos modelos)

OSM & Web Scraping Utilities (Extração de dados geográficos e comerciais)
