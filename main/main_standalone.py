from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import subprocess

# Kill all chrome-related processes beforehand
subprocess.run(['pkill', 'chrome'],stdout=subprocess.PIPE,universal_newlines=True)


# create a new Chrome session with a little configurations..
def chrome_init(window_size='1920x1080'):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage') 
    options.add_argument('--window-size={}'.format(window_size))
    options.add_argument("--disable-gpu")
    options.add_argument("user-agent=Mozilla/5.0" 
                            + "(Macintosh; Intel Mac OS X 10_12_6)" 
                            + "AppleWebKit/537.36 (KHTML, like Gecko)" 
                            + "Chrome/61.0.3163.100 Safari/537.36"
                        )
    driver = webdriver.Chrome(options=options, executable_path="./chromedriver")
    driver.maximize_window()
    return driver



# Webdriver Control

# -> http://www.yes24.com/24/Category/BestSeller -> Convert a link as URI with parameters as below
# -> Security breach may occur on query parameters -> No Limitation

def url_builder(fetch_size='40', category_number='001', page_number='1'):
    url = ("http://www.yes24.com/24/category/bestseller"
                + "?CategoryNumber={}".format(category_number)
                + "&sumgb=06"
                + "&fetchSize={}".format(fetch_size)
                + "&PageNumber={}".format(page_number)
            )
    return url    



def list_urls(html):
    soup = BeautifulSoup(html, 'lxml')
    divs = soup.find("table",{"id":"category_layout"}).find_all("div",{"class":"goodsImgW"}) # chaining
    urls = [div.find("a",{"href": lambda x:x.startswith("/Product/Goods/")})['href'] for div in divs]
    return urls


def detail_page():
    None





if __name__ == "__main__":

    driver = chrome_init()
    url = url_builder()
    driver.get(url)
    html_source = driver.page_source
    target_urls = list_urls(html_source)
    print(target_urls)

    # BeautifulSoup HTML Parsing

    # Get a table with an id of "category_layout"
    # Iterate table rows in oder to extract detail page links.






    #with open('./results/result.txt', 'w', encoding='utf-8') as yes24Write:
    #    yes24Write.write(driver.page_source)

    driver.close()
