import requests 
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
print("Welcome to the Mini Weather app : ")
city=input("Enter the name of your city :\n ")
url=f"http://api.weatherapi.com/v1/current.json?key=6205b9c76a904096844193357231305&q={city}"
r=requests.get(url)
weatherdict=json.loads(r.text)
w=weatherdict["current"]["temp_c"]
speak.Speak(f"The current weather in {city} is {w} degrees")
