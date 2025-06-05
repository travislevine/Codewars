import urllib.parse
def generate_link(user):
    safe_user = urllib.parse.quote(user)
    url = "http://www.codewars.com/users/" + safe_user
    return url

    #https://www.codewars.com/kata/57037ed25a7263ac35000c80/train/python
    #You have passed all of the tests! :)
    