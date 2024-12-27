# Workout Tracker

This is a Python script that allows users to track their workouts and store the data in a Google Sheets spreadsheet. 
It utilizes the Nutritionix API to get exercise data and the Sheety API to update the Google Sheets document.

### Workout Tracker Input 
![Workout Tracker Input](Images/Tracker%20input.JPG)

### Workout Tracker Output
![Workout Tracker Input](https://github.com/NoorMahammad-S/Workout_Tracker_using_API/blob/master/Images/Tracker%20output.JPG)

## Prerequisites

Before running the script, you need to obtain API credentials and install the required Python libraries.

### API Credentials

- You'll need to sign up and obtain API credentials from Nutritionix and Sheety.

- Replace the `APP_ID` and `API_KEY` in the code with your Nutritionix API credentials.

- Replace the `"Authorization"` value in the code with your Sheety API token.

### Python Libraries

You'll need to have the following Python libraries installed:

- `requests`: You can install it using pip: `pip install requests`

## How to Use

1. Clone this repository or download the code to your local machine.

2. Open the script in a code editor.

3. Replace the placeholder values with your Nutritionix API credentials (`APP_ID` and `API_KEY`).

4. Run the script:

   ```bash
   python workout_tracker.py
   ```

5. You will be prompted to enter details about your workout, such as exercise description. Provide the information as requested.

6. The script will send a request to the Nutritionix API to get exercise details, and then it will store the exercise information in a Google Sheets spreadsheet using the Sheety API.

7. You can view your workout history in the Google Sheets spreadsheet specified in the `sheet_endpoint` variable.

## Customization

- You can customize your `GENDER`, `WEIGHT_KG`, `HEIGHT_CM`, and `AGE` to match your personal information.

- You can modify the Google Sheets endpoint (`sheet_endpoint`) if you have your own Sheety API integration.

- You can further enhance the script with error handling, data validation, and more features as needed.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The code was developed with the help of Nutritionix and Sheety APIs.
