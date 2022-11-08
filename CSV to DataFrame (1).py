# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.DataFrame(pd.read_csv('cars.csv'))

# Print out cars
print(cars)