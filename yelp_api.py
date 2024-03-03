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

# Replace 'YOUR_API_KEY' with your actual Yelp API key
# api_key = 'aeUNyZ6qhJypkk0EwziKg2WH5Z_giVGlwbuWs4ncp2vIQKn6E_ymy62-ItCGIQswLd0Hh2H3XkXRL1jD-YhxZxQUwReOF9v6My78B2g2hzGyhJ8e4pfy6V2mXzrSZXYx'
#
# # Replace 'Restaurant Name' with the name of the restaurant you want to search for
# restaurant_name = "Oleana"
#
# # Replace 'Location' with the location where you want to search for the restaurant
# location = 'Cambridge, MA'
#
# analyzer = YelpSearchAPI(api_key)
#
# results = analyzer.search_restaurant(restaurant_name, location)
# if results:
#     restaurant = results[0]  # Assuming the first result is the restaurant you're looking for
#     print("Name:", restaurant["name"])
#     print("Address:", ", ".join(restaurant["location"]["display_address"]))
#     print("Phone:", restaurant["phone"])
#     print("Rating:", restaurant["rating"])
#     print("Reviews:", restaurant["review_count"])
#
#     # Get the reviews if available
#     reviews = analyzer.get_reviews(restaurant["id"])
#     if reviews:
#         # print(reviews)
#
#         review_res = {}
#         for review in reviews:
#             id = review['id']
#             rev = review['text']
#             review_res[id] = rev
#
#         df = pd.DataFrame(review_res.items(), columns=(['id', 'reviews']))
#         print(df.head())
#     else:
#         print("No reviews found.")
# else:
#     print("No results found.")