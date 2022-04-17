import requests

print("\nElija una de las siguientes opciones:\n1.Planetas\n2.Wookies\n3.Naves\n4.Peliculas\n5.Respuestas")
seleccion = int(input())
if seleccion == 1:
    api_url = "https://swapi.dev/api/planets/?page=2"
    response = requests.get(api_url)
    for i in response:
        print(i)
if seleccion == 2:
    api_url = "https://swapi.dev/api/planets/1/?format=wookiee"
    response = requests.get(api_url)
    for i in response:
        print(i)
if seleccion == 3:
    api_url = "https://swapi.dev/api/starships/"
    response = requests.get(api_url)
    for i in response:
        print(i)

if seleccion == 4:

    primera = "https://swapi.dev/api/films/1",
    segunda = "https://swapi.dev/api/films/2",
    tercera = "https://swapi.dev/api/films/3",
    cuarta = "https://swapi.dev/api/films/4",
    quinta = "https://swapi.dev/api/films/5",
    sexta = "https://swapi.dev/api/films/6"
    print('elija una de las siguientes peliculas:\n1.primera\n2.segunda\n3.tercera\n4.cuarta\n5.quinta\n6.sexta')
    pelicula = int(input())

    if pelicula == 1:
        response = requests.get(primera)
        for i in response:
            print(i)
    if pelicula == 2:
        response = requests.get(segunda)
        for i in response:
            print(i)
    if pelicula == 3:
        response = requests.get(tercera)
        for i in response:
            print(i)
    if pelicula == 4:
        response = requests.get(cuarta)
        for i in response:
            print(i)
    if pelicula == 5:
        response = requests.get(quinta)
        for i in response:
            print(i)
    if pelicula == 6:
        response = requests.get(sexta)
        for i in response:
            print(i)
if seleccion == 5:
    print("existen 2 planetas con terreno desertico\nhabia 400 wookies en la sexta pelicula\nla aeronava mas grande fue el executor")