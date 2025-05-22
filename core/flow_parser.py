import pandas as pd

def extrair_dados_blocos(json_data: dict) -> pd.DataFrame:
    blocos = json_data.get("flow", {})
    dados = []

    for bloco_id, bloco in blocos.items():
        titulo = bloco.get("$title", "")
        condicoes = [
            c.get("stateId")
            for c in bloco.get("$conditionOutputs", [])
            if not c.get("$isBuilderDefaultOutput", False)
        ]
        saida_padrao = [bloco.get("$defaultOutput", {}).get("stateId")] if bloco.get("$defaultOutput") else []

        dados.append({
            "bloco_id": bloco_id,
            "titulo": titulo,
            "condicoes_saida": condicoes,
            "saida_padrao": saida_padrao
        })

    df = pd.DataFrame(dados)
    lookup = {row["bloco_id"]: row["titulo"] for row in dados}
    df["titulos_condicoes_saida"] = df["condicoes_saida"].apply(lambda ids: [lookup.get(i, "[Título não encontrado]") for i in ids])
    df["titulos_saida_padrao"] = df["saida_padrao"].apply(lambda ids: [lookup.get(i, "[Título não encontrado]") for i in ids])

    return df
