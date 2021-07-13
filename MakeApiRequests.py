import requests
import json
class Api:
    def __init__(self):
        pass

    def makeApiRequestForCounrty(self, country_name):
        url = "https://covid-19-tracking.p.rapidapi.com/v1/"+country_name
        
        headers = {
            'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
            'x-rapidapi-key': "d46bd01c2cmsh4e9573f5eeece4cp104fcejsn4016dc963204"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('response')[0]
        print(result.get('cases'))
        print("*" * 20)
        return result.get('cases') , result.get('deaths'),result.get('tests')


    def makeApiRequestForIndianStates(self):
        url = "https://covid-19-tracking.p.rapidapi.com/v1/india"
        headers = {
            'x-rapidapi-host': "covid-19-tracking.p.rapidapi.com",
            'x-rapidapi-key': "d46bd01c2cmsh4e9573f5eeece4cp104fcejsn4016dc963204"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        #result = js.get('list')
        return js


    def makeApiWorldwide(self):
        url = "https://covid-19-statistics.p.rapidapi.com/reports/total"
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "d46bd01c2cmsh4e9573f5eeece4cp104fcejsn4016dc963204"
        }
        response = requests.request("GET", url, headers=headers)
        # print(response.text)
        js = json.loads(response.text)
        print("******", js)
        result = js.get('data')

        return result

