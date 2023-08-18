from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from urllib.parse import urlparse
import pandas as pd

# path = '../geckodriver.exe'


class News:

    def __init__(self, website, news_path, title_path, link_path):
        self.website = website
        self.news_path = news_path
        self.title_path = title_path
        self.link_path = link_path

    def collect_news_data(self):
        website = self.website

        # active headless-mode
        options = Options()
        options.headless = True

        service = Service()
        driver = webdriver.Firefox(service=service, options=options)
        driver.get(website)

        news_containers = driver.find_elements(by="xpath", value=self.news_path)

        titles = []
        links = []

        for news in news_containers:
            title = news.find_element(by='xpath', value=self.title_path).text
            link = news.find_element(by='xpath', value=self.link_path).get_attribute('href')
            titles.append(title)
            link_parse = urlparse(link)
            links.append(link_parse.path)

        # news_dict = {"Titles": titles, "Links": links}
        # latest_news = pd.DataFrame(news_dict)
        # latest_news.to_csv("gamerant.csv")

        return zip(titles, links)

        driver.quit()
