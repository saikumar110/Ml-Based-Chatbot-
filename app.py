# importing necessary liabraries
from flask import *
from Nutrition_processing .Nutrition_processing import *
from Covid_Api_processing.covid_processing import *


app = Flask(__name__)  # initializing a flask app


@app.route('/', methods=['GET', 'POST'])
def index():

    # fetching the json request
    req = request.get_json(silent=True, force=True)
    req = preprocessing(req)  # processing the requested data
    req = json.dumps(req, indent=4)  # Converting into json format

    r = make_response(req)
    r.headers['Content-Type'] = 'application/json'
    return r

    # return jsonify({"homepage":"http"})


# fetching data from parameter and creating parameters for ml model
def get_para(parameters):
    yes = ['yaa', 'yup', 'Y', 'y', 'Yes']
    no = ['n', 'nope', 'no', "No"]
    # creating list of data fetched from user from dialogflow
    ml_input = [1 if parameters[i] in yes else 0 for i in parameters]
    return ml_input


def model_predictions(model_features):  # Predicting the diseases
    return "done prediction"


def preprocessing(req):  # processing request from the dialogflow

    queryResult = req.get('queryResult')
    parameters = queryResult.get('parameters')
    intent = queryResult.get('intent')
    display_name = intent.get('displayName')
    # print(display_name)
    if display_name == "Symptoms -Based Prediction":

        # data for ml model_features
        model_data = get_para(parameters)
        # final result for ml model_features
        final_result = model_predictions(model_data)

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            final_result
                        ]
                    }
                }

            ]
        }

    elif display_name == "Nutrition information":

        raw_query = Nutrition_processing.get_nutrient_features(
            data=req)                                                     # Extracting raw query
        api_data = Nutrition_processing.Nutritions_api(
            raw_query)                                                    # Extracting data from Api
        food_info = Nutrition_processing.get_food_details(
            api_data)                                                     # Extracting information from API4
        # print(food_info)
        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            ""
                        ]
                    }
                },
                {
                    "payload": {
                        "richContent": food_info
                    }
                }
            ]
        }
    elif display_name == "Calorie-Count":

        query, gender, weight_kg, height_cm, age = Nutrition_processing.get_exercise_features(
            data=req)                                                                    # Extracting raw query
        api_data = Nutrition_processing.Exercise_api(
            query, gender, weight_kg, height_cm, age)                                    # sending all features
                                                                                          # Extracting information from API
        calorie_count = Nutrition_processing.get_cal(api_data)

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            calorie_count + "Cal"
                        ]
                    }
                }

            ]
        }
    elif display_name == "Covid-News":

        # Extracting the news data from API
        news_data = Covid_data_processing.Acess_api()
        # Extracting the articles                    # Extracting information from API
        articles = Covid_data_processing.get_articles(news_data)

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Latest New From Health Bot 👨‍⚕️"
                        ]
                    }
                }, {
                    "payload": {
                        "richContent": articles[:4]
                    }}

            ]
        }
    elif display_name == "By-Country-Name-stats":

        stat_name = Covid_data_processing.get_state_name(req)
        data = Covid_data_processing.getLatestCountryDataByName(stat_name)

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Latest Covid Stats From Health Bot 👨‍⚕️"
                        ]
                    }
                }, {
                    "payload": {
                        "richContent": data
                    }}

            ]
        }
    elif display_name == "world-wide":

        data=Covid_data_processing.getLatestCountryData()
       
        

        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            "Covid Stats From Health Bot 👨‍⚕️"
                        ]
                    }
                }, {
                    "payload": {
                        "richContent": data
                    }}

            ]
        }

    else:
        return {

            "fulfillmentMessages": [
                {
                    "text": {
                        "text": [
                            " Try Again "
                        ]
                    }
                }

            ]
        }


if __name__ == '__main__':

    app.run(debug=True)
