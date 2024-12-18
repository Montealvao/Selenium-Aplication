from config.Imports import *
from config.global_config import Global_Config


class License:
    start = Global_Config()
    start.Start()
    start.Login()

    def Licenses(self):
        license = WebDriverWait(self.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[1]'))
        )
        if(license):
            license.click()
            licenses = WebDriverWait(self.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div'))
            )
            licenses.click()

edede = License()
edede.Licenses()