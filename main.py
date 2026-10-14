import logging
import time
import requests
from previsao import buscarPrevisao
from regra import avaliarPrevisao

logging.basicConfig(level=logging.INFO)

falhas_seguidas = 0
cont_rodadas = 0
while True:
    try:
        previsao = buscarPrevisao()
        result = avaliarPrevisao(previsao)
        for hora in result:
            logging.info(f"{hora['hora']} | {hora['veredicto']}")

        falhas_seguidas = 0
        cont_rodadas = 0
        time.sleep(30 * 60)

    except requests.RequestException as erro:
        falhas_seguidas += 1
        logging.error(f"Não consegui obter a previsao: {erro}")

        if falhas_seguidas == 5:
            falhas_seguidas = 0
            cont_rodadas += 1

            if cont_rodadas == 6:
                logging.error(f"Desistência de busca: {erro}")
                cont_rodadas = 0
                time.sleep(30 * 60)
            else:
                time.sleep(600)
        else:
            time.sleep(10)