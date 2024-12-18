from config.Imports import * #Não esquecer de colocar só " from Imports import " *

class Global_Config:
    def __init__(self):
        self.env_path = '/root/Aprendizado/config/variable.env'
        self.load_dotenv = load_dotenv(dotenv_path=self.env_path)

        self.options = Options()
        self.options.add_argument("--incognito")
        self.options.add_argument("--disable-gpu")
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")

    def Start(self):
        self.service = Service("/usr/bin/chromedriver")
        self.driver = webdriver.Chrome(service=self.service, options=self.options)

        self.driver.maximize_window()

        # Acessar a página desejada
        self.driver.get("http://localhost:3000/")

    def Login(self):
        self.driver.find_element(By.ID, "formLoginUsuario").send_keys(os.getenv("LOGIN_USER"))
        self.driver.find_element(By.ID, "formLoginPassword").send_keys(os.getenv("LOGIN_PASSWORD"))
        self.driver.find_element(By.TAG_NAME, "button").click()


if __name__ == "__main__":
    start = Global_Config()
    start.Login()