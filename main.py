import requests,datetime as dt



natural_language_exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {'x-app-id': os.environ.get(APP_ID),'x-app-key': os.environ.get(APP_KEY)}


query = input("Tell me which exercise you did: ")
params = {'query': query,'gender': 'male', 'weight_kg': 81, 'height_cm': 178,'age': 26}


response = requests.post(natural_language_exercise_endpoint,json=params,headers=headers)

data = response.json()

exercises = data['exercises']

today = dt.datetime.now()

today_date = today.strftime("%m/%d/%Y")
today_hour = today.strftime("%H:%M:%S")
sheety_endpoint= os.environ.get('SHEETY_ENDPOINT')

headers = {'Content-Type': 'application/json','Authorization': os.environ.get('TOKEN')}
for exercise in exercises:

    exercise_type = exercise['user_input'].title()
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    sheety_body = {
                    'workout': {
                        'date': today_date,
                        'time': today_hour,
                        'exercise': exercise_type,
                        'duration': duration,
                        'calories': calories
                    }
                }
    response = requests.post(sheety_endpoint,json=sheety_body,headers=headers)
    print(response.text)







