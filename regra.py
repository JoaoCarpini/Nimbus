def avaliar_hora(hora):
    corte = hora["hora"][11:13]
    numero = int(corte)

    if numero < 5 or numero > 20:
        return "fora de janela"
    if hora['precipitacao'] >= 50:
        return 'ruim, precipitação alta'
    if hora['uv'] >= 6:
        return 'ruim, uv alto'
    if hora['temperatura'] >= 33:
        return 'ruim, temperatura alta'
    return 'bom'

def avaliarPrevisao(hours):
    veredict = []

    for hour in hours:
        result = avaliar_hora(hour)
        veredict.append({
            "hora": hour["hora"],
            "veredicto": result
        })

    return veredict

if __name__ == "__main__":
    teste = [
        {"hora": "2026-10-01T07:00", "temperatura": 25.0, "uv": 1.0, "precipitacao": 10},
        {"hora": "2026-10-01T14:00", "temperatura": 34.0, "uv": 8.0, "precipitacao": 0},
        {"hora": "2026-10-01T03:00", "temperatura": 20.0, "uv": 0.0, "precipitacao": 0}
    ]
    print(avaliarPrevisao(teste))