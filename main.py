# Introdução - Programa para ver a cotação de 4 moedas em tempo real usando uma API.

# Peimeiros passo...
#Importar o APP, importar o Builder (GUI = ...)
from kivy.app import App
from kivy.lang import Builder
import requests
GUI = Builder.load_file('screen.kv')

#Todo app Kivy é criado dentro de uma classe...
#Criar o Aplicativo
#Criar a função Build do aplicativo
class MeuAplicativo(App): 
    def build(self):
        return GUI
    
    def on_start(self): #Editando os ids de screen.kv / no caso o que serpa editado é o texto então ([...].text)
        self.root.ids["moeda1"].text = f"Dolar: R${self.pegar_cotacao('USD')}"
        self.root.ids["moeda2"].text = f"Euro: R${self.pegar_cotacao('EUR')}"
        self.root.ids["moeda3"].text = f"Bitcoin: R${self.pegar_cotacao('BTC')}"
        self.root.ids["moeda4"].text = f"Etheriun: R${self.pegar_cotacao('ETH')}"
    
    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
        requisicao = requests.get(link)
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}BRL"]["bid"]
        return cotacao

#Abrindo a tela
MeuAplicativo().run()