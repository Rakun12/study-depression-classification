# Study Depression Classification

## Table of Contents
- [Problem Description](#problem-description)
- [Repository](#repository)
- [Model Summary](#model-summary)
- [How to Run This Project](#how-to-run-this-project)

## Problem Description
Learning is an activity that can cause stress. Especially with a long duration and high score targets to achieve, it can trigger significant levels of stress. Awareness of stress in students should be a concern. Through this project, which aims to classify depression in students, the model can assist in providing suggestions and monitoring whether a student is experiencing depression. Depression must be identified early so that affected individuals do not remain trapped in a depressive phase, which could lead to extreme actions such as self-harm or even suicide. The model in this project will help users determine whether they are experiencing depression. If the model detects depression, users can immediately contact a psychologist to consult about the depression they are experiencing.

## Repository
- `data` : Folder contains the data used in this project
- `images` : Folder contains some images
- `model` : Folder contains saved model which trained in this project
- `notebook` : Notebook the project built
- `training.py` : Convert file from the notebooks
- `predict.py` : File used to run the server, contain the API inside
- `predict-testing.py` : File used to testing the API

## Model Summary
This project 2 algorithm: Logistic Regression and Random Forest. After training the model, the performance got is:

| Model               | Training Acc | Testing Acc | AUC   | 
|:--------------------|:------------:|:-----------:|:-----:|
| Logistic Regression | 0.845        | 0.85        | 0.838 |
| Random Forest       | 0.891        | 0.84        | 0.834 |

Based on the performance, the model use is Logistic Regression. The AUC score is bigger than Random Forest.


## How to Run This Project

1. Prequisites:\
   First, you need to install [pipenv](https://pipenv.pypa.io/en/latest/) and [docker](https://www.docker.com/products/docker-desktop/).
   
2. Clone this repository:
   ```bash
   git clone https://github.com/Rakun12/study-depression-classification.git
   ```
3. Set up the environment\
   Make sure that `pipenv` and `docker` already installed.\
   If `pipenv` didn't install yet, you can run this code:
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
7. You can access the app through a web browser or API requests, or just run the file `predict_testing.py`
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
