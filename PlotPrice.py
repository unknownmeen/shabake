import matplotlib.pyplot as plt
import numpy as np
from unidecode import unidecode as p2e

class PlotPrice:
    def __init__(self):
        self.plot_price = plt.gcf()
        self.draw_intial_plot()

        self.length = 5
        self.point = 0

        self.item_list = list()
        self.price_list = list()

    def set_item_list(self, item_list):
        self.item_list = item_list

    def set_price_list(self, price_list):
        self.price_list = price_list

    def next(self):
        self.point += self.length

    def prev(self):
        self.point -= self.length

    def draw_price_list_plot(self):
        plt.clf()
        ind = np.arange(len(self.price_list[self.point:self.point + self.length]))
        width = 0.4
        prices_list = list()

        for price in self.price_list:
            split_with_camma = p2e(price.split(" ")[0]).split(",")
            number = str()
            for split_part in split_with_camma:
                number += split_part
            prices_list.append(int(number))

        print(prices_list)
        p1 = plt.bar(ind, prices_list[self.point:self.point + self.length], width)

        plt.xticks(ind, self.item_list[self.point:self.point + self.length])
        ax = plt.gca()
        ax.tick_params(axis='x', labelrotation=45)
        ##plt.yticks(1, 2)
        # plt.show()
        plt.legend((p1[0],), ('Price comparison',))
        self.plot_price = plt.gcf()  # if using Pyplot then get the figure from the plot
        # ٍ

    def draw_intial_plot(self):
        values_to_plot = (0, 0 , 0, 0, 0)
        ind = np.arange(len(values_to_plot))
        width = 0.4

        p1 = plt.bar(ind, values_to_plot, width)

        plt.ylabel('Prices')
        plt.title('Price comparison')
        plt.legend((p1[0],), ('Price comparison',))
        self.plot_price = plt.gcf()  # if using Pyplot then get the figure from the plot

    def get_plot(self):
        return self.plot_price