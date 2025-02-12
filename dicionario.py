import streamlit as st


def analisar_sentimento(frase):
    # Dicionário de palavras positivas e negativas
    palavras_positivas = {"bom", "ótimo", "excelente", "maravilhoso", "feliz", "alegria", "positivo", "sucesso"}
    palavras_negativas = {"ruim", "péssimo", "horrível", "triste", "fracasso", "negativo", "chato", "desastroso"}

    # Separar a frase em palavras
    palavras = frase.lower().split()

    # Contar palavras positivas e negativas
    contagem_positiva = sum(1 for palavra in palavras if palavra in palavras_positivas)
    contagem_negativa = sum(1 for palavra in palavras if palavra in palavras_negativas)

    # Classificação do sentimento
    if contagem_positiva > contagem_negativa:
        return "Sentimento Positivo"
    elif contagem_negativa > contagem_positiva:
        return "Sentimento Negativo"
    else:
        return "Sentimento Neutro"


# Interface Web com Streamlit
st.title("Analisador de Sentimento")
st.write("Digite uma frase para analisar seu sentimento.")

frase_usuario = st.text_input("Frase:")

if st.button("Analisar Sentimento"):
    resultado = analisar_sentimento(frase_usuario)
    st.write(f"Classificação: {resultado}")
