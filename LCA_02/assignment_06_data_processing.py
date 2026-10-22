import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv')

print("\n")
print("Initial Dataset Shape:", df.shape)

print("\n")
print("Missing Values Before Cleaning:")
print(df.isnull().sum())

df['Age'] = df['Age'].fillna(df['Age'].mean())

df = df.drop(columns=['Cabin'])

df = df.dropna(subset=['Embarked'])

df = df.drop_duplicates()

first_class_df = df.loc[df['Pclass'] == 1]
print("\n")
print(f"\nNumber of First Class Passengers: {len(first_class_df)}")

print("\n")
print("Missing Values After Cleaning:")
print(df.isnull().sum())

print("\n")
print("Cleaned Dataset Shape:", df.shape)
