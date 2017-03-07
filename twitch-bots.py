#-*- coding: utf-8 -*-
from selenium import webdriver


class Criador():
    def __init__(self, address):
        self.driver = webdriver.Chrome('/home/gabs/Downloads/chromedriver')
        self.driver.get(address)

nJanelas = int(input('Digite quantas vezes deseja abrir o site: '))
address = raw_input('Digite endereco do site: ')
if address.startswith('http://www.'):
    lista = [Criador(address) for x in range(nJanelas)]
elif address.startswith('www.'):
    lista = [Criador('http://'+address) for x in range(nJanelas)]
else:
    lista = [Criador('http://www.'+address) for x in range(nJanelas)]
