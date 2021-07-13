import requests
import json
import fontstyle

class Nutrition_processing():

    def __init__(self):
        pass



    
        """
            This class shall  be used to extract features for nutrition info and exercise and making api requests.

            
            Version: 1.0
            Revisions: None

        """




    def get_food_details(data):
        food_list=[]
        foods =data.get('foods')                                  #Extracting all food items from dict
        for i in range(len(foods)):                               # Extracting Each and every food item data 
            food_dict =[]                                         # creating dict and storing all info about each data
            article=[
                {
                    "accessibilityText":"",
                    "type": "image",
                    "rawUrl":foods[i].get('photo')['thumb']
                },
                {
                     "subtitle": "Total Calories "+str( foods[i].get('nf_calories'))+'\n'+"Total fat" +str( foods[i].get('nf_total_fat'))+'\n'+"Total saturated fat" +str( foods[i].get('nf_saturated_fat'))
                       +'\n'+"Total cholesterol   " +str( foods[i].get('nf_cholesterol'))+'\n'+"Total sodium" +str( foods[i].get('nf_sodium'))
                       +'\n'+"Total carbohydrate" +str( foods[i].get('nf_total_carbohydrate'))
                       +'\n'+"Total dietary fiber" +str( foods[i].get('nf_dietary_fiber'))
                       +'\n'+"Total sugars"+"\t" +str( foods[i].get('nf_sugars'))
                       +'\n'+"Total protein" +str( foods[i].get('nf_protein'))
                       +'\n'+"Total potassium" +str( foods[i].get('nf_potassium')),
                    
                    
                     "type": "info",
                     "actionLink":"",
                    "title": (foods[i].get('food_name')).capitalize()
                }
            ]
            food_list.append(article)
        return food_list


    def Nutritions_api(query):
        url = "https://trackapi.nutritionix.com/v2/natural/nutrients"

        payload = json.dumps({
                                "query": query,
                                "timezone": "US/Eastern"
                                })

        headers = {
        'x-app-key': '0667c0d04a205a8ae5d7daa0f968b6da',
        'x-app-id': '556539cd',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        
        return response.json()
    
    def get_nutrient_features(data):                #returning the query by the user 
        return data.get('queryResult')['queryText'] 

    """ def get_food_details(data):
        food_list=[]
        foods =data.get('foods')                                  #Extracting all food items from dict
        for i in range(len(foods)):                               # Extracting Each and every food item data 
            food_dict ={}                                         # creating dict and storing all info about each data
            food_dict['food_name']=foods[i].get('food_name')
            food_dict['serving_qty']=foods[i].get('serving_qty')
            food_dict['serving_unit']=foods[i].get('serving_unit')
            food_dict['nf_calories']=foods[i].get('nf_calories')
            food_dict['serving_weight_grams']=foods[i].get('serving_weight_grams')
            food_list.append(food_dict)
        return food_list """



#           ------------------------------------------Exercise Part ---------------------------------------

    def get_exercise_features(data):
        query = data.get("queryResult")['parameters']['Query']                   # Fetching query
        gender =data.get("queryResult")['parameters']['gender']                  # Fetching gender
        weight =data.get("queryResult")['parameters']['weight']['amount']        # Fetching weight
        height = data.get("queryResult")['parameters']['height']
        age = data.get("queryResult")['parameters']['age']                 # Fetching height
        return query,gender,weight,height,age

    def Exercise_api(query,gender,weight_kg,height_cm,age):
        url = "https://trackapi.nutritionix.com/v2/natural/exercise"

        payload = json.dumps({
                            "query": query,
                            "gender": gender,
                            "weight_kg": weight_kg,
                            "height_cm": height_cm,
                            "age": age
                            })

        headers = {
        'x-app-key': '0667c0d04a205a8ae5d7daa0f968b6da',
        'x-app-id': '556539cd',
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        
        return response.json()


    def get_cal(data):
        precal=data.get('exercises')
        return precal[0]['nf_calories']