import pandas as pd

data = {'Name': ['John', 'Emma', 'Alex'],
        'Age': [25, 28, 30],
        'City': ['New York', 'London', 'Paris']}



df = pd.DataFrame(data)

print(df)

poo = df['Name']

smell = df["Age"].mean()

print(poo)
print('mean', smell)

