import requests

class Weather():
  def __init__(self, url):
    self.url = url

  def fetch_api(self):
    res = requests.get(self.url)
    data = res.json()
    return data

  def feels_like(self, json_data):
    temp = json_data['main']
    return self.convert_temp(temp['feels_like'])

  def weather(self, json_data):
    weather = json_data['weather'][0]
    return weather['main']

  def convert_temp(self, temp):
    return temp - 273
  
  
