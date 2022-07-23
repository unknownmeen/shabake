from bs4 import BeautifulSoup
import requests

class ScrapEmallsSite:
    def __init__(self, values):
        self.ui_information_dict = values
        self.price_list = list()
        self.item_list = list()

    def set_price_list(self, soup):
        span_list = soup.find_all("span", {"class": "item-price"})
        for span in span_list:
            try:
                self.price_list.append(span.contents[0])
            except:
                True

    def get_price_list(self):
        return self.price_list

    def set_item_list(self, soup):
        div_list = soup.find_all("div", {"class": "item-title"})
        # print("div_list: ", div_list)
        for div in div_list:
            try:
                self.item_list.append(div.contents[1]["href"].split("_")[1].split("-Mobile")[0])
            except:
                True
        print(div_list)

    def get_item_list(self):
        return self.item_list

    def scrap_page(self, window):
        brand_name = self.ui_information_dict["company"]
        page_number = self.ui_information_dict["page_number"]
        url = f"https://emalls.ir/%D9%85%D8%AD%D8%B5%D9%88%D9%84%D8%A7%D8%AA~Category~39~b~{brand_name}~page~{page_number}"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        self.set_price_list(soup)
        self.set_item_list(soup)

        for (item, price) in zip(self.get_item_list(), self.get_price_list()):
            window["output"].print([str(item), str(price)])

        window["url"].update(value=url)
        print([str(self.ui_information_dict)])