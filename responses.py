def symptioms_pred_response(result):
    return {
    "agentId": "6d4292c6-9ea5-4008-9d59-2c58fcc0b2c7",
    "agentSettings": {
        "enableAgentWideKnowledgeConnector": true
    },
    "queryResult": {
        "allRequiredParamsPresent": true,
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        result
                    ]
                }
            },
            {
                "payload": {
                    "richContent": [
                        [
                            {
                                "options": [
                                    {
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        },
                                        "link": "",
                                        "text": "Menu"
                                    },
                                    {
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        },
                                        "link": "",
                                        "text": "FaQ"
                                    },
                                    {
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        },
                                        "link": "",
                                        "text": "Symption Based Prediction"
                                    },
                                    {
                                        "image": {
                                            "src": {
                                                "rawUrl": ""
                                            }
                                        },
                                        "link": "",
                                        "text": "Thank you"
                                    }
                                ],
                                "type": "chips"
                            }
                        ]
                    ]
                }
            }
        ],
        "fulfillmentText": "sai , we will Let You Know In Some Time.......",
        "intent": {
            "displayName": "Symptoms -Based Prediction",
            "name": "projects/health-bot-mbfm/locations/global/agent/intents/e6f78410-1c82-43df-abed-1b7922bca414"
        },
        "intentDetectionConfidence": 1,
        "languageCode": "en",
        "outputContexts": [
            {
                "lifespanCount": 2,
                "name": "projects/health-bot-mbfm/locations/global/agent/sessions/9ac311aa-fb76-4f2c-24e3-b9513bcb0580/contexts/user-email",
                "parameters": {
                    "abdominal_pain": "n",
                    "abdominal_pain.original": "n",
                    "chest_pain": "n",
                    "chest_pain.original": "n",
                    "chills": "n",
                    "chills.original": "n",
                    "cough": "n",
                    "cough.original": "n",
                    "dark_urine": "n",
                    "dark_urine.original": "n",
                    "diarrhoea": "n",
                    "diarrhoea.original": "n",
                    "email": "sai@gmail.com",
                    "email.original": "sai@gmail.com",
                    "fatigue": "n",
                    "fatigue.original": "n",
                    "headache": "n",
                    "headache.original": "n",
                    "high_fever": "n",
                    "high_fever.original": "n",
                    "itching": "n",
                    "itching.original": "n",
                    "joint_pain": "n",
                    "joint_pain.original": "n",
                    "loss_of_appetite": "n",
                    "loss_of_appetite.original": "n",
                    "malaise": "n",
                    "malaise.original": "n",
                    "muscle_pain": "n",
                    "muscle_pain.original": "n",
                    "name": "sai",
                    "name.original": "sai",
                    "nausea": "n",
                    "nausea.original": "n",
                    "random": "",
                    "random.original": "",
                    "skin_rash": "n",
                    "skin_rash.original": "n",
                    "sweating": "n",
                    "sweating.original": "n",
                    "vomiting": "n",
                    "vomiting.original": "n",
                    "yellowing_of_eyes": "n",
                    "yellowing_of_eyes.original": "n",
                    "yellowish_skin": "n",
                    "yellowish_skin.original": "n"
                }
            },
            {
                "lifespanCount": 3,
                "name": "projects/health-bot-mbfm/locations/global/agent/sessions/9ac311aa-fb76-4f2c-24e3-b9513bcb0580/contexts/prediction",
                "parameters": {
                    "abdominal_pain": "n",
                    "abdominal_pain.original": "n",
                    "chest_pain": "n",
                    "chest_pain.original": "n",
                    "chills": "n",
                    "chills.original": "n",
                    "cough": "n",
                    "cough.original": "n",
                    "dark_urine": "n",
                    "dark_urine.original": "n",
                    "diarrhoea": "n",
                    "diarrhoea.original": "n",
                    "email": "sai@gmail.com",
                    "email.original": "sai@gmail.com",
                    "fatigue": "n",
                    "fatigue.original": "n",
                    "headache": "n",
                    "headache.original": "n",
                    "high_fever": "n",
                    "high_fever.original": "n",
                    "itching": "n",
                    "itching.original": "n",
                    "joint_pain": "n",
                    "joint_pain.original": "n",
                    "loss_of_appetite": "n",
                    "loss_of_appetite.original": "n",
                    "malaise": "n",
                    "malaise.original": "n",
                    "muscle_pain": "n",
                    "muscle_pain.original": "n",
                    "nausea": "n",
                    "nausea.original": "n",
                    "random": "",
                    "random.original": "",
                    "skin_rash": "n",
                    "skin_rash.original": "n",
                    "sweating": "n",
                    "sweating.original": "n",
                    "vomiting": "n",
                    "vomiting.original": "n",
                    "yellowing_of_eyes": "n",
                    "yellowing_of_eyes.original": "n",
                    "yellowish_skin": "n",
                    "yellowish_skin.original": "n"
                }
            },
            {
                "lifespanCount": 1,
                "name": "projects/health-bot-mbfm/locations/global/agent/sessions/9ac311aa-fb76-4f2c-24e3-b9513bcb0580/contexts/awaiting-name-check",
                "parameters": {
                    "abdominal_pain": "n",
                    "abdominal_pain.original": "n",
                    "chest_pain": "n",
                    "chest_pain.original": "n",
                    "chills": "n",
                    "chills.original": "n",
                    "cough": "n",
                    "cough.original": "n",
                    "dark_urine": "n",
                    "dark_urine.original": "n",
                    "diarrhoea": "n",
                    "diarrhoea.original": "n",
                    "email": "sai@gmail.com",
                    "email.original": "sai@gmail.com",
                    "fatigue": "n",
                    "fatigue.original": "n",
                    "headache": "n",
                    "headache.original": "n",
                    "high_fever": "n",
                    "high_fever.original": "n",
                    "itching": "n",
                    "itching.original": "n",
                    "joint_pain": "n",
                    "joint_pain.original": "n",
                    "loss_of_appetite": "n",
                    "loss_of_appetite.original": "n",
                    "malaise": "n",
                    "malaise.original": "n",
                    "muscle_pain": "n",
                    "muscle_pain.original": "n",
                    "name": "sai",
                    "name.original": "sai",
                    "nausea": "n",
                    "nausea.original": "n",
                    "random": "",
                    "random.original": "",
                    "skin_rash": "n",
                    "skin_rash.original": "n",
                    "sweating": "n",
                    "sweating.original": "n",
                    "vomiting": "n",
                    "vomiting.original": "n",
                    "yellowing_of_eyes": "n",
                    "yellowing_of_eyes.original": "n",
                    "yellowish_skin": "n",
                    "yellowish_skin.original": "n"
                }
            }
        ],
        "parameters": {
            "abdominal_pain": "n",
            "chest_pain": "n",
            "chills": "n",
            "cough": "n",
            "dark_urine": "n",
            "diarrhoea": "n",
            "fatigue": "n",
            "headache": "n",
            "high_fever": "n",
            "itching": "n",
            "joint_pain": "n",
            "loss_of_appetite": "n",
            "malaise": "n",
            "muscle_pain": "n",
            "nausea": "n",
            "skin_rash": "n",
            "sweating": "n",
            "vomiting": "n",
            "yellowing_of_eyes": "n",
            "yellowish_skin": "n"
        },
        "queryText": "n",
        "sentimentAnalysisResult": {
            "queryTextSentiment": {}
        }
    },
    "responseId": "7f873034-0ff4-4eb3-a276-347ea397134d-ae5d3882"
}