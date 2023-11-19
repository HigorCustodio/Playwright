from sys import path
path.insert(0, '.\\')
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    navegador = p.firefox.launch()
    page = navegador.new_page()
    page.goto('http://dgg.gg')
    
    print(page.title)
    navegador.close()