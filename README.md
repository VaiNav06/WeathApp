# WeathApp

Weather App

A simple weather application using Tkinter and the OpenWeatherMap API. Enter a city name to get real-time weather details, including temperature, wind speed, and sunrise/sunset times.

Installation
1.	Clone the repository:

		git clone https://github.com/VaiNav06/WeathApp
	cd weather-app


2.	Install the required package:

		pip install requests


3.	Run the application:

		python weather.py



Usage
	•	Open the app
	•	Enter a city name
	•	Press Enter to get weather details

API Key

This app uses the OpenWeatherMap API. Replace the API key in the script with your own:

api = "http://api.openweathermap.org/data/2.5/weather?q=" + LOCATION + "&appid=YOUR_API_KEY"

