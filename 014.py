# This application will convert celsius to fahrenheit
temperature = float(input('Enter the celsius temperature: '))
fahrenheit = temperature * 9 / 5 + 32

print('The temperature {:.1f}°C convert to fahrenheit is {:.1f}°F'.format(temperature, fahrenheit))
