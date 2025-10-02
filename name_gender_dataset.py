import pandas as pd
import bisect

df = pd.read_csv("name_gender_dataset.csv", sep=";")

print(df.head())
print(df.columns)

names = df["Name"].tolist()

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    arr_sorted = sorted(arr)
    index = bisect.bisect_left(arr_sorted, target)
    if index < len(arr_sorted) and arr_sorted[index] == target:
        return index
    return -1

target_name = "Thomas"
print(f"Лінійний пошук ({target_name}):", linear_search(names, target_name))
print(f"Бінарний пошук ({target_name}):", binary_search(names, target_name))
