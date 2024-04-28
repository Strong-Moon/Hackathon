from bs4 import BeautifulSoup

# ''r' means read the file only
with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)  # it gives whole  content of file
    # print(soup.prettify())
    # print(course.text) it gives the text inside the tag
    # print(course.h5) it is a way to fins specific thing
    soup = BeautifulSoup(content, 'lxml') # 2nd par. is parser method that we want to use
    course_cards = soup.find_all('div', class_="card") # we have to add underscore because clas is built-in keyword in python
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1] # there are 3 vocabulary, we are splitting with space than take the last element
        
        print(f'{course_name} costs {course_price}')








""" courses_html_tags = soup.find_all("h5") # it finds the first element

for course in courses_html_tags:
    print(course.text) 
this is a way to find all h5 tags content    
"""


""" course_cards = soup.find_all('div', class_="card") # we have to add underscore because clas is built-in keyword in python
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text
        print(course_name)
        print(course_price) 
"""