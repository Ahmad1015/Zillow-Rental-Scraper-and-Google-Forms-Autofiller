from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
'''[0:6]'''
def main():
    scrapping_data()


def scrapping_data():
    link = 'https://www.zillow.com/los-angeles-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.88551790039062%2C%22east%22%3A-117.93794709960937%2C%22south%22%3A33.674345035497645%2C%22north%22%3A34.36638498534224%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A4500%7D%2C%22price%22%3A%7B%22max%22%3A863182%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    
    headers={'User-Agent': 'Mozilla/5.0'}

    webpage = requests.get(url=link, headers=headers)

     
    soup = BeautifulSoup(webpage.text, "html.parser")

    price = [item.getText().strip() for item in soup.find_all(class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")]


    address = [item.getText() for item in soup.find_all(name = "address")]
    print(address)

    anchor_tag = soup.find('a', {'data-test': 'property-card-link'})

    # Extract the 'href' attribute value from the anchor tag
    href_link = anchor_tag['href'] if anchor_tag else None

    print(href_link)



    for iteration in range(0,2):
        link = f"https://www.zillow.com/los-angeles-ca/rentals/{iteration}_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A3%7D%2C%22usersSearchTerm%22%3A%22Los%20Angeles%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-118.88551790039062%2C%22east%22%3A-117.93794709960937%2C%22south%22%3A33.674345035497645%2C%22north%22%3A34.36638498534224%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12447%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22beds%22%3A%7B%22min%22%3A1%7D%2C%22baths%22%3A%7B%22min%22%3A1%7D%2C%22price%22%3A%7B%22max%22%3A863182%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A4500%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
        webpage = requests.get(url=link,headers=headers)
        soup = BeautifulSoup(webpage.text, "html.parser")
        price2 = [item.getText().strip() for item in soup.find_all(class_="PropertyCardWrapper__StyledPriceLine-srp__sc-16e8gqd-1 iMKTKr")]
        address2 = [item.getText() for item in soup.find_all(name="address")]
        address = address + address2
        price = price+price2







    

    
                                                    
    
    




def autofilling_google_forms():
    pass







if __name__ == "__main__":
    main()