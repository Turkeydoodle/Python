from requests import *
response = get("https://www.wikipedia.org/")
print(str(response) + ', because wikipedia blocks bots')
response = get("https://www.google.com/realornot")
print(str(response)+', because google.com/realornot does not exist')
response = get("https://real-frogger.neocities.org/")
print(str(response)+', because real-frogger.neocities.org does exist')

def parse(text):
    chomp('<', text)
    website = parse_html(text)
def chomp(text, body):
    extract = body[:len(text)]
    if extract == text:
        return body[len(text):]
    else:
        raise ValueError("Expected " + text + ", got " + extract)

#define parse head and parse body

def parse_html(text):
    chomp('<html>', text)
    #parse_and_text = parse_head(text)
    #parse = parse_body(text)
    chomp('</html>', text)
    #return {'head': parse_and_text, 'body': parse}
parse(response.text)