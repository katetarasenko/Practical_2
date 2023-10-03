import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data  = pd.read_csv("C:/Users/Kate/bestsellerswithcategories.csv",encoding='latin-1')
print(data)
data.head(10)
#find the shape and tell how many books are in this dataframe
#data.shape()
column_name = 'Name'  # Replace with the actual column name
unique_value_count = data[column_name].nunique()
print(unique_value_count)
#dataset stores the information about 351 books
data.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']
print(data)

#Вивести кількість пропусків у кожному стовпчику.
#Питання : Чи є в якихось змінних пропуски? (Так / ні)
na_count_df = data.isna().sum().reset_index()
na_count_df.columns = ['Column_Name', 'NA_Count']
data['Total_NA_Count'] = na_count_df['NA_Count']
print(data)

#За допомогою методу unique  перевірте. Які є унікальні жанри в стовпці genre
#Питання : Які є унікальні жанри?
column_name = 'genre'  # Replace with the actual column name
unique_genre_value_count = data[column_name].nunique()
print(unique_genre_value_count)

#Визначте максимальну, мінімальну, медіанну ціну за допомогою методів  max, min, mean, median
#Питання: Максимальна ціна?
column_name = 'price'
max_price = data[column_name].max()
print(max_price)

#Питання: Мінімальна ціна?
column_name = "price"
min_price = data[column_name].min()
print(min_price)

#Питання: Середня ціна?
column_name = "price"
mean_price = data[column_name].mean()
print(mean_price)

#Питання: Медіанна ціна?
column_name = "price"
median_price = data[column_name].median()
print(median_price)

#Виконайте наступні завдання з пошуку і сортування даних

#Питання: Який рейтинг у датасеті найвищий?
column_name = 'user_rating'
max_rev = data[column_name].dropna().max()
print(max_rev)

#Питання: Скільки книг мають такий рейтинг?
max_rating_books = len(data[data['user_rating'] == data['user_rating'].max()])
print(max_rating_books)


#Питання: Яка книга має найбільше відгуків?
sorted_data = data.sort_values(by=["reviews", "name"])
last_row = sorted_data.tail(1)
last_name = last_row["name"].to_string(index=False)
print(data.to_string())
print(sorted_data)
print(last_name)

#Питання: З тих книг, що потрапили до Топ-50 у 2010 році, яка книга найдорожча ?
top_2010 = data[data["year"] == 2010].sort_values(by = ["user_rating"]).tail(50)
most_expensicve = top_2010[top_2010["price"] == top_2010["price"].max()]["name"].to_string(index=False)
print(top_2010)

#Питання : Скільки книг жанру Fiction потрапили до Топ-50 у 2012 році
top_2012 = data[data["year"] == 2012].sort_values(by = ["user_rating"])
fiction_books_2012 = top_2012['genre'][top_2012['genre'] == 'Fiction'].count()
print(top_2012)

#Питання : Скільки книг з рейтингом 4.9 потрапило до рейтингу у 2010 та 2011 роках (використовуйте | або метод isin)?
rating_2010 = data[data["year"] == 2010].sort_values(by = ["user_rating"]).tail(50)
rating_2011 = data[data["year"] == 2011].sort_values(by = ["user_rating"]).tail(50)
rating_2010_2011 = pd.concat([rating_2010,rating_2011]).sort_values(by = ['user_rating']).tail(50)
count = (rating_2010_2011['user_rating'] == 4.9).sum()
print("how many books  have a 4.9 rating", count)


#Вивести максимальну і  мінімальну ціну для жанру Fiction I NonFiction (за допомогою методів  groupby та agg, для підрахунку мінімальних та максимальних значень використовуйте max та min). Використовуйте тількі потрібні вам стовпці.
g_p = data.groupby('genre')[['price']]
result = g_p.agg({"price" : ["min", 'max']})
print(result)