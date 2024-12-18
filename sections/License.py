import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class License:
    start = Global_Config()
    start.Start()
    start.Login()

    def Licenses(self):
        license = WebDriverWait(self.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[1]'))
        )
        if(license):
            license.click()
            licenses = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div'))
            )
            licenses.click()

if __name__ == "__main__":
    license = License()
    license.Licenses()
