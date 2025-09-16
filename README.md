# 🛠️ Automação Python + n8n para Extração de Dados do GLPI

Este repositório contém scripts em **Python** desenvolvidos para automação de processos de extração de dados do **GLPI**.  
A integração é feita por meio do **n8n**, que orquestra os fluxos e dispara os robôs para realizar consultas automáticas na plataforma.

---

## 📌 Objetivo
Automatizar a coleta de informações do **GLPI** (chamados, usuários, inventário, etc.) sem a necessidade de intervenção manual, garantindo:
- Redução de tempo em atividades repetitivas;  
- Padronização na coleta e tratamento dos dados;  
- Integração simples com o **n8n** para criação de fluxos automatizados.

---

## 🚀 Tecnologias Utilizadas
- [Python 3.10+](https://www.python.org/)  
- [n8n](https://n8n.io/) – plataforma de automação low-code  
- Bibliotecas Python:
  - `selenium` → para automação

---

## ⚙️ Estrutura do Projeto
```bash
.
├── main.py               # Script principal da automação


