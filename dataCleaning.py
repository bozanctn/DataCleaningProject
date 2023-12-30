import pandas as pd 


df = pd.read_excel("Customer Call List.xlsx")

df = df.drop_duplicates()

df  = df.drop(columns="Not_Useful_Column")

df["Last_Name"] = df["Last_Name"].str.lstrip("...")

df["Last_Name"] = df["Last_Name"].str.lstrip("/")

df["Last_Name"] = df["Last_Name"].str.rstrip("_")

df["Phone_Number"] = df["Phone_Number"].str.replace("-", "")

df["Phone_Number"] = df["Phone_Number"].str.replace("|", "")

df["Phone_Number"] = df["Phone_Number"].str.replace("/", "")

#df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))

df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])

df["Phone_Number"] = df["Phone_Number"].str.replace('nan--','')

df["Phone_Number"] = df["Phone_Number"].str.replace('Na--','')

df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(',',n= 2,expand=True)

print(df[["Street_Address", "State", "Zip_Code"]])

df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")

df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")

print(df["Paying Customer"])


df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")

df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")


print(df["Do_Not_Contact"])

df = df.replace('N/a', '')
df = df.replace('NaN', '')
df = df.fillna('')

print(df)

for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
       df.drop(x, inplace=True)

print(df)

for x in df.index:
    if df.loc[x, "Phone_Number"] == '':
       df.drop(x, inplace=True)


print(df)

df = df.reset_index(drop=True)

print(df)



