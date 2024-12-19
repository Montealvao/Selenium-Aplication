import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class Authentication:
    start = Global_Config()
    # start.Start()
    start.Login()
    authentication = WebDriverWait(start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[1]'))
    )
    authentication.click() 

    def Groups(self):
        if(authentication):
            groups = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[2]/div'))
            )
            groups.click()
    
    def Users(self):
        if(authentication):
            users = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[2]/div[3]/div'))
            )
            users.click()

if __name__ == "__main__":
    authentication = Authentication()
    authentication.Groups()
    time.sleep(10)