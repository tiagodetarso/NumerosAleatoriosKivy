import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox

class Numeros_Aleatorios(App): 
  
    def build (self):
        self.window = GridLayout(cols = 2)
        self.window.siz_hint = (1, 1)
        self.window.po_hint = {"center_x": 0.5, "center_y": 0.5}
        self.window.spacing = [10,10]
        
        #Adicionar Imagem
        self.window.add_widget(Image(source="Embaralhar.png",
                               #size_hint_x = None,
                               width = 250))
        
        #Adicionar Textos e Entradas
        self.titulo = Label(
            text = "SortNum\nNúmeros Aleatórios",
            font_size = 35,
            color = "green",
            bold = True,
            halign = 'center',
            valign = 'center',
            width = 275
            )
        self.window.add_widget(self.titulo)
            
        self.txliminferior = Label(
            text = "Limite Inferior do Intervalo: ",
            halign = 'right',
            valign = 'center',
            #size_hint_x = None,
            width = 250
            )
        self.window.add_widget(self.txliminferior)
        
        self.liminferior = TextInput(
            multiline=False,
            font_size = 30,
            padding = (50,30,10,30),
            #size_hint = (1, 1),
            width = 275
            )
        self.window.add_widget(self.liminferior)
       
        self.txlimsuperior = Label(
            text = "Limite Superior do Intervalo:",
            halign = 'right',
            valign = 'center',
            #size_hint_x = None,
            width = 250
            )
        self.window.add_widget(self.txlimsuperior)
        
        self.limsuperior = TextInput(
            multiline=False,
            font_size = 30,
            padding = (50,30,10,30),
            size_hint = (1, 1),
            width = 275
            )
        self.window.add_widget(self.limsuperior)
        
        self.txquantidade = Label(
            text = "Quantidade de números a sortear:",
            halign = 'right',
            valign = 'center',
            #size_hint_x = None,
            width = 250
            ) 
        self.window.add_widget(self.txquantidade)
        
        self.quantidade = TextInput(
            multiline=False,
            font_size = 30,
            padding = (50,30,10,30),
            size_hint = (1, 1),
            width = 275
            )
        self.window.add_widget(self.quantidade)
              
        self.repetir = Label(
            text = "Permitir repetição de números?",
            halign = 'center',
            valign = 'center',
            size_hint = (1,1),
            width = 250
            )
        self.window.add_widget(self.repetir)
        
        #Adicionar CheckBox
        self.Checagem = CheckBox(
            color = [0,255,255,1],
            size_hint = (1,1)
            )
        self.Checagem.bind(active = self.marcado)
        self.window.add_widget(self.Checagem)
        
        #Adicionar Botão
        self.botao = Button(
            text = "Sortear",
            width = 250,
            #size_hint_x = None,
            bold = True,
            background_color = "green",
            background_normal = "",
            )
        self.botao.bind(on_press=self.Aleatorios)
        self.window.add_widget(self.botao)
        
        #Adicionar saídas
        self.resultado = Label(
            text="",
            font_size = 23,
            color = "green",
            halign = 'left',
            width = 275
            )
        self.window.add_widget(self.resultado)
        
        return self.window

    def marcado(self, instance, value):
        if value == True:
            self.ticagem = True
        else:
            self.ticagem = False

    def Aleatorios(self, instance): 
        limite_inferior = int(self.liminferior.text)
        limite_superior = int(self.limsuperior.text)
        quantidade = int(self.quantidade.text)
        
        i = (limite_superior - limite_inferior) + 1
        lista = [limite_inferior]
        a = 1
        while a < i:
            lista.append(limite_inferior + a)
            a+=1
        
        try:
            if self.ticagem == True:
                Aleatorio = sorted(list(random.choices(lista, k=quantidade)))
                i = 1
                apresentacao=str(Aleatorio[0])
                while i < len(Aleatorio):
                    apresentacao = apresentacao+", "+str(Aleatorio[i])
                    i+=1
                self.resultado.text = apresentacao
        
            elif self.ticagem == False:
                x=0
                lista_resultado = []
                while x < quantidade:
                    Aleatorio = random.choices(lista, k=1)
                    lista_resultado.append(Aleatorio)
                    lista_resultado = sorted(lista_resultado)
                    z = set(lista)
                    y = set(Aleatorio)
                    lista = list(z.difference(y))
                    x+=1
                i=1
                apresentacao = str(lista_resultado [0])
                while i < len(lista_resultado):
                    apresentacao = apresentacao+" "+str(lista_resultado[i])
                    i+=1
                self.resultado.text = apresentacao
        except:
                x=0
                lista_resultado = []
                while x < quantidade:
                    Aleatorio = random.choices(lista, k=1)
                    lista_resultado.append(Aleatorio)
                    lista_resultado = sorted(lista_resultado)
                    z = set(lista)
                    y = set(Aleatorio)
                    lista = list(z.difference(y))
                    x+=1
                apresentacao = str(lista_resultado [0][0])
                i=1
                while i < len(lista_resultado):
                    apresentacao = apresentacao+", "+str(lista_resultado[i][0])
                    i+=1
                self.resultado.text = apresentacao
            
if __name__ == "__main__":
    Numeros_Aleatorios().run()
