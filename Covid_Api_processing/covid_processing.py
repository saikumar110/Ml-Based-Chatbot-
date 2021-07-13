import requests


class Covid_data_processing():

    def __init__(self):
        pass

        """ 
        
            This class shall  be used to extract features for Covid info and news  by  making api requests.

            
            Version: 1.0
            Revisions: None
        
        
         """

    # --------------------------------------------- News Section ---------------------------

    def Acess_api():

        url = "https://covid-19-news.p.rapidapi.com/v1/covid"

        querystring = {"q": "covid", "lang": "en", "media": "True"}

        headers = {
            'x-rapidapi-key': "d46bd01c2cmsh4e9573f5eeece4cp104fcejsn4016dc963204",
            'x-rapidapi-host': "covid-19-news.p.rapidapi.com"
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        return response.json()

    def get_articles(data):
        processed_atricles = []
        channel_list = ['thehindu.com', 'hindustantimes.com', 'indiatimes.com', 'indianexpress.com',
                        'cbsnews.com', 'ndtv.com', 'ndtv.com', 'google.com', 'healthline.com']
        for i in range(len(data['articles'])):
            if data['articles'][i]['media'] != None and data['articles'][i]['clean_url'] in channel_list:
                article = [
                    {
                        "accessibilityText": data['articles'][i]['link'],
                        "type": "image",
                        "rawUrl": data['articles'][i]['media']
                    },
                    {
                        "subtitle": data['articles'][i]['summary'][:60],
                        "type": "info",
                        "actionLink":data['articles'][i]['link'],
                        "title": data['articles'][i]['title']
                    }
                ]
                processed_atricles.append(article)
        return processed_atricles


#     ------------------------------------------------Stats Section ---------------------------------------

    def get_state_name(data):
        return data.get('queryResult')['queryText']

    def getLatestCountryDataByName(name):

        final_data = []

        url = "https://covid-19-data.p.rapidapi.com/country"

        querystring = {"name": name}

        headers = {
            'x-rapidapi-key': "c64477f5cemshc55c6ce39045df2p1e9929jsn5f773e90b280",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }
        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        confirmed = (response.text).split(",")[2][12:]
        recovered = (response.text).split(",")[3][12:]
        critical = (response.text).split(",")[4][11:]
        deaths = (response.text).split(",")[5][9:]

        data = [
            {
                "type": "description",
                "title": 'Statistics of '+name,
                "text": [
                    " Confirmed Cases : " + confirmed,
                    " Recovered Cases : " + recovered,
                    " Critical Cases : " + critical,
                    " Deaths Cases : " + deaths,

                ]
            }
        ]
        final_data.append(data)
        return final_data

    def getLatestCountryData():
        final_data = []
        url = "https://covid-19-data.p.rapidapi.com/totals"

        headers = {
            'x-rapidapi-key': "c64477f5cemshc55c6ce39045df2p1e9929jsn5f773e90b280",
            'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)
        confirmed = (response.text).split(",")[0][14:]
        recovered = (response.text).split(",")[1][12:]
        critical = (response.text).split(",")[2][11:]
        deaths = (response.text).split(",")[3][9:]

        data = [


            {
                "type": "description",
                "title": 'Statistics of Covid 2021 ',
                "text": [
                    " Confirmed Cases : " + confirmed,
                    " Recovered Cases : " + recovered,
                    " Critical Cases : " + critical,
                    " Deaths Cases : " + deaths,

                ]
            }

        ]
        final_data.append(data)

        return final_data
