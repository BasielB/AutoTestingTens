from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class YandexSearch (unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://yandex.ru")
        time.sleep(2)

    def test_01(self):
        driver = self.driver

        assert driver.find_element_by_id("text")

        input_field = driver.find_element_by_id("text")
        input_field.send_keys("Тензор")
        time.sleep(5)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]")))

        assert driver.find_element_by_xpath("/html/body/div[5]")

        input_field.send_keys(Keys.ENTER)

        time.sleep(5)

        assert driver.find_element_by_tag_name("ul")

        links = driver.find_elements_by_css_selector("h2 > a")


        def Link_in_list():
            for i in range(5):
                a = str(links[i].get_attribute("href"))
                if a == "https://tensor.ru/":
                    return True

        assert Link_in_list()


    def test_02(self):
        driver = self.driver

        assert driver.find_element_by_link_text('Картинки')

        img_link = driver.find_element_by_link_text('Картинки')
        img_link.click()

        time.sleep(5)

        assert driver.current_url == "https://yandex.ru/images/"

        assert driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[1]/div/a')

        first_img = driver.find_element_by_xpath('//*[@id="main"]/div/div/div[1]/div[1]/div/a')
        first_img.click()

        time.sleep(3)

        assert driver.find_element_by_class_name("image__image")

        first_img_open = driver.find_element_by_class_name("image__image")

        first_img_open_link = first_img_open.get_attribute("src")

        btn_forward = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/a')
        btn_forward.click()

        second_img_open = driver.find_element_by_class_name("image__image")

        second_img_open_link = second_img_open.get_attribute("src")

        assert second_img_open_link != first_img_open_link

        btn_back = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[2]/div[1]/a')
        btn_back.click()

        third_img_open = driver.find_element_by_class_name("image__image")

        third_img_open_link = third_img_open.get_attribute("src")

        assert third_img_open_link == first_img_open_link





    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()