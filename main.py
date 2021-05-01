import requests
from bs4 import BeautifulSoup


def get_Product_Information(URL, headers):

    # Getting the html page
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    # Extracting the title of the product
    title = soup.find(class_="product-header__title").get_text()

    # Extracting the price of the product
    price_class = soup.find(class_="Data-n9fk43-0 jPJDmG")
    price = price_class['data-integer']

    return title, int(price)


def main():

    #Defaining the price range when we want to get a notification
    alarm_price = 399

    # Specifying the page (the item) that we want to track
    URL = 'https://www.verkkokauppa.com/fi/product/13289/nmhkj/Apple-iPhone-SE-64-Gt-puhelin-musta?list=OZCYkRirLCyir8gvirLSKirL88irLdWir8S9irLgjirn8qir8dDit6Az9MR69OiklaN'

    # Used to get the right information about the browser
    headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:88.0) Gecko/20100101 Firefox/88.0'}

    title, price = get_Product_Information(URL, headers)

    #Checking if the price has fell down the critical points
    if(price < alarm_price):
        print("HÄLYTYS!\n Hinta on tippunut tuotteessa: '%s'\nHinta: %s€"% (title, price))
    else:
        print("Kaikki ok\nTuotteen '%s' hinta on edelleen %d€" % (title, price))

    return None


main()

############################### EOF ###############################
