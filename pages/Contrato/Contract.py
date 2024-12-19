import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class Contract:
    start = Global_Config()
    # start.Start()
    start.Login()
    contract = WebDriverWait(start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[1]'))
    )
    contract.click()

    def Certificates(self):
        if(contract):
            certificates = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[2]/div'))
            )
            certificates.click()

    def Contract_analysis(self):
        if(contract):
            contract_analysis = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[3]/div'))
            )
            contract_analysis.click()

    def Billing(self):
        if(contract):
            billing = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[4]/div'))
            )
            billing.click()
    
    def Recurrence(self):
        if(contract):
            recurrence = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[5]/div'))
            )
            recurrence.click()

    def Retentions(self):
        if(contract):
            retentions = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[6]/div'))
            )
            retentions.click()

    def Contracts(self):
        if(contract):
            contracts = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[7]/div'))
            )
            contracts.click()

    def Registers(self):
        if(contract):
            registers = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[8]'))
            )
            registers.click()


if __name__ == "__main__":
    contract = Contract()
    contract.Registers()
    time.sleep(10)