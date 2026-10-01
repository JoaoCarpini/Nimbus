import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=-21.85&longitude=-47.48&hourly=apparent_temperature,precipitation_probability,uv_index&forecast_days=7&timezone=America/Sao_Paulo"

def buscarPrevisao():
    request = requests.get(url)
    hourly = request.json()["hourly"]

    hours = []

    for i in range(len(hourly["time"])):
        time = hourly["time"][i]
        temperature = hourly["apparent_temperature"][i]
        uv_index = hourly["uv_index"][i]
        precipitation_probability = hourly["precipitation_probability"][i]

        hours.append({
            "hora": time,
            "temperatura": temperature,
            "uv": uv_index,
            "precipitacao": precipitation_probability
        })

    return hours