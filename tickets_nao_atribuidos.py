#Importações das bibliotecas necessárias

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv

load_dotenv()

URL_LOGIN="https://chamados.idxdatacenters.com.br/front/login.php"
USUARIO = os.getenv("GLPI_USER")
SENHA = os.getenv("GLPI_PASS")
URL_DC="https://chamados.idxdatacenters.com.br/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=65&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=11&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B3%5D%5Blink%5D=AND&criteria%5B3%5D%5Bfield%5D=5&criteria%5B3%5D%5Bsearchtype%5D=equals&criteria%5B3%5D%5Bvalue%5D=0&savedsearches_id=63&itemtype=Ticket&start=0&_glpi_csrf_token=6bd147875ace38c4a5ea5a8e6f6b57ee71caf1bd3460c38331733335df9686a9&sort%5B%5D=19&order%5B%5D=DESC"
URL_INFRA="https://chamados.idxdatacenters.com.br/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=7&criteria%5B0%5D%5Bsearchtype%5D=contains&criteria%5B0%5D%5Bvalue%5D=infra&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B5%5D%5Blink%5D=AND&criteria%5B5%5D%5Bfield%5D=5&criteria%5B5%5D%5Bsearchtype%5D=equals&criteria%5B5%5D%5Bvalue%5D=0&savedsearches_id=104&itemtype=Ticket&start=0&_glpi_csrf_token=47cfad430b04c89d7088b423b3806794d505308795e4de628446e1495e0be476&sort%5B%5D=19&order%5B%5D=DESC"
URL_N1="https://chamados.idxdatacenters.com.br/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=12&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=notold&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=65&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=16&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=7&criteria%5B2%5D%5Bsearchtype%5D=notcontains&criteria%5B2%5D%5Bvalue%5D=telefo&criteria%5B3%5D%5Blink%5D=AND&criteria%5B3%5D%5Bfield%5D=7&criteria%5B3%5D%5Bsearchtype%5D=notcontains&criteria%5B3%5D%5Bvalue%5D=infra&criteria%5B4%5D%5Blink%5D=AND&criteria%5B4%5D%5Bfield%5D=5&criteria%5B4%5D%5Bsearchtype%5D=equals&criteria%5B4%5D%5Bvalue%5D=0&savedsearches_id=38&itemtype=Ticket&start=0&_glpi_csrf_token=1434690fd161f16302376e91f0787d3ac4aa208b6119f78bd5133c91d395ab70&sort%5B%5D=19&order%5B%5D=DESC"
URL_NOC="https://chamados.idxdatacenters.com.br/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=65&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=12&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=5&criteria%5B2%5D%5Bsearchtype%5D=equals&criteria%5B2%5D%5Bvalue%5D=0&savedsearches_id=63&itemtype=Ticket&start=0&_glpi_csrf_token=029c8df4fe2bec758eb346701d5dfea4643bfe887c66fff99b6f7d4e533f9616&sort%5B%5D=19&order%5B%5D=DESC"
URL_SOC="https://chamados.idxdatacenters.com.br/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=65&criteria%5B0%5D%5Bsearchtype%5D=equals&criteria%5B0%5D%5Bvalue%5D=13&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B2%5D%5Blink%5D=AND&criteria%5B2%5D%5Bfield%5D=5&criteria%5B2%5D%5Bsearchtype%5D=equals&criteria%5B2%5D%5Bvalue%5D=0&savedsearches_id=63&itemtype=Ticket&start=0&_glpi_csrf_token=bbb6754189a1b8aa1c2d7c58ea8d3c61362a55a645cb97fe04a6da73c5b35403&sort%5B%5D=19&order%5B%5D=DESC"
URL_TEL="https://chamados.idxdatacenters.com.br/front/ticket.php?is_deleted=0&as_map=0&browse=0&criteria%5B0%5D%5Blink%5D=AND&criteria%5B0%5D%5Bfield%5D=7&criteria%5B0%5D%5Bsearchtype%5D=contains&criteria%5B0%5D%5Bvalue%5D=SFTC&criteria%5B1%5D%5Blink%5D=AND&criteria%5B1%5D%5Bfield%5D=12&criteria%5B1%5D%5Bsearchtype%5D=equals&criteria%5B1%5D%5Bvalue%5D=notold&criteria%5B2%5D%5Blink%5D=OR&criteria%5B2%5D%5Bfield%5D=7&criteria%5B2%5D%5Bsearchtype%5D=contains&criteria%5B2%5D%5Bvalue%5D=telefonia&criteria%5B3%5D%5Blink%5D=AND&criteria%5B3%5D%5Bfield%5D=12&criteria%5B3%5D%5Bsearchtype%5D=equals&criteria%5B3%5D%5Bvalue%5D=notold&criteria%5B4%5D%5Blink%5D=AND&criteria%5B4%5D%5Bfield%5D=5&criteria%5B4%5D%5Bsearchtype%5D=equals&criteria%5B4%5D%5Bvalue%5D=0&savedsearches_id=39&itemtype=Ticket&start=0&_glpi_csrf_token=6b4aa1c681597605910ce09626f7656aed13980c02f9482ee4fe0c68932cf194&sort%5B%5D=19&order%5B%5D=DESC"

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

        # Captura os tickets sem técncico abruído - Mesa DC
        driver.get(URL_DC)
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

        # Captura os tickets sem técncico abruído - Mesa INFRA
        driver.get(URL_INFRA)
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

        # Captura os tickets sem técncico abruído - Mesa N1 - PMW
        driver.get(URL_N1)
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

        # Captura os tickets sem técncico abruído - Mesa NOC
        driver.get(URL_NOC)
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

        # Captura os tickets sem técncico abruído - Mesa SOC
        driver.get(URL_SOC)
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

        # Captura os tickets sem técncico abruído - Mesa NOC
        driver.get(URL_TEL)
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

        print(f"-> Tickets - DC ({len(ids_dc)}): {ids_dc}") # Mostra os tickets de DC
        print(f"-> Tickets - Infra ({len(ids_infra)}): {ids_infra}") # Mostra os tickets de Infra
        print(f"-> Tickets - N1 ({len(ids_n1)}): {ids_n1}") # Mostra os tickets de Infra
        print(f"-> Tickets - NOC ({len(ids_noc)}): {ids_noc}") # Mostra os tickets de Infra
        print(f"-> Tickets - SOC ({len(ids_soc)}): {ids_soc}") # Mostra os tickets de Infra
        print(f"-> Tickets - Telefonia ({len(ids_tel)}): {ids_tel}") # Mostra os tickets de Infra

        # Junta todos os IDs por categoria
        todos_ids = {
            "DataCenter": ids_dc,
            "Infra": ids_infra,
            "N1": ids_n1,
            "NOC": ids_noc,
            "SOC": ids_soc,
            "Telefonia": ids_tel
        }

        # Cria apenas UM arquivo no final
        with open("ids_tickets_nao_atribuidos.txt", "w", encoding="utf-8") as f:
            for categoria, ids in todos_ids.items():
                f.write(f"\n### {categoria} ({len(ids)}) ###\n")
                for _id in ids:
                    f.write(_id + "\n")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
