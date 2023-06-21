import requests

def get_data(lat, lon, forecast_days = None, kind = None):
    api_key = "bb5dc40bff5a8078f2b814f9edfc1146"
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data



if __name__ == "__main__":
    print(get_data(12.0282,12.0842323))