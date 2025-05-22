
import pytest
from core.flow_parser import extrair_dados_blocos

@pytest.fixture
def json_exemplo():
    return {
        "flow": {
            "bloco1": {
                "$title": "Início",
                "$conditionOutputs": [
                    {"stateId": "bloco2"},
                    {"stateId": "bloco3"}
                ],
                "$defaultOutput": {"stateId": "bloco2"}
            },
            "bloco2": {
                "$title": "Confirmação",
                "$conditionOutputs": [],
                "$defaultOutput": {"stateId": "bloco3"}
            },
            "bloco3": {
                "$title": "Finalização",
                "$conditionOutputs": [],
                "$defaultOutput": {}
            }
        }
    }

def test_extrair_dados_blocos(json_exemplo):
    df = extrair_dados_blocos(json_exemplo)
    assert df.shape[0] == 3
    assert "Início" in df["titulo"].values
    assert df.iloc[0]["saida_padrao"] == ["bloco2"]
    assert isinstance(df.iloc[0]["titulos_condicoes_saida"], list)
