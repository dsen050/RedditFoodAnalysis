import requests
import pandas as pd


class YelpSearchAPI:
    def __init__(self, api_key):
        self.api_key = api_key
    def search_restaurant(self, term, location):
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        params = {
            "term": term,
            "location": location,
            "limit": 1  # Limiting to 1 result
        }
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        return data["businesses"]

    def get_reviews(self, business_id):
        url = f"https://api.yelp.com/v3/businesses/{business_id}/reviews"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        response = requests.get(url, headers=headers)
        data = response.json()
        return data["reviews"]

