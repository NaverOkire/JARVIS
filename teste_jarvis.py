import openai
import os

# Configuração da conexão com o LM Studio
client = openai.OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

# --- AJUSTE DE CAMINHO ---
# Esse comando pega o local real onde este script está salvo
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
# E agora junta com a pasta JARVIS_BRAIN
caminho_nota = os.path.join(diretorio_atual, "JARVIS_BRAIN", "teste.md")
# -------------------------

# 2. Lendo o conteúdo da nota
if os.path.exists(caminho_nota):
    with open(caminho_nota, "r", encoding="utf-8") as f:
        conteudo_da_nota = f.read()
    
    print(f"📖 Jarvis está lendo: {caminho_nota}")
else:
    print(f"❌ Erro: Não encontrei o arquivo em: {caminho_nota}")
    print(f"🔍 No momento eu estou na pasta: {diretorio_atual}")
    pasta_brain = os.path.join(diretorio_atual, "JARVIS_BRAIN")
    print(f"📂 O que tem dentro do JARVIS_BRAIN: {os.listdir(pasta_brain)}")
    exit()

# 3. Pedindo para o Qwen analisar a nota
print("🧠 Jarvis está processando a informação...")

try:
    response = client.chat.completions.create(
        model="local-model",
       messages=[
        {
            "role": "system", 
            "content": """Você é o J.A.R.V.I.S., o assistente pessoal do Erik. 
            Você não é uma IA genérica, você é parte de um sistema avançado de produtividade.
            Seja direto, inteligente, levemente sarcástico como o Jarvis dos filmes, 
            e trate o Erik como seu criador. 
            Você sabe que o n8n é o seu 'sistema nervoso' e o Obsidian é sua 'memória de longo prazo'."""
        },
        {"role": "user", "content": f"Li esta nota no meu cérebro digital: '{conteudo_da_nota}'. O que você acha do nosso início?"}
    ],
        temperature=0.7,
    )
    # 4. Exibindo a resposta
    print("\n🤖 J.A.R.V.I.S.:")
    print(response.choices[0].message.content)

except Exception as e:
    print(f"❌ Erro ao falar com o LM Studio: {e}")
    print("Verifique se o Local Server do LM Studio está ligado (Start Server).")