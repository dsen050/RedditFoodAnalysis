import praw
import pandas as pd
from googlesearch import search

client_id = "client_id"
client_secret = "client_secret"
user_agent = "my user agent"

class RedditParsing:
    def __init__(self, client_id, client_secret, user_agent):
        self.reddit = praw.Reddit(
            client_id = client_id,
            client_secret = client_secret,
            user_agent = user_agent)


    def search_google(self, query, num_limit=3):
        # Use the googlesearch-python library to search Google
        results = list(search(query,  num_results=num_limit))
        return results


    def get_top_comment(self, submission):
        # Get the top comment by most likes in the submission
        submission.comments.replace_more(limit=0)
        top_comment = max(submission.comments, key=lambda comment: comment.score, default=None)

        if top_comment:
            return [top_comment.body, top_comment.score]
        else:
            return "No comments"


    def scrape_data_from_reddit(self, post_url):
        # Extract relevant information from the Reddit post using PRAW
        submission = self.reddit.submission(url=post_url)
        # print(submission.title)

        top_comment = self.get_top_comment(submission)

        # Create a dictionary with post title as key and top comment as value
        post_dict = {
            'title': [submission.title],
            # 'url': submission.url,
            'top_comment_score': [top_comment[1]],
            # 'num_comments': submission.num_comments,
            'top_comment': [top_comment[0]]
        }
        # print(post_dict)
        df_return = pd.DataFrame.from_dict(post_dict)
        # print(df_return)
        return df_return


# Example usage
# browse = RedditParsing(client_id, client_secret, user_agent)
# google_query = "Best mexican food in boston reddit"
# num_results = 3  # You can adjust this based on your needs
# google_results = browse.search_google(google_query, num_results)
# #
# posts_df = pd.DataFrame(columns = ['title', 'score', 'top_comment'])
# if google_results:
#     # Store entire post objects in a list
#     for result_url in google_results:
#         post_info = browse.scrape_data_from_reddit(result_url)
#         posts_df = pd.concat([posts_df, post_info], ignore_index = True)
#
# else:
#     print("no results found")
#
# print(posts_df)

#
#
#
# print(posts_list)
# for post in posts_list:
#         # print(f'Title: {post.title}')
#         # print(f'URL: {post.url}')
#         # print(f'Score: {post.score}')
#         top_comment = post['top_comment'][0]
#         score = post['top_comment'][1]
#         print(f"Top comment: {top_comment} \n Score: {score}")
#         print('---')

