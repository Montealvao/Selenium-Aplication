import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class License:
    start = Global_Config()
    # start.Start()
    start.Login()
    license = WebDriverWait(start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[1]'))
    )
    license.click() 

    def Licenses(self):
        if(license):
            licenses = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div'))
            )
            licenses.click()
    
    def Products(self):
        if(license):
            products = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[3]/div'))
            )
            products.click()

    def Equipament(self):
        if(license):
            equipament = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[4]/div'))
            )
            equipament.click()

    def Versions(self):
        if(license):
            versions = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[5]/div'))
            )
            versions.click()

    def Catalogue(self):
        if(license):
            catalogue = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[6]/div'))
            )
            catalogue.click()

    def Clients(self):
        if(license):
            clients = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[7]/div'))
            )
            clients.click()

    def Suppliers(self):
        if(license):
            suppliers = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[8]/div'))
            )
            suppliers.click()

if __name__ == "__main__":
    license = License()
    license.Suppliers()
    time.sleep(10)
