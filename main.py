import subprocess
from show_cpu_temperature import LCD
from weather import Weather
import time
def main():
  url = 'https://api.openweathermap.org/data/2.5/weather?lat=35.6894&lon=139.6917&appid=0e669b6386ca3a2d8c720e823df0520c'
  lcd = LCD()
  weather = Weather(url)
  lcd.LCDinit()
  while 1:
    lcd.command(lcd.clear)
    data = weather.fetch_api()
    weather_data = weather.weather(data)
    temp = weather.feels_like(data)
    lcd.writeLCD("Weather: ")
    lcd.writeLCD(weather_data)
    lcd.command(lcd.LCD_2ndline)
    lcd.writeLCD("Temp: ")
    lcd.writeLCD(str(temp))


    time.sleep(60)

if __name__ == '__main__':
  main()
