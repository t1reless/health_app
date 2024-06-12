import json 
import requests

def calorie_and_nutrition_fetcher(food):
  url = f"https://trackapi.nutritionix.com/v2/natural/nutrient"
  headers = {"Content-Type":"application/json",
            
