import matplotlib.pyplot as plt
import numpy as np

class PlotPrice:
    def __init__(self):
        self.plot_price = plt.gcf()
        self.draw_plot()

    def draw_price_list_plot(self, price_list, item_list):
        print("dsfjdsfjhdskfhsdkjfhskd")
        print(price_list)
        print(item_list)
        ind = np.arange(len(price_list))
        width = 0.4

        p1 = plt.bar(ind, price_list, width)

        plt.xticks(ind, item_list)
        plt.show()

        self.plot_price = plt.gcf()  # if using Pyplot then get the figure from the plot
        pass

    def draw_plot(self):
        values_to_plot = (100000, 15000000 , 100, 100, 100)
        ind = np.arange(len(values_to_plot))
        width = 0.4

        p1 = plt.bar(ind, values_to_plot, width)

        plt.ylabel('Prices')
        plt.title('Price comparison')
        plt.xticks(ind, ('apple', 'samsung', 'xiaomi', 'huawi', 'LG'))
        plt.yticks(np.arange(2000000, 40000000, 2000000))
        plt.legend((p1[0],), ('Price comparison',))
        self.plot_price = plt.gcf()  # if using Pyplot then get the figure from the plot

    def get_plot(self):
        return self.plot_price