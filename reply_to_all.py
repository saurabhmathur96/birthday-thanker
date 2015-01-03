"""
This script replies to the first LIMIT posts on your wall
"""

import requests
import json


TOKEN = '' #Insert token here
LIMIT = '10' #Number of posts to be replied to
    

def comment_on_post(post, message):
    """ makes a POST request to facebok that comments on a post """
    url = 'https://graph.facebook.com/v2.2/%s/comments' % post['id']
    parameters = {'access_token': TOKEN, 'message': message}
    s = requests.post(url, data = parameters)
    return s

def get_first_name(post):
    """ returns first name of poster from post dict """
    return post['from']['name'] 

def main():
    """ main function """
    parameters = {'access_token': TOKEN, 'limit': LIMIT}
    r = requests.get(
        'https://graph.facebook.com/v2.2/me/feed', 
        params=parameters
    )
    result = json.loads(r.text)
    posts = result['data']

    for post in posts:
        name = get_first_name(post)
        message = 'Thank You, '+ name
        r = comment_on_post(post, message)
        print r #status of post request
        
if __name__ == '__main__':
    main()
