import requests
url = 'https://api.openweathermap.org/data/2.5/weather?lat=35.6894&lon=139.6917&appid=0e669b6386ca3a2d8c720e823df0520c'

class Weather():
  def __init__(self, url):
    self.url = url

  def fetch_api(url):
    res = requests.get(url)
    data = res.json()
    return data

  def feels_like(json_data):
    temp = json_data['main']
    return temp['feels_like']

  def weather(json_data):
    return json_data['weather']
  
  
