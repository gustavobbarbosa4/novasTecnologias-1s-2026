import pandas as pd
df = pd.read_csv(
    "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv",
    sep=",",
    encoding="utf-8",
    na_values=["N/A","-"]
)
print("-------Desafio 1-------")
print(df.head())
df.info()
print(df.shape)

print("-------Desafio 2-------")
describe = df.describe()
print(describe)
print(df["Pclass"].nunique())
print(df["Sex"].value_counts())

print("-------Desafio 3-------")
print(df.loc[0:10, ["Name", "Age"]])
print(" ")
print(df.iloc[14])

print("-------Desafio 4-------")
print(df[df["Age"] >= 60])
minas_ricas = df[
    (df["Sex"] == "female") &
    
    (df["Pclass"] == 1)]
print(minas_ricas)
print(df[df["Fare"].between(50, 100)])
print(df.query("Embarked == 'C' and Survived == 1"))