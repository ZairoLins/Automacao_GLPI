#Importações das bibliotecas necessárias

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os, time
import os, time
from selenium.common.exceptions import StaleElementReferenceException, WebDriverException  

URL_LOGIN = "https://chamados.idxdatacenters.com.br/front/login.php"
URL_TICKETS = "https://chamados.idxdatacenters.com.br/front/ticket.php"

USUARIO = os.getenv("GLPI_USER") or "zairo.cunha"
SENHA   = os.getenv("GLPI_PASS") or "Zlrc731686-"

def main():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # roda sem abrir janela
    options.add_argument("--disable-gpu") # evita bugs em alguns sistemas
    options.add_argument("--no-sandbox") # recomendado em alguns ambientes
    options.add_argument("--window-size=1920,1080") # tamanho "virtual" da tela


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(driver, 15)

    try:
        # Login
        driver.get(URL_LOGIN)
        user_input = wait.until(EC.visibility_of_element_located((By.ID, "login_name")))
        pass_input = wait.until(EC.visibility_of_element_located((By.ID, "login_password")))

        user_input.clear(); user_input.send_keys(USUARIO)
        pass_input.clear(); pass_input.send_keys(SENHA)
        pass_input.send_keys(Keys.ENTER)

        wait.until(lambda d: "login.php" not in d.current_url.lower())

        # Tickets
        driver.get(URL_TICKETS)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        wait.until(lambda d: d.execute_script("return document.readyState") == "complete")  

        # Clica no menu de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):  
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "Pré-Tickets"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[1]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_pre = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_pre.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_pre:
                f.write(_id + "\n")

        # Clica no menu de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):  
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "DataCenter"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[2]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_dc = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_dc.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_dc:
                f.write(_id + "\n")

        # Entra novamente na lista de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):  
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "Suporte - Infra PMW"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[4]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_infra = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_infra.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_infra:
                f.write(_id + "\n")

        #Entra novamente na lista de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):  
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "Suporte N1 - Palmas"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[5]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_n1 = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_n1.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_n1:
                f.write(_id + "\n")

        # Entra novamente na lista de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "Suporte NOC"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[6]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_noc = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_noc.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_noc:
                f.write(_id + "\n")

        # Entra novamente na lista de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):  
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "Suporte SOC"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[7]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_soc = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_soc.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_soc:
                f.write(_id + "\n")

        # Entra novamente na lista de Tickets
        xpath_pre_tickets = '/html/body/div[2]/header/div/ul/li[3]/a'

        for attempt in range(4):
            try:
                # Garante que o header existe antes de buscar o link
                wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/header")))
                link_pre_tickets = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_pre_tickets))
                )
                driver.execute_script("arguments[0].scrollIntoView({block:'center'});", link_pre_tickets)
                driver.execute_script("arguments[0].click();", link_pre_tickets)  
                break
            except (StaleElementReferenceException, WebDriverException) as e:
                if "target frame detached" in str(e):
                    time.sleep(0.6)
                    continue
                raise

        # Espera o container das listas aparecer
        wait.until(EC.presence_of_element_located((By.ID, "itemtype-filtered")))  

        # Entra na lista "Suporte Telefonia"
        xpath_tickets_suporte_dc = '//*[@id="itemtype-filtered"]/div/div[8]/a'
        el_dc = wait.until(EC.element_to_be_clickable((By.XPATH, xpath_tickets_suporte_dc)))
        driver.execute_script("arguments[0].scrollIntoView({block:'center'});", el_dc)  
        driver.execute_script("arguments[0].click();", el_dc)  

        # Aguarda a tabela e coleta TODOS os IDs
        wait.until(EC.presence_of_element_located(
            (By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr")
        ))
        id_cells = driver.find_elements(
            By.XPATH, "//table[starts-with(@id,'search_')]/tbody/tr/td[2]"
        )

        ids_tel = []
        for c in id_cells:
            txt = c.text.strip()
            if not txt:
                try:
                    txt = c.find_element(By.XPATH, ".//a | .//span").text.strip()
                except Exception:
                    pass
            if txt:
                ids_tel.append(txt)

        with open("ids_tickets_mesa_atual.txt", "w", encoding="utf-8") as f:
            for _id in ids_tel:
                f.write(_id + "\n")

        print(f"-> Pré - Tickets ({len(ids_pre)}): {ids_pre}") # Mostra os pré-tickets
        print(f"-> Tickets - DC ({len(ids_dc)}): {ids_dc}") # Mostra os tickets de DC
        print(f"-> Tickets - Infra ({len(ids_infra)}): {ids_infra}") # Mostra os tickets de Infra
        print(f"-> Tickets - N1 ({len(ids_n1)}): {ids_n1}") # Mostra os tickets de Infra
        print(f"-> Tickets - NOC ({len(ids_noc)}): {ids_noc}") # Mostra os tickets de Infra
        print(f"-> Tickets - SOC ({len(ids_soc)}): {ids_soc}") # Mostra os tickets de Infra
        print(f"-> Tickets - Telefonia ({len(ids_tel)}): {ids_tel}") # Mostra os tickets de Infra

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
