from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\LabInfo\\Documents\\sla\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://github.com/login")

    def enviarDados(usuario, senha):
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        senha_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]'))
        )
        email_login.clear
        senha_login.clear
        email_login.send_keys(usuario)
        senha_login.send_keys(senha)
        btn_login.click()
        driver.implicitly_wait(5)
        btn_reposi = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/ul/li[5]/div/div/a'))
        ) 
        btn_reposi.click()
        # btn_repository = WebDriverWait(driver, 5).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="item-844d2999-ddfb-4b1e-80b2-bf61df17442a"]/span[2]'))
        # )
        # btn_repository.click()
        # btn_desgraca = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, '//*[@id="user-repositories-list"]/ul/li[1]/div[1]/div[1]/h3/a'))
        # )
        # btn_desgraca.click()
    alert = enviarDados('ApenasUmDio','Felaa1524')
    print("o teste foi um sucesso!")

except:
    print("Teste Falhou! Erro na execução")

driver.quit()