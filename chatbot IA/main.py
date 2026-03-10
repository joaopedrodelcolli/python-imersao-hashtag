# titulo
# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar
    # mostrar a mensagem que o usuário enviou no chat
    # pegar a mensagem e enviar para uma IA responder
    # exibir a resposta da IA na tela

# Streamlit -> apenas com Python criar o frontedn e o backend
# a IA que vamos usar: OpenAI
# pip install openai streamlit

import streamlit as st
from openai import OpenAI

modelo_ia = OpenAI(api_key="sk-xxxx")

st.write("# Chatbot com IA") # markdwon

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []



texto_usuario = st.chat_input("Digite sua mensagem")

# role = quem é o usuário (user ou assistant)
# content = conteúdo da mensagem

for mensagem in ["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    
    st.chat_message(role).write(content)

if texto_usuario:
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # user
    # assistant
    
    # ia respondeu
    resposta_ia = modelo_ia.chat.completions.create(
        messages=st.session_state["lista_mensagens"],
        model = "gpt-4o"
    )
    texto_resposta_ia = resposta_ia.choices[0].message.content


    st.chat_message("assistant").write(texto_resposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)

