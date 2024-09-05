# Running the Application

To run the application, Follow the instructions below
- Install dependencies, by running the following command
    - `pip install -r requirements.in`
- Open the terminal in the projects folder
- Generate Tables, Using the following command
    - `python manage.py migrate`
- Run the following command to run the server
    - `python manage.py runserver`

## List all Users

You can visit the following url to list users
 - `localhost:8000/api/users`

## Generate DLO
To generate a DLO for a particular user, You can visit the following url.
    - `localhost:8000/api/dlo/{user_id}`
For testing purposes you can get the user id from the above url.

