
---

# 🧠 Projeto JARVIS (v0.2 Beta)

**Status do Projeto:** 🛠️ **Funcional / Em Fase de Testes** O sistema já se encontra operacional e capaz de responder interações. A arquitetura básica está consolidada, incluindo a integração com interfaces externas. No entanto, o sistema ainda passa por baterias de testes intensivas para validar a precisão total do motor RAG.

---

## 📋 Sobre o Projeto
O **JARVIS** é uma iniciativa focada em ampliar as capacidades de Modelos de Linguagem (LLMs) locais com baixa contagem de parâmetros. O objetivo central é fornecer a essas IAs um "cérebro" externo de conhecimento especializado, permitindo que modelos leves entreguem precisão comparável a modelos de grande porte em tarefas específicas e nichadas.

O projeto utiliza uma arquitetura de **Geração Aumentada por Recuperação (RAG)** para mitigar alucinações e fornecer contexto dinâmico a modelos que, de outra forma, teriam conhecimento limitado.

---

### 🏗️ Arquitetura do Sistema
O ecossistema é integrado por quatro componentes principais que trabalham em simbiose:

* **O Cérebro (Obsidian):** Biblioteca de notas em Markdown que atua como a base de dados de longo prazo e fonte de verdade do sistema.
* **O Sistema Nervoso (n8n via Docker):** O orquestrador central que gerencia o fluxo de dados, realiza a lógica de busca e conecta todas as pontas.
* **A Voz / Interface (Discord Bot):** Porta de entrada e saída para comandos remotos, permitindo a interação com o sistema de qualquer lugar via chat.
* **O Motor de Processamento (LM Studio):** Responsável por hospedar e executar os modelos locais (LLMs), processando as requisições via API local.

---

### 🛠️ Tecnologias Utilizadas
* **LM Studio:** Execução de modelos locais em formato GGUF.
* **Obsidian:** Gestão de conhecimento e armazenamento de contexto estruturado.
* **n8n:** Automação de workflow baseada em nós para orquestração técnica.
* **Docker:** Ambiente de conteinerização para o n8n e serviços auxiliares.
* **Discord API:** Interface de usuário para comunicação e logs de resposta.

---

### 🚀 Como Funciona
1.  O usuário envia uma mensagem ou comando através do bot no **Discord**.
2.  O **n8n** captura a entrada e inicia o processo de recuperação de dados no **Obsidian**.
3.  O sistema busca notas relevantes para o tema, criando um pacote de contexto.
4.  Este contexto é injetado no prompt e enviado ao **LM Studio**.
5.  A IA processa a informação e a resposta final é entregue diretamente no canal do **Discord**.

---

### 🧪 Status dos Testes
* **Interface Discord:** ✅ Operacional.
* **Fluxo de Dados n8n:** ✅ Operacional e estável.
* **Processamento Local:** ✅ Operacional.
* **Precisão do RAG:** ⚠️ **Em avaliação**. Testes em progresso para garantir que a recuperação de informação do Obsidian seja 100% assertiva e relevante antes da versão final.

---

## 📄 Licença
Este projeto é de código aberto sob a licença MIT. Sinta-se à vontade para contribuir com melhorias durante esta fase de maturação.
---
