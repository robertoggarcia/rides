## Rides App
In order to run the app, follow the next steps:
1. Add input data in data/operations.json file
2. Run the app ```python -m app.app```

Run with docker:
1. Build the image ```docker build -t rides .```
2. And then run the container image ```docker run rides```


## Project structure
### app.py
General logic that read rides data and validate the input type.

### driver.py
Driver functions for ban or activate a driver.

### rides.py
Rides functions to start or finish a ride.

## Data
Folder to store input data.

## Utils
Folder that contains the schema validations for the input data. For example validate the input for a new driver.

## Test
All app test cases. In order to run the test cases run the following command:
```py.test```

Note: Install dependencies first. Follow the next steps:
1. Make a virtual env: ``` python3 -m venv ../venv```
2. Activate the env: ```source ../venv/bin/activate```
3. Install the package: ```pip install -r requirements.txt```
4. Run the test!
