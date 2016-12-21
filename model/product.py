# -*- coding: utf-8 -*-

class Product:
    def __init__(self, id=None, name=None, code=None, quantity=None, keywords=None,
                 description=None, head_title=None, short_description=None, meta_description=None, purchase_price=None,
                 pricesUSD=None, pricesEUR=None):
        self.id = id
        self.name = name
        self.code = code
        self.quantity = quantity
        self.keywords = keywords
        self.description = description
        self.head_title = head_title
        self.short_description = short_description
        self.meta_description = meta_description
        self.purchase_price = purchase_price
        self.pricesUSD = pricesUSD
        self.pricesEUR = pricesEUR

    def __repr__(self):
        return "%s" \
               % (self.name)

    def __eq__(self, other):
        return (self.name is None or other.name is None or str(self.name) == str(other.name))

    def name_product(self):
        return self.name


