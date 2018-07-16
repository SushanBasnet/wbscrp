class product_entry():

    def __init__(self, index, item_name, item_subtitle='', price='', shipping_price='', link=''):
        self.index = index
        self.item_name = item_name
        self.subtitle = item_subtitle
        self.price = price
        self.shipping_price = shipping_price
        self.total_price = price + shipping_price
        self.link = link

    def __str__(self):
        print("Item: {}\t Price: {}".format(self.item_name, self.price))

