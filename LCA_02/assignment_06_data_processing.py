import pandas as pd

df = pd.read_csv("/content/Titanic-Dataset.csv")

print("Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nStatistical Summary:")
print(df.describe())

print("First Five Rows:")
print(df.head())

print("\nLast Five Rows:")
print(df.tail())

print("\nDataset Information:")
df.info()

print("\nPassenger Names:")
print(df["Name"].head())

print("\nPassengers by Gender:")
print(df["Pclass"].value_counts())

print("\nAverage Age:")
print(df["Age"].mean())

print("\nHighest Fare:")
print(df["Fare"].max())

print("\nAverage Fare:")
print(df["Fare"].mean())

df = df.drop(columns=['Cabin', 'Embarked'])

print("\nPassengers Older Than 60:")
print(df[df["Age"] > 60])

print("\nPassengers Who Survived:")
print(df[df["Survived"] == 1][["Name", "Sex", "Age"]].head())

print("\nSurvival Counts:")
print(df["Survived"].value_counts())

print("\nSurvival Rate by Gender:")
print(df.groupby("Sex")["Survived"].mean())

print("\nTop 10 Highest Fares:")
print(df.sort_values("Fare", ascending=False)[["Name", "Fare"]].head(10))

print("\nPassengers by Class:")
print(df["Pclass"].value_counts().sort_index())

print("\nAverage Age by Gender:")
print(df.groupby("Sex")["Age"].mean())

df = df.drop_duplicates()
print("\nDuplicate Rows Removed")

for col in df.columns:
    if df[col].isnull().any():
        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].mean())
        else:
            df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing Values Handled")

df.to_csv("titanic_copy.csv", index=False)
