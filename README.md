# 🤖 ai-sales-agents-castanhal

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![CrewAI](https://img.shields.io/badge/CrewAI-Orchestration-orange?style=for-the-badge)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-blueviolet?style=for-the-badge&logo=openai)
![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)

> Automação inteligente de prospecção B2B e geração de abordagens hiper-personalizadas focada no polo comercial de Castanhal e região.

---

## 📌 Sobre o Projeto

Este projeto utiliza **Sistemas Multi-Agentes (CrewAI)** para automatizar todo o pipeline de prospecção e vendas B2B para distribuidoras, indústrias e comércios no polo econômico de **Castanhal - Pará** e cidades num raio de até 300 km (Belém, Capanema, Paragominas, Abaetetuba, entre outras).

### 📋 Cenário e Desafio
Empresas locais costumam utilizar um processo de prospecção 100% manual, lento e dependente de abordagens genéricas ("frias") via WhatsApp ou e-mail. O desafio deste software é identificar alvos comerciais estratégicos e gerar mensagens de alta conversão, contextualizadas com a realidade do mercado paraense.

---

## 📐 Fluxo de Funcionamento (Arquitetura dos Agentes)

* 📍 **Entrada:** Região e Nicho Target
* 🔍 **SDR Agent:** Mineração, Scraping e Qualificação de Leads
* 🧠 **Análise de Dores:** Mapeamento de Gargalos Comerciais e Operacionais
* ✍️ **Sales Copywriter Agent:** Geração do Cold Mail/Pitch Personalizado
* 🚀 **Saída:** Cadência de Abordagem B2B Pronta para Disparo

---

## 🛠️ A Solução Implementada

A aplicação utiliza uma equipe de agentes autônomos de IA orquestrados em sequência:

1. **🔍 SDR Agent (Search & Prospecting):**
   * Extrai e minera dados comerciais geográficos.
   * Identifica potenciais gargalos operacionais (ex: atendimento lento, falta de automação, ausência de e-commerce).
   * Qualifica os leads prioritários da região.

2. **✍️ Sales Copywriter Agent:**
   * Analisa as dores específicas extraídas pelo SDR Agent.
   * Redige e-mails e abordagens comerciais personalizadas mantendo o contexto e o tom de voz do mercado regional.

---

## 💻 Exemplo de Entrada e Saída

**[SDR Agent - Lead Qualificado]**
* **Empresa:** Distribuidora de Cosméticos em Castanhal/PA
* **Gargalo Identificado:** Atendimento 100% manual no WhatsApp em horários de pico.

**[Sales Copywriter Agent - Output]**
> **Assunto:** Eficiência no atendimento da [Nome da Empresa] em Castanhal
>
> Olá, equipe da [Nome da Empresa]!
>
> Acompanho a forte presença de vocês no fornecimento para salões em Castanhal e região. 
> Percebi que o volume de pedidos via WhatsApp no horário de pico costuma ser alto, o que pode sobrecarregar a equipe e atrasar confirmações de estoque.
>
> Desenvolvemos uma solução de IA que automatiza a triagem inicial desses pedidos e conecta direto ao seu controle interno, sem perder o tom humano do atendimento.
>
> Teria 10 minutos nesta quinta-feira para vermos como reduzir esse tempo de resposta a zero?

---

## 🛠️ Tecnologias Utilizadas

* **Python 3.10+** — Linguagem base do sistema.
* **CrewAI** — Framework para orquestração de agentes autônomos multi-tarefas.
* **LangChain / OpenAI (GPT-4 / GPT-3.5-turbo)** — LLMs e motores de raciocínio.
* **OSM & Web Scraping Utilities (Selenium / BeautifulSoup)** — Utilitários para extração de dados geográficos e comerciais.
* **python-dotenv** — Gerenciamento seguro de variáveis de ambiente.

---

## 📊 Impacto e Resultados (KPIs)

* ⚡ **Automação Integral:** O tempo gasto com pesquisa e qualificação de leads foi reduzido a zero.
* 🎯 **Alta Conversão:** A personalização contextual via IA gerou um volume de leads qualificados sem precedentes para a região.
* 🚀 **Gargalo de Sucesso:** A demanda gerada pelos agentes excedeu a capacidade operacional inicial da equipe comercial, demonstrando a força de escalar o topo do funil com IA.

---

## 📝 Licença

Este projeto está sob a licença [MIT](./LICENSE).
