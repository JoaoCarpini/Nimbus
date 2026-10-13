import logging
import time
from previsao import buscarPrevisao
from regra import avaliarPrevisao

logging.basicConfig(level=logging.INFO)

while True:
    previsao = buscarPrevisao()
    result = avaliarPrevisao(previsao)

    for hora in result:
        logging.info(f"{hora['hora']} | {hora['veredicto']}")

    time.sleep(30 * 60)