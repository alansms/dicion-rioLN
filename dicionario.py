import streamlit as st
import re
import random
import urllib.parse

# Dicionário de palavras positivas e negativas
palavras_positivas = {"bom", "ótimo", "excelente", "maravilhoso", "feliz", "alegria", "positivo", "sucesso", "incrível",
                      "fantástico", "adorável"}
palavras_negativas = {"ruim", "péssimo", "horrível", "triste", "fracasso", "negativo", "chato", "desastroso",
                      "deprimente", "lamentável"}

# Mensagens motivacionais para sentimentos negativos
mensagens_apoio = [
    "💙 Respire fundo. Você não está sozinho. 💙",
    "🌿 Tente ouvir uma música relaxante e cuidar de você. 🌿",
    "🌟 Lembre-se: dias difíceis passam. Você é mais forte do que imagina. 🌟"
]

# Configuração de cores para realçar emoções
cores = {
    "Muito Positivo": "#D4EDDA",  # Verde claro
    "Positivo": "#C3E6CB",
    "Neutro": "#FFF3CD",  # Amarelo claro
    "Negativo": "#F8D7DA",  # Vermelho claro
    "Muito Negativo": "#F5C6CB"
}


def analisar_sentimento(frase):
    if not frase.strip():
        return "Por favor, insira uma frase válida.", "🧐"

    frase = re.sub(r'[^\w\s]', '', frase.lower())
    palavras = frase.split()

    contagem_positiva = sum(1 for palavra in palavras if palavra in palavras_positivas)
    contagem_negativa = sum(1 for palavra in palavras if palavra in palavras_negativas)

    if contagem_positiva >= 3:
        return "Muito Positivo", "😍"
    elif contagem_positiva > contagem_negativa:
        return "Positivo", "🙂"
    elif contagem_negativa >= 3:
        return "Muito Negativo", "😢"
    elif contagem_negativa > contagem_positiva:
        return "Negativo", "😞"
    else:
        return "Neutro", "😐"


# Interface Web com Streamlit
st.set_page_config(page_title="Sentimento AI - Seu Detector de Emoções", page_icon="💡", layout="wide")

st.markdown(
    """
    <style>
        .big-title {
            font-size: 42px;
            text-align: center;
            color: #4A90E2;
        }
        .sub-title {
            font-size: 22px;
            text-align: center;
            color: #666;
        }
        .result-box {
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
            margin-top: 20px;
            animation: fadeIn 1.5s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='big-title'>🔍 Sentimento AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Seu Detector de Emoções Inteligente 🤖💙</p>", unsafe_allow_html=True)

st.sidebar.title("📝 Entrada de Texto")
frase_usuario = st.sidebar.text_area("Digite sua frase aqui:")

# Histórico de análises
if "historico" not in st.session_state:
    st.session_state.historico = []

if st.sidebar.button("🔎 Analisar Sentimento"):
    if frase_usuario.strip():
        resultado, emoji = analisar_sentimento(frase_usuario)
        st.session_state.historico.append((frase_usuario, resultado, emoji))

        st.markdown(
            f"<div class='result-box' style='background-color: {cores.get(resultado, '#ffffff')};'>{emoji} {resultado}</div>",
            unsafe_allow_html=True)

        # Se o sentimento for negativo, oferecer ajuda emocional
        if "Negativo" in resultado:
            st.warning(
                "💙 Se você estiver se sentindo mal, saiba que você não está sozinho. Procure apoio de amigos, familiares ou profissionais. Você pode entrar em contato com serviços de apoio emocional como o CVV (Centro de Valorização da Vida) pelo telefone 188 ou pelo site [cvv.org.br](https://www.cvv.org.br/). 💙")
            st.info(random.choice(mensagens_apoio))

        # Gerar link para compartilhamento
        url_compartilhar = f"https://twitter.com/intent/tweet?text={urllib.parse.quote(f'Analisei meu sentimento e deu: {resultado}! 😀 #SentimentoAI')}"
        st.markdown(f"[📢 Compartilhe no Twitter]({url_compartilhar})", unsafe_allow_html=True)

        # Exibir histórico
        st.subheader("📜 Histórico de Sentimentos")
        for frase, sentimento, icon in reversed(st.session_state.historico[-5:]):
            st.write(f"{icon} **{frase}** → {sentimento}")
    else:
        st.warning("⚠️ Digite um texto para análise.")
