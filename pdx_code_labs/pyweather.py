import requests
question = input('Would you like to search by (c)ity or (z)ip?: ')
city = input('What city or zip are you looking for?: ')
package = {
    'APPID': 'b33478fac3dbac4a05f1b2809df804af',
}

if question == 'c':
    package['q'] = city
else:
    package['zip'] = city

r = requests.post('http://api.openweathermap.org/data/2.5/weather', params=package)

data = r.json()
print(data['name'])
print("Your city's temperature: ", data['main']['temp'], "Kelvin")

temperature_conversion = input("Would you like your temperature converted to (f)ahrenheit or (c)elsius?: ")

kelvin_temp = data['main']['temp']
fahrenheit_conversion = (kelvin_temp * 9 / 5 - 459.67 )
celsius_conversion = (kelvin_temp - 273.15)

if temperature_conversion == 'f':
    print(fahrenheit_conversion, 'Fahrenheit')
if temperature_conversion == 'c':
    print(celsius_conversion, 'Celsius')

final_menu = input("Would you like to return to the temperature conversion options [y/n]?")

if final_menu == 'y':
    print(temperature_conversion)
if final_menu == 'n':`
    print("Thank you. Goodbye!")
