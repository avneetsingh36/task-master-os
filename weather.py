import requests

def getWeather():
    cityName = input("\nEnter the city name: ")
    print()
    print(f"Displaying Weather Report for: {cityName.upper()}")
    print()

    url = 'https://wttr.in/{}'.format(cityName.upper())
    res = requests.get(url)

    print(res.text)
    print()

    goAgainWeather = input("Would you like to try getting weather for another city (y/n): ")

    if goAgainWeather.lower() == "y":
        print('\n\n\n')
        getWeather()
    else:
        print("\nOkay, what would you like to do next?\n")
