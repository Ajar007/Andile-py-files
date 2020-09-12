from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import socket
from threading import Thread

class MyApp(GridLayout):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
        self.cols=1
        from threading import Thread

        self.add_widget(Label(text="Client", color=(1,0,0,1), bold=True, size_hint=(1,0.05)))
        self.chats=TextInput()
        self.add_widget(self.chats)

        #second gridlayout
        self.txtandsnd=GridLayout(size_hint=(1,0.05))
        self.txtandsnd.cols=2
        self.add_widget(self.txtandsnd)

        self.msg=TextInput(size_hint=(0.85,1))
        self.txtandsnd.add_widget(self.msg)

        def snd(msg):
            """Handles send msg"""
            message=self.msg.text
            self.msg.text=""
            if message and tags[-1]==0:
                self.chats.text += "\n" + str("Client: ") + str(message)
                s.send((str("Client: ")+str(message)).encode("utf-8"))
            elif message and tags[-1]>int(10):
                self.chats.text += "\n" + str("Client: ") + str(message)
                s.send((str(tags[-1]) + str("Client: ")+str(message)+ str("~")).encode("utf-8"))
            else:
                self.chats.text += "\n" + str("You did not send a message")


        self.B1=Button(text="Send", color=(1,0,0,1,), bold=True, italic=True, size_hint=(0.15,1))
        self.B1.bind(on_press=snd)
        self.txtandsnd.add_widget(self.B1)

        tags=[0]


        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host='197.214.117.210'
        port=9999
        s.connect((host,port))

        def rec():
            """Handles incoming msg""" 
            while True:
                msgi=s.recv(1024)
                msgf=msgi.decode("utf-8")
                tag=int(msgf[0:2])
                if tag==int(10):
                    try:
                        self.chats.text += "\n" + str(msgf[2:])
                    except OSError:
                        self.chats.text += "\n" + str("Operation System Error, close and open App again")
                        break
                        
                elif tag>int(10):
                    try:
                        self.chats.text += "\n" + str(msgf[2:])
                        tags.append(tag)
                    except OSError:
                        self.chats.text += "\n" + str("Operation System Error, close and open App again")
                        break

        while True:
            recThread=Thread(target=rec)
            recThread.start()
            break
       
class ALM(App):
    icon="waterdrop.jpg"
    def build(self):
        return MyApp()
            

if __name__=="__main__":
    ALM().run()
