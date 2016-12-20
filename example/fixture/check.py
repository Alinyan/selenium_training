# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from model.country import Country

class CheckHelper:

    def __init__(self, app):
        self.app = app

    def check_count_sticker_product(self):
        # проходим цикл по всем продуктам, содержащим стикер
        list_product = self.app.wd.execute_script("return $('.image-wrapper')")
        for product in list_product:
             count_sticker = len(product.find_elements_by_class_name('sticker'))
             assert count_sticker == 1

    def check_sorting_zones(self):
        country_list = []
        for element in self.app.wd.find_elements_by_class_name("row"):
            cells = element.find_elements_by_tag_name("td")
            id = cells[2].text
            country = cells[4].text.encode('utf-8')
            count_zones = cells[5].text
            country_list.append(Country(id=id, name=country, count_zones=count_zones))
        sorted_country_list = sorted(country_list, key=Country.name)
        assert sorted_country_list == country_list





