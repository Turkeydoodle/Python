from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Turkeydoodle Page</title></head>
<body>
<p class="title"><b>Turkeydoodle Example</b></p>
<p class="story">Once upon a time there were three turkeys;
<a href="http://example.com/turkey1" class="turkey" id="link1">Turkey 1</a>,
<a href="http://example.com/turkey2" class="turkey" id="link2">Turkey 2</a> and
<a href="http://example.com/turkey3" class="turkey" id="link3">Turkey 3</a>;
they lived happily ever after.</p>
</body></html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Print the title of the page
print("Title:", soup.title.string)

# Find all links with class 'turkey'
for link in soup.find_all('a', class_='turkey'):
    print("Link text:", link.get_text(), "| URL:", link['href'])