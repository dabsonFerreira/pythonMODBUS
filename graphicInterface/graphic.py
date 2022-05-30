import kivy#não sei resolver esse problema. Execute pelo terminal!!!!
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyWidget(BoxLayout):
    def incrementar(self):
        self.ids['lb'].text = str(int(self.ids['lb'].text)+1)
class BasicApp(App):
    def build(self):#Construtor
        bt = Button(text='bt1')
        #lb = label(text='lb1')
        return MyWidget()
      
if __name__ == '__main__':
    BasicApp().run()

