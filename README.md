## How to Run This Project

1. Prequisites:\
   First, you need to install [pipenv](https://pipenv.pypa.io/en/latest/) and [docker](https://www.docker.com/products/docker-desktop/).
   
2. Clone this repository:
   ```bash
   git clone https://github.com/Rakun12/study-depression-classification.git
   ```
3. Set up the environment\
   Make sure that `pipenv` and `docker` already installed.
   - If `pipenv` didn't install yet, you can run this code:
     ```bash
     pip install pipenv
     ```
4. Run the docker first
5. Build the dockerfile inside:
   ```bash
   docker build -t depression-classification .
   ```
6. Run the docker image:
   ```bash
   docker run -it -p 1212:1212 depression-classification
   ```
7. You can access the app through a web browser or API requests, If you have deployed the project using Docker or With the Flask application.
   ```python
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
   ```
