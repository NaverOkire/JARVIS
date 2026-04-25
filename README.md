# 🧠 Projeto JARVIS (Alpha)
Status do Projeto: ⚠️ Versão de Testes / Experimental
Este projeto está em fase inicial de desenvolvimento. Funcionalidades podem apresentar instabilidades e a arquitetura está sujeita a mudanças frequentes.

---

## 📋 Sobre o Projeto
O JARVIS é uma iniciativa focada em ampliar as capacidades de Modelos de Linguagem (LLMs) locais com baixa contagem de parâmetros. O objetivo central é fornecer a essas IAs um "cérebro" externo de conhecimento especializado, permitindo que modelos leves entreguem precisão comparável a modelos de grande porte em tarefas específicas e nichadas.

A ideia é mitigar as alucinações e a falta de contexto de modelos menores através de uma arquitetura de recuperação de informações eficiente.

---

### 🏗️ Arquitetura do Sistema
O projeto é construído sobre três pilares fundamentais:

O Cérebro (Obsidian): Uma biblioteca de notas em Markdown que serve como a base de conhecimento estruturada e rica em contexto.

O Sistema Nervoso (n8n via Docker): Atua como o motor de orquestração e fluxo de dados, conectando as solicitações do usuário à base de conhecimento e ao modelo de IA.

O Motor de Processamento (LM Studio): Responsável por rodar as IAs locais de forma eficiente, expondo uma API local para comunicação.

---

### 🛠️ Tecnologias Utilizadas
LM Studio: Interface para execução de LLMs locais (GGUF).

Obsidian: Gestão de conhecimento e armazenamento de dados contextuais.

n8n: Automação de fluxo de trabalho baseada em nós.

Docker: Conteinerização para garantir um ambiente de execução estável para o sistema nervoso.

---

### 🚀 Como Funciona
O n8n recebe a entrada do usuário.

O sistema realiza uma busca no Obsidian para encontrar informações relevantes sobre o tema solicitado.

O contexto recuperado é injetado em um prompt otimizado.

O LM Studio processa o prompt usando o modelo local e gera uma resposta baseada nos dados reais fornecidos, e não apenas em seu treinamento prévio.

---


## 📄 Licença
Este projeto é de código aberto sob a licença MIT. Sinta-se à vontade para contribuir com melhorias durante esta fase de testes.
