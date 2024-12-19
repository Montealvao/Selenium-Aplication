import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class Administration:
    start = Global_Config()
    # start.Start()
    start.Login()
    administration = WebDriverWait(start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[1]'))
    )
    administration.click() 

    def Clients(self):
        if(administration):
            clients = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[2]/div'))
            )
            clients.click()
    
    def Manual(self):
        if(administration):
            manual = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[3]/div'))
            )
            manual.click()

    def Suppliers(self):
        if(administration):
            suppliers = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[1]/div[4]/div'))
            )
            suppliers.click()

if __name__ == "__main__":
    administration = Administration()
    administration.Clients()
    time.sleep(10)