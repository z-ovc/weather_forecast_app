import requests
from config import my_api_key

def get_data(lat, lon, forecast_days = None):
    api_key = my_api_key
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data



if __name__ == "__main__":
    data = get_data(12.0282,12.0842323,forecast_days = 3)
    print(data)
