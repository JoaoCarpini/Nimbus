import logging
from previsao import buscarPrevisao
from regra import avaliarPrevisao

logging.basicConfig(level=logging.INFO)

previsao = buscarPrevisao()
result = avaliarPrevisao(previsao)

for hora in result:
    logging.info(f"{hora['hora']} | {hora['veredicto']}")