from pyvis.network import Network
from core.constants import ALTURA_GRAFO, COR_BLOCO_ATUAL, COR_CONDICIONAL, COR_PADRAO
import tempfile

def gerar_grafo_html(df, titulo_bloco: str) -> str:
    bloco = df[df["titulo"] == titulo_bloco].iloc[0]
    net = Network(height=ALTURA_GRAFO, width="100%", directed=True)
    net.barnes_hut()

    net.add_node(titulo_bloco, label=titulo_bloco, color=COR_BLOCO_ATUAL)

    for destino in bloco["titulos_condicoes_saida"]:
        net.add_node(destino, label=destino, color=COR_CONDICIONAL)
        net.add_edge(titulo_bloco, destino, color="blue")

    for destino in bloco["titulos_saida_padrao"]:
        net.add_node(destino, label=destino, color=COR_PADRAO)
        net.add_edge(titulo_bloco, destino, color="red")

    temp_path = tempfile.NamedTemporaryFile(delete=False, suffix=".html")
    net.save_graph(temp_path.name)
    return temp_path.name
