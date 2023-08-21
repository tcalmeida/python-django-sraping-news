from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from urllib.parse import urlparse
import pandas as pd

# path = '../geckodriver.exe'


def collect_gamerant_data(url, news_path, title_path, link_path):

    # active headless-mode
    options = Options()
    options.headless = True

    service = Service()
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(url)

    news_containers = driver.find_elements(by="xpath", value=news_path)

    titles = []
    links = []

    for news in news_containers:
        title = news.find_element(by='xpath', value=title_path).text
        link = news.find_element(by='xpath', value=link_path).get_attribute('href')
        titles.append(title)
        link_parse = urlparse(link)
        links.append(link_parse.path)

    news_dict = {'Titles': titles, 'Links': links}
    latest_news = pd.DataFrame(news_dict)
    latest_news.to_csv("gamerant.csv")

    return zip(titles, links)

    driver.quit()