# Calorie & Nutrition API (Flask) 

This is a **Flask API** that provides **calorie requirements, nutrition details, and user authentication**.  
It integrates with **Google Gemini API** to fetch **calorie estimates** based on **age and weight**.

---

## **Features**
Fetch **nutrition information** (protein, carbs, fat, vitamins) for a given food item  
Calculate **daily calorie requirement** based on weight and age  
User **authentication system** (Registration & Login)  
**JWT authentication** for secure endpoints  
**CORS enabled** for frontend integration  

---

## ** Setup & Installation**

```bash
git clone https://github.com/VigneshwarRaj7/Backend-CalorieInfo.git
cd Backend-CalorieInfo

TRY:
    pip install -r requirements.txt
    python main.py -> to run
ELSE:
    pip install flask
    pip install flask-cors  
    pip install flask-jwt-extended  
    pip install requests  
    pip install google-generativeai
    python main.py