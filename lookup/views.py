# Views
from django.shortcuts import render


# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=71BC600B-FFD8-4FF6-99A8-36871C82A528
from requests import Response


def home(request):
    import json
    import requests


    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request: Response = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+ zipcode +"&distance=25&API_KEY=71BC600B-FFD8-4FF6-99A8-36871C82A528")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"

        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
            category_description = "0 to 50	Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
            category_description = '51 to 100	Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
            category_description = "101 to 150	Members of sensitive groups may experience health effects. The general public is not likely to be affected."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
            category_description = "151 to 200	Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description = "201 to 300	Health alert: everyone may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
            category_description = "301 to 500	Health warnings of emergency conditions. The entire population is more likely to be affected."
        return render(request, 'home.html',
                      {'api': api, 'category_description': category_description, 'category_color': category_color})
    else:
        api_request: Response = requests.get(
            "http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=71BC600B-FFD8-4FF6-99A8-36871C82A528")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."
        if api[0]['Category']['Name'] == "Good":
            category_color = "good"
            category_description = "0 to 50	Air quality is considered satisfactory, and air pollution poses little or no risk."
        elif api[0]['Category']['Name'] == "Moderate":
            category_color = "moderate"
            category_description = '51 to 100	Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.'
        elif api[0]['Category']['Name'] == "Unhealthy for Sensitive Groups":
            category_color = "usg"
            category_description = "101 to 150	Members of sensitive groups may experience health effects. The general public is not likely to be affected."
        elif api[0]['Category']['Name'] == "Unhealthy":
            category_color = "unhealthy"
            category_description = "151 to 200	Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Very Unhealthy":
            category_color = "veryunhealthy"
            category_description = "201 to 300	Health alert: everyone may experience more serious health effects."
        elif api[0]['Category']['Name'] == "Hazardous":
            category_color = "hazardous"
            category_description = "301 to 500	Health warnings of emergency conditions. The entire population is more likely to be affected."
        return render(request, 'home.html', {'api': api, 'category_description': category_description,'category_color': category_color})


def about(request):
    return render(request, 'about.html', {})
