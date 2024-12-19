import sys
sys.path.append('/root/Aprendizado')
from pages.Licença.License import *


class NewLicense:
    license = License()
    license.Licenses()
    
    # def 

    

if __name__ == "__main__":
    time.sleep(10)
    
    new_licence = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/button'))
    )
    new_licence.click()
    time.sleep(6)
    firt_camp = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="react-select-undefined"]/div'))
    )
    firt_camp.click()
    Keys.ARROW_DOWN
    Keys.ENTER

    equipament = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div/div/div[1]'))
    )
    equipament.click()
    
    service_type = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#tipo_servico_locacao'))
    )
    service_type.click()
    
    distributor = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[4]/div[1]/div/div/div/div/div[1]'))
    )
    distributor.click()