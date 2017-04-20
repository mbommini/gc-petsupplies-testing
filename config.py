#!/usr/bin/python
#config.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import sys

#url which should be parsed. Should be converted to accept the passed arguments 
url="http://petsuppliesplus.gamecommerce.com/FindDifferenceMultiLevelPhaser.build/adz.html?campaign_id=PSP-TR-FL-LAN4011-3"
getcouponurl = "https://www.petsuppliesplus.com/coupon.jsp?pageName=20161216_4011_GO_89599"
facebookurl = "https://www.facebook.com/"

#Seconds by which the page should be displayed 
pagedisplayduration=10

#Seconds by which the webdriver should poll to ensure the DOM elements are loaded in the page and program can find an element or elements
pageloaddelayduration=30

#Seconds by which the page should be loaded 
maximumtimetoloadduration=5

#Seconds by which the time's up screen should appear after losing the game 
times_up_button_load_duration=40

#Maximum time to load the page given below. This is used in the load page duration t/c
maximumtimetoloadthepage=5

#Email id to which email should be sent
emailtoreceive='mbommini@gmail.com'

#assertpage="petsuppliesplus.gamecommerce.com"
assertpage="Game Commerce"
assertcouponpage="Pet Supplies Plus"
assertfacebookpage="Facebook"



##################################################
#
#  Set the DEBUG to True when you want to see the log messages
#  Set the DEBUG to False when you want dont want to see any log messages
#
##################################################    
DEBUG = True
#DEBUG = False


##################################################
#
#  log() prints the received arguments to the standard output if DEBUG is set to True
#  Expected input is the string
#
##################################################  
def log(s):
    if DEBUG:
        print (s)

##################################################
#
#  show() print the messages to the standard output
#  Expected input is the string 
#
##################################################  
def show(s):
    print (s)
    
##################################################
#
#  error() print the messages to the standard output
#  Expected input is the string 
#
##################################################      
def error(s):
    print (s)

 
    
##################################################
#
#  Function to execute java script code and return the value 
#
##################################################    
def execute_script(s):
    output=browserdriver.execute_script(s);
    return output
    
##################################################
#
#  Debug the clicks on the page ( the clicks and details 
#  are printed to the console )
#
##################################################
def debugClicksOnUI():
    log('Registering debug for clicks')
    # Script to setup the debug click information
    # We want this to print during the capturing phase
    script = "var debugBody = document.getElementsByTagName('body')[0];"
    script += "debugBody.addEventListener('click', function(ev) {console.log('clicked at x =['+ev.clientX+'] y =['+ev.clientY+']'); console.log(ev); }, true);"
    browserdriver.execute_script(script)
    
##################################################
#
#  Clicks at the XTarget and YTarget on the element 
#  Arguments : element, X position, Y position
#
##################################################
def clickMouseAtXY(browserdriver, element, xTarget, yTarget):
        actions = ActionChains(browserdriver)
        actions.move_to_element_with_offset(element, xTarget, yTarget)
        actions.click()
        actions.perform()
        actions.release()

##################################################
#
#  Ensure canvas is clickable 
#  Returns the clickable webelement 
#
##################################################        
def ensureCanvasIsClickable(browserdriver):
    wait = WebDriverWait(browserdriver, pageloaddelayduration)
    element = wait.until(EC.element_to_be_clickable((By.TAG_NAME, 'canvas')))
    return element
    
##################################################
#
#  Loads the url 
#  Returns none 
#
##################################################     
def loadWebDriver(browserdriver):
    #page to determine which browser should be used. Should be converted to accept the passed arguments 
    #browserdriver = webdriver.Firefox() 
    #global browserdriver
    browserdriver = webdriver.Chrome('chromedriver') 
    browserdriver.maximize_window()
    browserdriver.get(url)
    return browserdriver

##################################################
#
#  Closes the url and quits it 
#  Returns none 
#
##################################################     
def closeWebDriver():
    browserdriver.close()
    browserdriver.quit()    

    
def sendEmail(s):
    elem = browserdriver.switch_to_active_element()
    elem.send_keys(s)
    elem.send_keys(Keys.ENTER)
    log('Sent the email id to the web')

 
    
def useHiddenWebElement(s):
    exestr ='var inputElem = document.createElement("input");'
    exestr += 'inputElem.type = "hidden";'
    exestr += 'inputElem.id = "testElement";'
    exestr += 'inputElem.name = "testElement";'
    exestr += 'inputElem.value = "'+s+'";'
    exestr += 'document.body.appendChild(inputElem);'
    exestr += 'console.log("window.innerHeight :"+window.innerHeight);'
    browserdriver.execute_script(exestr);    
    input = browserdriver.find_element_by_name("testElement")
    #localpythonvariable = input.get_attribute("value")
    log('Extracted value from testElement in web: %s' %(input.get_attribute("value")))    
    
def asserturl(browserdriver, s):
    assert s in browserdriver.title