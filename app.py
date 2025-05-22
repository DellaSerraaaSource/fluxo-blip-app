import streamlit as st
import json
import os
import streamlit.components.v1 as components
from core.flow_parser import extrair_dados_blocos
from core.graph_generator import gerar_grafo_html

st.set_page_config(layout="wide")
st.title("🔁 Visualizador de Fluxo BLiP")

arquivo = st.file_uploader("Faça upload do JSON de fluxo exportado do BLiP", type=["json"])

if arquivo:
    fluxo_json = json.load(arquivo)
    df_blocos = extrair_dados_blocos(fluxo_json)

    titulos = df_blocos["titulo"].tolist()
    bloco_escolhido = st.selectbox("Selecione um bloco para visualizar o grafo:", titulos)

    grafo_path = gerar_grafo_html(df_blocos, bloco_escolhido)
    with open(grafo_path, "r", encoding="utf-8") as f:
        components.html(f.read(), height=600, scrolling=True)
    os.remove(grafo_path)
