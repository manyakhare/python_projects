# with open("weather_data.csv", mode="r") as data_file:
#     print(data_file.readlines())

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# data_list = data["temp"].to_list()
# print(data_list)
# avg = sum(data_list)/len(data_list)
# print(avg)
# print(data["temp"].mean())
# print(data["temp"].max())

# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# far = (int(monday.temp) * 9 / 5) + 32
# print(far)


import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
Gray_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
Cinnamon_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
Black_squirrel = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color" : ["Gray", "Cinnamon", "Black"],
    "count" : [Gray_squirrel, Cinnamon_squirrel, Black_squirrel]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")

