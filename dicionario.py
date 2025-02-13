import streamlit as st
import re  # Mantendo re para limpeza da string


def analisar_sentimento(frase):
    # Dicionário de palavras positivas e negativas
    palavras_positivas = {"bom", "ótimo", "excelente", "maravilhoso", "feliz", "alegria", "positivo", "sucesso"}
    palavras_negativas = {"ruim", "péssimo", "horrível", "triste", "fracasso", "negativo", "chato", "desastroso"}

    # Verifica se a frase não está vazia
    if not frase.strip():
        return "Por favor, insira uma frase válida.", "🧐"

    # Remover pontuação e converter para minúsculas
    frase = re.sub(r'[^\w\s]', '', frase.lower())  # Corrigido para usar apenas re

    # Separar a frase em palavras
    palavras = frase.split()

    # Contar palavras positivas e negativas
    contagem_positiva = sum(1 for palavra in palavras if palavra in palavras_positivas)
    contagem_negativa = sum(1 for palavra in palavras if palavra in palavras_negativas)

    # Classificação do sentimento
    if contagem_positiva > contagem_negativa:
        return "Sentimento Positivo", "😀"
    elif contagem_negativa > contagem_positiva:
        return "Sentimento Negativo", "😞"
    else:
        return "Sentimento Neutro", "😐"


# Interface Web com Streamlit
st.title("🔍 Analisador de Sentimento")
st.write("Digite uma frase para analisar seu sentimento.")

# Entrada do usuário
frase_usuario = st.text_input("Digite sua frase aqui:")

# Analisar sentimento ao clicar no botão
if st.button("🔎 Analisar Sentimento"):
    if frase_usuario.strip():  # Garante que a entrada não está vazia
        resultado, emoji = analisar_sentimento(frase_usuario)
        st.subheader("Resultado:")
        st.markdown(f"### {emoji} {resultado}")  # Melhor exibição da resposta

        # Se o sentimento for negativo, oferecer ajuda emocional
        if resultado == "Sentimento Negativo":
            st.warning(
                "💙 Se você estiver se sentindo mal, saiba que você não está sozinho. Procure apoio de amigos, familiares ou profissionais. Você pode entrar em contato com serviços de apoio emocional como o CVV (Centro de Valorização da Vida) pelo telefone 188 ou pelo site [cvv.org.br](https://www.cvv.org.br/). 💙")
    else:
        st.warning("⚠️ Digite um texto para análise.")  # Exibe alerta visual no Streamlit
