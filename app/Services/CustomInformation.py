#This service provides information with response to the "Other questions" from the HOME page.

from flask import Flask, request, jsonify
import google.generativeai as genai 
import json
from app.Models.Item import Item

genai.configure(api_key="AIzaSyBigK0uLo3k4vnDEuWiN8UISblre4SCSxQ") 
def get_custom_info(food_item, weight,custom):
 
        prompt = f"""
        Provide a JSON response answering the {custom} for {weight}g of {food_item}.
        The response must be structured as follows:
        {{
            {custom}:value
        }}
        Ensure:
        - The response contains only 1-3 line sentence.
        - The response should not contain more than 3 sentence.
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
            custom_data = json.loads(response_text)
        except json.JSONDecodeError:
            return {"error": "Invalid JSON format received from Gemini API", "raw_response": response_text}
        print(custom_data)
    
        if (custom_data):
            return custom_data
        else:
            return {"error": "No nutrient data found", "raw_response": custom_data}

   