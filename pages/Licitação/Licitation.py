import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class Licitation:
    start = Global_Config()
    # start.Start()
    start.Login()
    licitation = WebDriverWait(start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[3]/div[1]'))
    )
    licitation.click() 

    def Licitations(self):
        if(licitation):
            licitations = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[3]/div[2]/div'))
            )
            licitations.click()
    
    def Closed(self):
        if(licitation):
            closed = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[3]/div[3]/div'))
            )
            closed.click()

    def Prospected_Opportunities(self):
        if(licitation):
            prospected_Opportunities = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[3]/div[4]/div'))
            )
            prospected_Opportunities.click()

    def Calendar(self):
        if(licitation):
            calendar = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[3]/div[5]/div'))
            )
            calendar.click()

    def Registers(self):
        if(licitation):
            registers = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[3]/div[6]'))
            )
            registers.click()


if __name__ == "__main__":
    licitation = Licitation()
    licitation.Licitations()
    time.sleep(10)