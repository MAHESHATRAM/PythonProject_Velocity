from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver



class FacebookCreateaccount:
#it takes driver as an argument (webdriver instance) and store it in self.driver so 
#  it can use used in other methods

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.firstName =  (By.NAME, 'firstname')
        self.lastName =  (By.NAME,'lastname')
        self.gender = (By.ID, 'sex')
        self.email = (By.NAME, "reg_email__")
        self.password = (By.NAME,'reg_passwd__')
        self.sigupButton = (By.NAME,"websubmit")

    def enter_firstname(self, username):
        self.driver.find_element(*self.firstName).send_keys(username)

    def enter_lastname(self, password):
        self.driver.find_element(*self.lastName).send_keys(password)
    
    def click_gender(self):
        self.driver.find_element(*self.gender).click()

    def enter_email(self,email):
        self.driver.find_element(*self.email).send_keys(email)
    
    def enter_password(self, pwd ):
        logo = self.driver.find_element(*self.password).send_keys(pwd)
  
    def clcik_signup(self):
        self.driver.find_element(*self.sigupButton).click()