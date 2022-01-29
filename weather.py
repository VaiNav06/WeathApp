import requests
import tkinter as tk
import time

def getWeather(board):
    
    LOCATION = textField.get()
    api = "http://api.openweathermap.org/data/2.5/weather?q=" + LOCATION +"&appid=ea79cc9cf865424aceb0b0cc07bf7572"

    json_data = requests.get(api).json()
    CONDITION = json_data['weather'][0]['main']
    TEMP = int(json_data['main']['temp'] - 273.15)
    SUNRISE = time.strftime('%I : %M : %S' ,time.gmtime(json_data['sys']['sunrise'] - 21600))
    SUNSET = time.strftime('%I : %M : %S' ,time.gmtime(json_data['sys']['sunset'] - 21600))
    MIN_TEMP = int(json_data['main']['temp_min'] - 273.15)
    MAX_TEMP = int(json_data['main']['temp_max'] - 273.15)
    WIND = json_data['wind']['speed']
    

    info = CONDITION + "\n" + str(TEMP) + "°C"
    data = "\n" + "Max Temp: " + str( MAX_TEMP) + "°C" + "\n" + "Min Temp: " + str( MAX_TEMP) + "°C" +"\n"  + "Wind Speed :" + str(WIND) +"\n" + "Sunrise : " + SUNRISE + "\n" + "Sunset : " + SUNSET
    label1.config(text = info)
    label2.config(text = data)

board = tk.Tk()
board.geometry("700x800")
board.title("Weather App")

f1 = ("poppins", 15, "bold")
f2 = ("poppins", 35, "bold")

textField = tk.Entry(board, font = f2)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(board, font = f2)
label1.pack()
label2 = tk.Label(board, font = f1)
label2.pack()

board.mainloop()


