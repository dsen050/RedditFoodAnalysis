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



