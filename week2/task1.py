from bs4 import BeautifulSoup

"""
Task 1: Extract State Names:

Extract the names of the states (Arizona, California) from the "locations" section.
"""
with open ('/Users/mistarkelly/ubuntu_shared/My-Projects/ALX-ONLY/AirBnB_clone/web_static/8-index.html','r') as file_html:
    content = file_html.read()
    soup = BeautifulSoup(content, 'lxml')
    states_div = soup.find('div', class_='locations')
    states = states_div.find('h3').text.strip()
    states_names = states_div.find('h4').text.strip()
    if __name__ == "__main__":
        print(f"all states in location div are {states}: {states_names}")
