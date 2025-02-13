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
st.title("🔍 Analisador de Sentimento")
st.sidebar.title("📝 Entrada de Texto")
frase_usuario = st.sidebar.text_area("Digite sua frase aqui:")

# Histórico de análises
if "historico" not in st.session_state:
    st.session_state.historico = []

if st.sidebar.button("🔎 Analisar Sentimento"):
    if frase_usuario.strip():
        resultado, emoji = analisar_sentimento(frase_usuario)
        st.session_state.historico.append((frase_usuario, resultado, emoji))

        st.subheader("Resultado:")
        st.markdown(f"<h2 style='text-align: center; color: blue;'>{emoji} {resultado}</h2>", unsafe_allow_html=True)

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
