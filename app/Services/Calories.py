#This service provides response for food items and its weight with information like protein, carbs, fat and other.
#This service provides information when the API call is made from HOME page.

from flask import Flask, request, jsonify
import google.generativeai as genai 
import json
from app.Models.Item import Item


genai.configure(api_key="AIzaSyBigK0uLo3k4vnDEuWiN8UISblre4SCSxQ")  
def get_nutrition_info(food_item, weight):
       
        prompt = f"""
        Provide a JSON response with detailed nutrition information for {weight}g of {food_item}.
        The response must be structured as follows:
        {{
            "calories": value,
            "protein": value,
            "carbs": value,
            "fat": value,
            "fiber": value,
            "vitamins": {{
                "vitaminA": value,
                "vitaminB12": value,
                "vitaminD": value,
                "riboflavin": value,
                "niacin": value,
                "vitaminE": value
            }}
        }}
        Ensure:
        - The response contains **only JSON** (no markdown, no disclaimers, no explanations).
        - Use numerical values (in grams or milligrams where applicable).
        - If a nutrient is unavailable, set its value to 0.
        """


        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        response_text = response.text.strip()
       
        if response_text.startswith("```json"):
            response_text = response_text[7:] 
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        print(response_text)
    
        try:
            nutrition_data = json.loads(response_text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format received from Gemini API", "raw_response": response_text}

        
        if "calories"and"protien"and"carb" and"fat "and "fiber" and "vitamins"in nutrition_data:
            calories = nutrition_data.get('calories')
            protein  = nutrition_data.get('protein')
            carbs = nutrition_data.get('carbs')
            fat = nutrition_data.get('fat')
            fiber = nutrition_data.get('fiber')
            vitamins = nutrition_data.get('vitamins')
            
            nutrition_data1= Item(calories,protein,carbs,fat,fiber,vitamins)
            
            return nutrition_data1.to_dict()
        else:
            return {"error": "No nutrient data found", "raw_response": nutrition_data}

    