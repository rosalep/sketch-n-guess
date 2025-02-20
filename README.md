# sketch-n-guess

Python 3.12.3
Django
virtualenv

To run:
A virtualenv is needed to run Django apps, so you must create an environment.
To install virtualenv:
```
pip install virtualenv
```
Make a new directory where you will store your environment:
```
mkdir environments
```
Inside of that directory run the following:
```
virtualenv <env_name>
```
To start the environment:
```
source <env_name>/bin/activate
```
NOTE: The secret key is stored using environment variables, so you need to this in the base directory:
```
pip install python-dotenv
```
The settings.py file should have the following lines added:
```
import os
from dotenv import load_dotenv
SECRET_KEY = os.environ.get('SECRET_KEY')
```
Inside the .env file insert the following:
```
SECRET_KEY=<your_key>
```
Once the environment is set up, run the following commands from the sketch_game/sketch_game directory:
```
python3 manage.py makemigrations users
```
```
python3 manage.py migrate
```
