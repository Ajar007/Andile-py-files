from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import socket
from threading import Thread
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelHeader

class MyApp(TabbedPanel):
    def __init__(self, **kwargs):
        super(MyApp, self).__init__(**kwargs)
    
        from threading import Thread

        sample=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        clients=[10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
        tabs=[0,0,0,0,0,0,0,0,0,0]
        chatslist=[0,0,0,0,0,0,0,0,0,0]
        msgs=[]

        self.do_default_tab = False
        self.tab_width = 40

        def snd(msg_i):
            """Handles send msg"""
            for i in msgs:
                a=i.text
                i.text=""
                if a:
                    tag=int(msgs.index(i))+int(10)
                    print (tag)
                    try:
                        chatslist[tag].text += "\n" +str("Admin: ")+str(a)  #make this a separate function
                        s.send((str(tag)+str("Admin: ")+str(a)).encode("utf-8"))
                    except ValueError:
                        pass
                if not a:
                    pass
            

        for i in sample:

            tabtext= str("C")+str(i)

            self.tab_i=TabbedPanelHeader(text=tabtext)
            tabs.append(self.tab_i)
            self.add_widget(self.tab_i)

            self.tabgrid_i=GridLayout()
            self.tabgrid_i.cols=1
            self.tab_i.content=self.tabgrid_i

            self.chats_i=TextInput()
            chatslist.append(self.chats_i)
            self.tabgrid_i.add_widget(self.chats_i)

            #second gridlayout
            self.txtandsndgrid_i=GridLayout(size_hint=(1,0.06))
            self.txtandsndgrid_i.cols=2
            self.tabgrid_i.add_widget(self.txtandsndgrid_i)

            self.msg_i=TextInput(text="", size_hint=(0.85,1))
            msgs.append(self.msg_i)
            self.txtandsndgrid_i.add_widget(self.msg_i)

            self.B_i=Button(text="Send", color=(1,0,0,1,), bold=True, italic=True, size_hint=(0.15,1))
            self.B_i.bind(on_press=snd)
            self.txtandsndgrid_i.add_widget(self.B_i)

        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host=socket.gethostname()
        port=9999
        s.connect((host,port))

        def rec():
            """Handles incoming msg"""
            while True:
                msgi=s.recv(1024)
                msgf=msgi.decode("utf-8")
                tag=int(msgf[0:2])
                for i in clients:
                    if tag==i:
                        try:
                            self.switch_to(tabs[tag])
                            chatslist[tag].text += "\n" + str(msgf[2:])
                            continue
                        except ValueError:
                            continue
                        
                    elif tag!=i:
                        pass
                    
                    elif tag>50: #to be changed with more clients
                        pass

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

