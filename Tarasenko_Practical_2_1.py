import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Прочитайте CSV файл (використовуйте метод read_csv):
data = pd.read_csv("C:/Users/Kate/GlobalYouTubeStatistics.csv",encoding='latin-1')
print(data)

#Виведіть перші п'ять рядків (використовується метод head)
print(data.head(10))

#Виведіть розміри датасету (використовуйте метод shape)
print(data.shape)

#Перевірте, чи у всіх рядків вистачає даних:
# виведіть кількість пропусків  у кожному зі стовпців (використовуйте методи isna та sum).
na_count_per_row = data.isna().sum(axis=1)
data['NA_Count_Per_Row'] = na_count_per_row
print(data)

data.fillna(np.nan, inplace=True)
#Замініть комірки з пропущеними значенями на середні за стовпцем. І тип даних на float.

columns_with_missing_values = data.columns[data.isna().any()].tolist()
for column in columns_with_missing_values:
    if data[column].dtype in ['float','int']:
        data[column] = data[column].astype('float')
        column_mean = data[column].mean(skipna=True).round(1)
        data[column].fillna(column_mean, inplace=True)
# Check the nan once more
na_count_per_row = data.isna().sum(axis=1)
data['NA_Count_Per_Row'] = na_count_per_row
print(data)

# find the quantity of unique values in the column "Country"
column_name = "Country"
unique_value_count = data[column_name].nunique()
print(unique_value_count)

# Побудуйте діаграму розподілу переглядів (використовуйте kind='hist')
column_name = 'video views'
data[column_name].plot(kind='hist')
plt.ylabel("views")
plt.title(f'Histogram of {column_name}')
plt.show()

# find max, mean, min
column_name = 'video views'
max_value = data[column_name].max()
print(max_value)
column_name = 'video views'
min_value = data[column_name].min()
print(min_value)
column_name = 'video views'
mean_value = data[column_name].mean()
print(mean_value)

#find the country that has the most uploaded videos
max_value_index = data['uploads'].idxmax()
country_with_max_value = data.loc[max_value_index, 'Country']
max_value = data['uploads'].max()

print(f"The country with the largest video uploads value ({max_value}) is: {country_with_max_value}")