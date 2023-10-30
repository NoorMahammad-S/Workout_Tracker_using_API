import requests
from datetime import datetime


# Define user information (You can replace with actual values)
GENDER = "male"
WEIGHT_KG = "50"
HEIGHT_CM = "5.5"
AGE = "25"

# Replace "Your App ID" and "Your API Key" with your actual Nutritionix API credentials
APP_ID = "Your App ID"
API_KEY = "Your API Key"

# Define API endpoints
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/daabe1f15058534d58d2371ab9d1ebd3/myWorkoutsSpreadsheet/workouts"

# Get exercise input from the user
exercise_text = input("Tell me which exercises you did: ")

# Set request headers for the Nutritionix API
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}


# Create parameters for the Nutritionix API request
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Send a POST request to the Nutritionix API
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()


# Get the current date and time for use in the spreadsheet
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Loop through the exercises in the Nutritionix API response
for exercise in result["exercises"]:
    # Create input data for the Sheety API request
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Set headers for the Sheety API request
    bearer_headers = {
        "Authorization": "Bearer rbdfdgfkfjbdkggbvvb2"  # replace with actual authorization token
    }

    # Send a POST request to the Sheety API to add workout data to the spreadsheet
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)


