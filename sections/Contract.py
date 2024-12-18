import sys
sys.path.append('/root/Aprendizado')
from config.global_config import *


class Contract:
    start = Global_Config()
    start.Start()
    start.Login()

    def Contracts(self):
        contract = WebDriverWait(self.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[1]'))
        )
        if(contract):
            license.click()
            contracts = WebDriverWait(self.start.driver,20).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[4]/div[7]/div'))
            )
            contracts.click()


if __name__ == "__main__":
    contract = Contract()
    contract.Contracts()