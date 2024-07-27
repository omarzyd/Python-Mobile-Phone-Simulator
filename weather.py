import tkinter as tk
from tkinter import simpledialog, messagebox
import requests

def geting_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def convert_kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def suggest_what_to_wear(temperature):
    if temperature < 10:
        return "Wear a heavy coat, hat, gloves, and boots."
    elif 10 <= temperature < 20:
        return "You might consider wearing a light sweater, a long-sleeved shirt, or a comfortable hoodie."
    else:
        return "Dress lightly."

def suggest_the_activities(weather_description):
    if "rain" in weather_description.lower():
        return "Consider indoor activities or bring an umbrella."
    elif "snow" in weather_description.lower():
        return "Enjoy winter sports or build a snowman."
    else:
        return "Explore outdoor activities like hiking or cycling."

def display_weather_info(weather_data):
    temperature = convert_kelvin_to_celsius(weather_data['main']['temp'])
    weather_description = weather_data['weather'][0]['description']
    info = (
        f"Weather: {weather_description.capitalize()}\n"
        f"Temperature: {temperature:.2f}°C\n"
        f"Humidity: {weather_data['main']['humidity']}%"
    )
    messagebox.showinfo("Weather Info", info)

def weather_menu():
    root = tk.Tk()
    root.title("Weather")

    def check_weather():
        api_key = "534325d698a0f7f1bbeed1a09bb6b8af"  # Replace with your actual API key
        city = simpledialog.askstring("Input", "Enter the city name:")
        weather_data = geting_weather(api_key, city)
        if weather_data['cod'] == '404':
            messagebox.showerror("Error", "City not found. Please check the spelling.")
        else:
            display_weather_info(weather_data)
            clothing_suggestion = suggest_what_to_wear(convert_kelvin_to_celsius(weather_data['main']['temp']))
            activities_suggestion = suggest_the_activities(weather_data['weather'][0]['description'])
            suggestions = f"Clothing: {clothing_suggestion}\nActivities: {activities_suggestion}"
            messagebox.showinfo("Suggestions", suggestions)

    tk.Button(root, text="Check Weather", command=check_weather, width=20).pack(pady=10)
    tk.Button(root, text="Quit", command=root.quit, width=20).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    weather_menu()
