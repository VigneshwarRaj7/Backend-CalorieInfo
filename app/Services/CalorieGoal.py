#This service provides information of required calories per day.
#This service responds to the request that is being generated from Calorie Guide page.

import google.generativeai as genai
import json


genai.configure(api_key="AIzaSyBigK0uLo3k4vnDEuWiN8UISblre4SCSxQ")  

def get_calorie_goal(weight, age):

        prompt = f"""
        Given the details:
        - Weight: {weight} kg
        - Age: {age} years
        

        Calculate and return ONLY the daily calorie requirement for this person.
        Respond with a single number (calories per day) and NO additional text, disclaimers, or explanations.
        """

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)

        response_text = response.text.strip()
 
        response_text = response_text.replace(",", "").split("\n")[0]

        
        try:
            calorie_goal = int(response_text)
            return {"calories_per_day": calorie_goal}
        except ValueError:
            return {"error": "Invalid response format from Gemini API", "raw_response": response_text}
