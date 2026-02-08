from collections import Counter

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

lst = [1, 3, 4, 5, 7, 4]


count = Counter(lst)
print(count)
print(type(count))
print(len(count))

