from flask import Flask, request, jsonify
import google.generativeai as genai 
import json
from app.Models.Item import Item

genai.configure(api_key="add_your_key")  # Rep
def get_nutrition_info(food_item, weight):
    try:
        # Define prompt
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

        # Call Gemini API
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        print(response)
        # Clean the response text (Remove backticks)
        response_text = response.text.strip()
       
        if response_text.startswith("```json"):
            response_text = response_text[7:]  # Remove ```json
        if response_text.endswith("```"):
            response_text = response_text[:-3]  # Remove ```
        print(response_text)
        # Convert response to JSON
        try:
            nutrition_data = json.loads(response_text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format received from Gemini API", "raw_response": response_text}

        # Extract only calorie and nutrient information
        if "calories"and"protien"and"carb" and"fat "and "fiber" and "vitamins"in nutrition_data:
            calories = nutrition_data.get('calories')
            protein  = nutrition_data.get('protein')
            carbs = nutrition_data.get('carbs')
            fat = nutrition_data.get('fat')
            fiber = nutrition_data.get('fiber')
            vitamins = nutrition_data.get('vitamins')
            
            nutrition_data1= Item(calories,protein,carbs,fat,fiber,vitamins)
            print(nutrition_data1)
            return nutrition_data1.to_dict()
        else:
            return {"error": "No nutrient data found", "raw_response": nutrition_data}

    except Exception as e:
        return {"error": str(e)}