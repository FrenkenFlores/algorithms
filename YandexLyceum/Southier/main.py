import requests


TOKEN = "40d1649f-0493-4b70-98ba-98533de7710b&geocode"


def main():
    cities = input().split(',')
    latitudes = []
    for city in cities:
        geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey={TOKEN}={city}&format=json"
        response = requests.get(geocoder_request)

        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"][
            "featureMember"][0]["GeoObject"]
        pos = toponym['Point']['pos']
        latitudes.append((city, pos.split()[1]))

    latitudes.sort(key=lambda x: float(x[1]))
    print(latitudes[0][0])


if __name__ == "__main__":
    main()
