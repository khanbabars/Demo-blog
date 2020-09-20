'''
Created on Sep 6, 2020

@author: shazib
'''

from Apex.Config  import Config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class Web:
    conf = Config()
    def load_apex_application(self):
        user_name   = self.conf.username
        password    = self.conf.password
        driver      = webdriver.Chrome(self.conf.path_to_driver)
        driver.get(self.conf.path_to_web_application)
        
        element = driver.find_element_by_id(self.conf.login_element)
        element.send_keys(user_name)
        element = driver.find_element_by_id(self.conf.password_element)
        element.send_keys(password)
        
        element.send_keys(Keys.RETURN)
        
        delay = 1 # seconds
        try:
            myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, self.conf.region_id)))
            print('============================================')
            print("Page loaded successfully!")
            print("============================================")
            print('')
            print('')
            print('')
            print('extracting elements from the webpage')
            id = []
            data = []
            ####fetch id elements
            id_1 = driver.find_element_by_id(self.conf.element_id_1)
            value = id_1.get_attribute(self.conf.element_value)
            id.append(value)
            
            
            id_2 = driver.find_element_by_id(self.conf.element_id_2)
            value = id_2.get_attribute(self.conf.element_value)
            id.append(value)
       
            
            id_3 = driver.find_element_by_id(self.conf.element_id_3)
            value = id_3.get_attribute(self.conf.element_value)
            id.append(value)
   
            
            id_4 = driver.find_element_by_id(self.conf.element_id_4)
            value = id_4.get_attribute(self.conf.element_value)
            id.append(value)
          
            
            id_5 = driver.find_element_by_id(self.conf.element_id_5)
            value = id_5.get_attribute(self.conf.element_value)
            id.append(value)
            
            
            id_6 = driver.find_element_by_id(self.conf.element_id_6)
            value = id_6.get_attribute(self.conf.element_value)
            id.append(value)
           
            
            
            
            #####fetch data elements
            data_1 = driver.find_element_by_id(self.conf.element_data_1)
            value = data_1.get_attribute(self.conf.element_value)
            data.append(value)
            
            data_2 = driver.find_element_by_id(self.conf.element_data_2)
            value = data_2.get_attribute(self.conf.element_value)
            data.append(value)
            
            data_3 = driver.find_element_by_id(self.conf.element_data_3)
            value = data_3.get_attribute(self.conf.element_value)
            data.append(value)
            
            data_4 = driver.find_element_by_id(self.conf.element_data_4)
            value = data_4.get_attribute(self.conf.element_value)
            data.append(value)
            
            data_5 = driver.find_element_by_id(self.conf.element_data_5)
            value = data_5.get_attribute(self.conf.element_value)
            data.append(value)
            
            data_6 = driver.find_element_by_id(self.conf.element_data_6)
            value = data_6.get_attribute(self.conf.element_value)
            data.append(value)
            print('========================================= ')
            print('Successfully fetched below elements from the webpage' )  
            print('========================================= ')
            print(id, data)
            #####return all values
            driver.quit();
            return id, data
        
           
        except TimeoutException:
            print("Page does not load")
            



