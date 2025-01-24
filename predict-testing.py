import requests

url = 'http://localhost:1212/predict'

user = {
    'academic_pressure': 4, 
    'age': 25, 
    'cgpa': 9.25, 
    'dietary_habits': 'healthy',
    'family_history_of_mental_illness': 'yes',
    'financial_stress': 4,
    'sleep_duration_hours': '5-6', 
    'study_satisfaction': 4, 
    'suicidal_thoughts': 'no',
    'work/study_hours': 7
}

response = requests.post(url, json=user).json()
print(response)