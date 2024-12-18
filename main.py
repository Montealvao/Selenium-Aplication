from config.Imports import *

env_path = '/root/Aprendizado/config/variable.env'
load_dotenv(dotenv_path=env_path)


options = Options()
options.add_argument("--incognito")
# options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

service = Service("/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

driver.maximize_window()

# Acessar a página desejada
driver.get("http://localhost:3000/")

print(driver.current_url)

login = driver.find_element(By.ID, "formLoginUsuario").send_keys(os.getenv("LOGIN_USER"))
password = driver.find_element(By.ID, "formLoginPassword").send_keys(os.getenv("LOGIN_PASSWORD"))
button = driver.find_element(By.TAG_NAME, "button").click()

license = WebDriverWait(driver,20).until(
    EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[1]'))
)
if(license):
    license.click()
    licenses = WebDriverWait(driver,20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div[2]/div[1]/div/div[1]/div[3]/div[6]/div[2]/div'))
    )
    licenses.click()
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


print(driver.current_url)

time.sleep(40)

# Fechar o navegador
driver.quit()
