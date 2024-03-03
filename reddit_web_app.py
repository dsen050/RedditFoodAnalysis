from Top_Food_Reddit import *
from yelp_api import *
from sentiment_analysis import *
import pandas as pd
import streamlit as st
import numpy as np
from nltk.sentiment import SentimentIntensityAnalyzer

#reddit info
client_id = "client_id"
client_secret = "client_secret"
user_agent = "my user agent"
api_key = 'api_key'

st.title('Reddit Cuisine')

#user enters type of cuisine

cuisine = st.sidebar.text_input("Enter the type of cuisine here")


#user enters location

location = st.sidebar.text_input("Enter the location (city, state)")

#table from reddit is produced

search_query = f"Best {cuisine} food in {location} reddit"

# st.sidebar.write(search_query)

food_parse = RedditParsing(client_id, client_secret, user_agent)

num_results = 3
google_results = food_parse.search_google(search_query, num_results)

posts_df = pd.DataFrame(columns = ['title', 'top_comment_score', 'top_comment'])
if google_results:
    # Store entire post objects in a list
    for result_url in google_results:
        post_info = food_parse.scrape_data_from_reddit(result_url)
        posts_df = pd.concat([posts_df, post_info], ignore_index = True)

else:
    print("no results found")

posts_df = posts_df.reset_index(drop=True)
if cuisine and location:
    st.table(posts_df)
    restaurant_name = st.sidebar.text_input("Enter a restaurant based on selection")
    location_new = st.sidebar.text_input("Enter the location for this restaurant")

    # Get reviews from yelp
    if restaurant_name and location_new:
        analyzer = YelpSearchAPI(api_key)
        results = analyzer.search_restaurant(restaurant_name, location_new)

        if results:
            restaurant = results[0]  # Assuming the first result is the restaurant you're looking for
            # print("Name:", restaurant["name"])
            # print("Address:", ", ".join(restaurant["location"]["display_address"]))
            # print("Phone:", restaurant["phone"])
            # print("Rating:", restaurant["rating"])
            # print("Reviews:", restaurant["review_count"])

            # Get the reviews if available
            reviews = analyzer.get_reviews(restaurant["id"])
            if reviews:
                # print(reviews)

                review_res = {}
                for review in reviews:
                    id = review['id']
                    rev = review['text']
                    review_res[id] = rev

                df = pd.DataFrame(review_res.items(), columns=(['id', 'reviews']))
                analyze_sentiment = SENTIMENT_ANALYZER(df)
                df_sentiment = analyze_sentiment.sentiment()
                df = df.merge(df_sentiment, on=['id'])
                st.table(df[['reviews', 'compound']])
                # st.write(df_sentiment.columns)
            else:
                print("No reviews found.")
        else:
            print("No results found.")
    else:
        st.write('enter a restaurant you would like to get additional details on')
else:
    st.write('Enter information on the side bar')

# st.write(posts_list)

#ask for a restaurant from list



#grab sentiment analysis from yelp

