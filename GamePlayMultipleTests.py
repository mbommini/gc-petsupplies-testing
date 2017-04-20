# -*- coding: utf-8 -*-
#!/usr/bin/python
# Program to test whether the start button can be clicked 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import unittest
import config

class GamePlayTest (unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        #global driver
        inst.browserdriver = webdriver.Chrome('chromedriver') 
        inst.browserdriver.maximize_window()
        
        try:
            inst.browserdriver.get(config.url)
        except Exception as exc:
            config.error('Error in page in browser: Exception: %s' % (exc))
              
        
        #inst.driver = config.loadWebDriver(inst.driver)
        #global start_time
        inst.start_time = time.time()
        #global element
        try:
            inst.element = config.ensureCanvasIsClickable(inst.browserdriver)
            """wait = WebDriverWait(inst.browserdriver, config.pageloaddelayduration)
            inst.element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'canvas')))"""

        except Exception as exc:
            config.error('Error in waiting for clickable canvas: Exception: %s' % (exc))
        
    

  
 
  
    def test_loadDuration(self):
        loadduration = time.time() - self.start_time
        config.log("--- %s seconds to load and display the page ---" % loadduration)
        if (loadduration > config.maximumtimetoloadduration):
            config.log("Testcase failed: Page load took %s seconds" %loadduration)
        else:
            config.log("Testcase passed: Page loaded by %s seconds" %loadduration)
        self.assertLessEqual(loadduration,config.maximumtimetoloadthepage)
        config.show("Asserted:Page load duration is <= %d" %(config.maximumtimetoloadthepage))
    
    
    def test_startButton_click(self): 
        try:
            xTarget = self.element.size['width']*0.5
            yTarget = self.element.size['height']*0.75
            config.clickMouseAtXY(self.browserdriver, self.element, xTarget, yTarget)
            config.show("Testcase passed: Start button clicked")
            
        except Exception as exc:
            config.error('Error in clicking start button: Exception: %s' % (exc))	
            config.error("Testcase failed: Start button could not be clicked")
    
        try:
            config.asserturl(self.browserdriver, config.assertpage)
            config.show("Url %s asserted" %(config.assertpage))
            
        except Exception as exc:
            config.error('Assert page for %s failed: Exception: %s' % (config.assertpage, exc))
    
    @classmethod    
    def tearDownClass(inst):
        #Set the sleep so that next page is visible
        time.sleep(config.pagedisplayduration)
        
        # Close and quit the driver
        #config.closeWebDriver()
        inst.browserdriver.close()
        inst.browserdriver.quit()
        
if __name__ ==  "__main__":
    unittest.main()
   