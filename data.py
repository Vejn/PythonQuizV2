import requests

# Parameters that we need to get right response from Api
parameters = {
    "amount": 10,
    "type": "boolean",
}

# Using Open Trivia Api to get the questions for the Quiz
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data['results']


