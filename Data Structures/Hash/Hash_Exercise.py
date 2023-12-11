import csv


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self, key):
        arr_index = self.get_hash(key)
        for kv in self.arr[arr_index]:
            if kv[0] == key:
                return kv[1]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        arr_index = self.get_hash(key)
        for index, kv in enumerate(self.arr[arr_index]):
            if kv[0] == key:
                print("del", index)
                del self.arr[arr_index][index]


nyc_weather = HashTable()

with open("nyc_weather.csv", "r") as f:
    next(f)
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        weather = float(tokens[1])
        nyc_weather[day] = weather


print(nyc_weather["Jan 1"])
print(nyc_weather.arr)
all_values = []
for sublist in nyc_weather.arr:
    for key, value in sublist:
        all_values.append(value)

average = sum(all_values) / len(all_values)
maxim = max(all_values)
print(average)
print(maxim)
