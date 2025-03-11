#This class defines a food item and its properties.
class Item:
    def __init__(self, calories, protein, carbs, fat,fiber,vitamins):
        self._calories = calories
        self._protein = protein
        self._carbs = carbs
        self._fat = fat
        self._fiber = fiber
        self._vitamins = vitamins
    
    def get_calories(self):
        return self._calories

    def get_protein(self):
        return self._protein

    def get_carbs(self):
        return self._carbs

    def get_fat(self):
        return self._fat
    
    def get_fiber(self):
        return self._fiber

    def get_vitamins(self):
        return self._vitamins


    def to_dict(self):
        return {
            "calories": self._calories,
            "protein": self._protein,
            "carbs": self._carbs,
            "fat": self._fat,
            "fiber": self._fiber,
            "vitamins":[
                { "name": key , "value":value  } for key, value in self._vitamins.items()

            ]
        }
