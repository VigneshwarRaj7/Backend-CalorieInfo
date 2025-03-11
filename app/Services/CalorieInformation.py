#This service was just created for testing purpose. 
from app.Models.Item import Item

def get_CalorieInfo():
    item = Item(100,12,10,10,10,  {
        "niacin": 1,
        "riboflavin": 0.2,
        "vitaminA": 100,
        "vitaminB12": 0.5,
        "vitaminD": 10,
        "vitaminE": 0.5
    })
    print(item)
    return item.to_dict()