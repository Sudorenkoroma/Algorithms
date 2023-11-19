from phone import Phone
from item import Item



# phone1 = Phone("myPhone1", 500, 5, 1)


Item.instantiate_from_csv()
print(Item.all)
# print(phone1.calculate_total_price())