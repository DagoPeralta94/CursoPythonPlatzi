import pandas as pd

data = {'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
        'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
        'age': [27, 31, 36, 53, 48, 36, 40, 34],
        'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
        'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]}
df1 = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
df2 = pd.DataFrame(data, columns = ['first_name', 'last_name', 'age', 'amount_1', 'amount_2'])
df1.to_csv('C:\\Users\\RYZEN\\Documents\\Python\\Python_Excel\\prueba1.csv')
df2.to_csv('C:\\Users\\RYZEN\\Documents\\Python\\Python_Excel\\prueba2.csv')

#df3 = pd.read_csv('C:\\Users\\RYZEN\\Documents\\Python\\Python_Excel\\prueba1.csv')
#print(type(df3['amount_1']))

new_amount_1 = df1['amount_1']
longitud_new_amount_1 = len((new_amount_1))
new_amount_2 = df2['amount_1']
longitud_new_amount_2 = len((new_amount_2))

