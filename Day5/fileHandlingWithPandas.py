import pandas as pd

df = pd.read_csv("mod.csv")
print(df)

#Create dataFrame

df1 = pd.DataFrame({
    "Name":["David","RAhul","Tony"],
    "AGe":["12","15","16"],
    "Grade":["A","B","c"],
    "Location":["hyd","delhi","chennai"]
})

df1.to_csv('newstudents.csv', index=False)

#convert to excel
df1.to_excel("output.xlsx", index=False)