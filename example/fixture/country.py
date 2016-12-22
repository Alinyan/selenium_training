# -*- coding: utf-8 -*-
from model.country import Country
from model.geozone import Geozone
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CountryHelper:

    country_cache = None

    def __init__(self, app):
        self.app = app
        self.wait = WebDriverWait(self.app.wd, 20)

    def get_country(self):
        if self.country_cache is None:
            self.country_cache = []
            for element in self.app.wd.find_elements_by_class_name("row"):
                cells = element.find_elements_by_tag_name("td")
                country = cells[4].text.encode('utf-8')
                count_zones = cells[5].text
                self.country_cache.append(Country(name=country, count_zones=count_zones))
            return list(self.country_cache)

    def get_zone_list_for_county(self, name_country):
        zone_list = []
        self.app.wd.find_element_by_link_text("%s" % name_country).click()
        for element in self.app.wd.find_elements_by_xpath("//table[@id='table-zones']/tbody/tr[not(@*)]"):
            cell = element.find_element_by_xpath("td[3]/input")
            type = cell.get_attribute('type')
            if type == 'hidden':
                zone = cell.get_attribute('value').encode('utf-8')
                zone_list.append(Geozone(name=zone))
        self.app.navigation.open_countries_page()
        return zone_list

    def check_opening_external_links_in_new_window(self):
        main_window = self.app.wd.current_window_handle
        old_windows = self.app.wd.window_handles
        external_links = self.app.wd.find_elements_by_css_selector(".fa-external-link")
        for ext_link in external_links:
            ext_link.click()
            self.wait.until(EC.new_window_is_opened(old_windows))
            new_windows = self.app.wd.window_handles
            new_window = self.get_new_window(old_windows, new_windows)
            self.app.wd.switch_to_window(new_window)
            self.app.wd.close()
            self.app.wd.switch_to_window(main_window)

    def get_new_window(self, old_windows_id_list, new_windows_id_list):
        for new_window_id in sorted(new_windows_id_list):
            for old_window_id in sorted(old_windows_id_list):
                if new_window_id == old_window_id:
                    new_windows_id_list.remove(new_window_id)
        return new_windows_id_list[0]