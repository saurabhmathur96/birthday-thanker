import requests
import json
import urllib

'''
This script replies to the first LIMIT posts on your wall
'''

TOKEN = '' #Insert token here

LIMIT = '10' #Number of posts to be replied to

def comment_on_post(post, message):
    url = 'https://graph.facebook.com/v2.2/%s/comments' % post['id']
    parameters = {'access_token': TOKEN, 'message': message}
    s = requests.post(url, data = parameters)
    return s

def comment_on_posts(posts):
    """Comments on all posts"""
    for post in posts:
        url = 'https://graph.facebook.com/%s/comments' % post['post_id']
        message = 'Commenting through the Graph API'
        parameters = {'access_token': TOKEN, 'message': message}
        s = requests.post(url, data = parameters)


parameters = {'access_token': TOKEN, 'limit': LIMIT}
r = requests.get('https://graph.facebook.com/v2.2/me/feed', params=parameters)
result = json.loads(r.text)
posts = result['data']

for post in posts:
    name = get_first_name(post)
    message = 'Thank You, '+ name
    r = comment_on_post(post, message)
    print r #status of post request
