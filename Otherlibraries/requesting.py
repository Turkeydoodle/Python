from requests import *
response = get("https://www.wikipedia.org/")
print(str(response) + ', because wikipedia blocks bots')
response = get("https://www.google.com/realornot")
print(str(response)+', because google.com/realornot does not exist')
response = get("https://real-frogger.neocities.org/")
print(str(response)+', because real-frogger.neocities.org does exist')