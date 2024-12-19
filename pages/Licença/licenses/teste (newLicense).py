import sys
sys.path.append('/root/Aprendizado')
from pages.Licença.License import *

license = License()
license.Licenses()
    
def New_license():
    new_licence = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/button'))
    )
    new_licence.click()
    time.sleep(6)
    firt_camp = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div/div/div[1]'))
    )
    firt_camp.click()
    actions = ActionChains(license.start.driver)
    actions.send_keys(Keys.ENTER).perform() 
    time.sleep(2)

    
    equipament = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/div[2]/div/div/div/div/div[1]'))
    )
    equipament.click()
    time.sleep(2)

    service_type = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#tipo_servico_locacao'))
    )
    service_type.click()
    time.sleep(2)

    distributor = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[4]/div[1]/div/div/div/div/div[1]'))
    )
    distributor.click()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)

    version = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[4]/div[2]/div/div/div/div/div[1]'))
    )
    version.click()
    actions.send_keys(Keys.ENTER).perform()
    time.sleep(2)

    product = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[5]/div[1]/div/div/div/div/div[1]'))
    )
    product.click()
    time.sleep(2)

    product_key = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[5]/div[2]/input'))
    )
    product_key.send_keys("12312421421414")
    time.sleep(2)

    amount = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/form/div[6]/div[1]/input'))
    )
    amount.send_keys('43')
    time.sleep(2)

    unit_value = WebDriverWait(license.start.driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div/form/div[6]/div[2]/div/input'))
    )
    unit_value.send_keys(1233)

if __name__ == "__main__":
    new_license = New_license()
    time.sleep(40)