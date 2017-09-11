# BUILD

You want to create a new virtualenv and then run `pip install -r api/requirements.txt` from the project root. This will install the Python packages you will need.

You will need to set the environment variable `OPEN_WEATHER_MAP_KEY` to your OpenWeather Map Key then from within the api folder run `python manage.py runserver`. This will spinup the dev server on the default port.

Once that is up you will want ot go into the `front-end` folder and open up the `index.html` file in a browser. This should load the UI.

