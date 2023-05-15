# Phone validation via OTP code

## Getting Started
For this project, I used the [Twilio](https://www.twilio.com/) API to send an SMS message to a phone number with a verification code.
The user then enters the code into the application to verify their phone number.

### Installing
For init project you need to clone this repository and install all dependencies.

`poetry install`

Open the project in your IDE and create a `.env` file in the root directory. Add the following environment variables to the file(see .env.example):

```
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_VERIFY_SID=your_twilio_verify_sid
```
### Starting
To start the application, run the following command in the terminal:

#### For run Rabbitmq you need to install docker and run command  
`docker run -d -p 5672:5672 rabbitmq`

#### For run Celery you need to run command 
`celery -A pythonpro_dz_9 worker -l INFO`

#### For run application you need to run command
`poetry python manage.py runserver`

