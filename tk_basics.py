import tkinter
from tkinter import ttk

DemoWindow = tkinter.Tk()

global LineInTurn
LineInTurn=0

TabbedWindow = ttk.Notebook(DemoWindow)
FirstTab = ttk.Frame(TabbedWindow, height=200, width=200)
SecondTab = ttk.Frame(TabbedWindow, height=200, width=200)
TabbedWindow.add(FirstTab, text='one')
TabbedWindow.add(SecondTab, text='two')
Frame01 = tkinter.Frame(FirstTab, background="yellow", height=20, width=20)
Frame02 = tkinter.Frame(FirstTab, background="orange", height=20, width=40)
Frame03 = tkinter.Frame(FirstTab, background="white", height=100, width=150, relief="ridge", borderwidth=5)
TextArea = tkinter.Label(Frame01, text="Hello World", background="green", font=('Helvetica', 18))
TextArea2 = tkinter.Label(Frame01, text="Read This", background="#6699ff", font=('Times', 18, 'bold italic'))


CanvasOnj = tkinter.Canvas(SecondTab, height=10, width=20, relief="sunken")
CanvasOnj.pack(expand="yes", fill="both")
CanvasOnj.create_text(20, 30, anchor='w', font="Courier", text="Text is added as an example")

def DisplayResults():
    ScrlBar = ttk.Scrollbar(Frame03)
    ResultTree = ttk.Treeview(Frame03)
    ScrlBar.config(command=ResultTree.yview)
    ResultTree.configure(columns=("one", "two"))
    ResultTree.column('#0', width=100)
    ResultTree.column("one", width=200)
    ResultTree.column("two", width=200)
    ResultTree.heading('#0', text="No")
    ResultTree.heading("one", text="Column 01")
    ResultTree.heading("two", text="Column 02")
    ResultTree.pack(side="left", expand="yes", fill="both")
    ScrlBar.pack(side="right", fill="y")

    SalesGroup=ResultTree.insert("", 0, text="Sales Team")
    DevGroup=ResultTree.insert("", 1, text="Devlop Team")

    ResultTree.insert(SalesGroup, "end", text="Person1", values=("Name1","Age1"))
    ResultTree.insert(SalesGroup, "end", text="Person2", values=("Name2","Age2"))
    ResultTree.insert(SalesGroup, "end", text="Person3", values=("Name3","Age3"))
    ResultTree.insert(DevGroup, "end", text="Person1", values=("Name1","Age1"))
    ResultTree.insert(DevGroup, "end", text="Person2", values=("Name2","Age2"))
    ResultTree.insert(DevGroup, "end", text="Person3", values=("Name3","Age3"))
    
Button01= tkinter.Button(Frame02, text="Button", command=DisplayResults)



TabbedWindow.pack()
TextArea.pack()
TextArea2.pack()
Button01.pack()
Frame01.pack(expand="yes", fill="both")
Frame02.pack(expand="yes", fill="both")
Frame03.pack(expand="yes", fill="both")


DemoWindow.mainloop()
