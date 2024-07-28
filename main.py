import requests
from twilio.rest import Client
parameters = {
    "lon": 13.404954,
    "lat": 52.520008,
    "appid": "727f8709b33885c2e647c77c812ca0c5",
    "cnt": 4
}
account_sid = "ACe38853c6b1267e1ce61ed81b32fb4ca3"
auth_token = "03ec402f79894bff437c0bebb06da435"
client = Client(account_sid, auth_token)
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
list_of_IDs = [weather["weather"][0]["id"] for weather in weather_data["list"]]
for ID in list_of_IDs:
    if ID < 700:
        message = client.messages.create(
            body="It is going to be raining in the next 12 hours. Bring an umbrella with you.",
            from_="whatsapp:+14155238886",
            to="whatsapp:+4917689183516",
        )
        break
