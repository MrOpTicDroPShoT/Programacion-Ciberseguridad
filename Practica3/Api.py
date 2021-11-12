import requests, json, datetime, math
def get_weather():
    APIkey = "b12cdd9192527ebede621c86a32c3152"
    while True:
        #a=(str(input(("Introduzca la ciudad para ver el clima\n"
        #    "Ciudades disponibles:\n"
        #    "Monterrey\n"
        #    "Guadalajara\n"
        #    "Torreon\n"
        #    "Queretaro\n"))))
        #a=a.lower()
        a="monterrey"
        if a!="monterrey" and a!="guadalajara" and a!="torreon" and a!="queretaro":
            True
        elif a=="monterrey":
            lat = "25.66667"
            lon = "-100.316673"
            break
        elif a=="guadalajara":
            lat = "20.66667"
            lon = "-103.333328"
            break
        elif a=="torreon":
            lat = "25.549999"
            lon = "-103.433327"
            break
        elif a=="queretaro":
            lat = "20.6"
            lon = "-100.383331"
            break
    #url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&units=metric&exclude=minutely,hourly,alerts,daily&appid={APIkey}&lang=sp"
    cityname="Monterrey"
    cnt=10
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={APIkey}"

    response = requests.get(url)
    data = json.loads(response.content)
    print(data)
    print("Las condiciones climatologicas son: ", data["weather"][0]["main"])
    print("Descripcion: ", data["weather"][0]["description"])
    grados=int((data["main"]["temp"])-273.15)
    print("La temperatura es: ", grados)
    sensacion = int((data["main"]["feels_like"]) - 273.15)
    print("Sensasion de temperatura: ", sensacion)
    temp_max = int((data["main"]["temp_max"]) - 273.15)
    print("Temperatura maxima: ", temp_max)
    temp_min = int((data["main"]["temp_min"]) - 273.15)
    print("Temperatura minima: ", temp_min)
    print("Humedad: %", data["main"]["humidity"])
    print("Presion atmosferica", data["main"]["pressure"])


get_weather()