#v 1.0.0

'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Howard C Davis
Final Tk
'''


from tkinter import *
from tkinter import ttk

#Code boards
UD1 = [['111','121','131'],['112','122','132'],['113','123','133']]
UD2 = [['211','221','231'],['212','222','232'],['213','223','233']]
UD3 = [['311','321','331'],['312','322','332'],['313','323','333']]

#Boards that are going to be seen
UDS1 = [['___','___','___'],['___','___','___'],['___','___','___']]
UDS2 = [['___','___','___'],['___','___','___'],['___','___','___']]
UDS3 = [['___','___','___'],['___','___','___'],['___','___','___']]


root = Tk()

global textFUD1
global textFUD2
global textFUD3
global PLAYERN
PLAYERN = 0
global PLAYER
PLAYER = ' X '
global UDL


def makeboard1():
    global textFUD1
    textFUD1 = []
    for i in UDS1:
        a = str(i).replace(',','').replace('[','').replace(']','').replace("'",'')
        textFUD1.append(a)

def makeboard2():
    global textFUD2
    textFUD2 = []
    for i in UDS2:
        a = str(i).replace(',', '').replace('[', '').replace(']', '').replace("'",'')
        textFUD2.append(a)

def makeboard3():
    global textFUD3
    textFUD3 = []
    for i in UDS3:
        a = str(i).replace(',', '').replace('[', '').replace(']', '').replace("'",'')
        textFUD3.append(a)

makeboard1()
makeboard2()
makeboard3()

def check():
    if TTTCBL.get() == '' or TTTCBC.get() == '' or TTTCBR.get() == '':
        labelWL.config(text='Missing input')
        pass
    else:
        if TTTCBL.get() == 'Top':
            UDL = UDS1
        elif TTTCBL.get() == 'Middle':
            UDL = UDS2
        elif TTTCBL.get() == 'Bottom':
            UDL = UDS3

        if UDL[int(TTTCBR.get()) - 1][int(TTTCBC.get()) - 1] != '___':
            labelWL.config(text='That space is occupied!')
            pass
        else:
            change()

def change():
    global PLAYER
    global PLAYERN
    global UD1
    global UD2
    global UD3
    global UDL

    a = 1

    if PLAYERN == 0:
        PLAYER = ' X '
    elif PLAYERN == 1:
        PLAYER = ' O '
    else:
        PLAYERN = 0
        PLAYER = ' X '

    labelWL.config(text = 'Player %s'%PLAYER)


    if TTTCBL.get() == 'Top':
        UDSL = UDS1
        a = 1
    elif TTTCBL.get() == 'Middle':
        UDSL = UDS2
        a = 2
    elif TTTCBL.get() == 'Bottom':
        UDSL = UDS3
        a = 3

    UDSL[int(TTTCBR.get()) - 1][int(TTTCBC.get()) - 1] = PLAYER

    makeboard1()
    makeboard2()
    makeboard3()

    b = TTTCBC.get()
    c = TTTCBR.get()
    WLplace = str('%s%s%s'%(a,b,c))


    newWLboard1 = []
    newWLboard2 = []

    if TTTCBL.get() == 'Top':
        UDL = UD1
    elif TTTCBL.get() == 'Middle':
        UDL = UD2
    elif TTTCBL.get() == 'Bottom':
        UDL = UD3

    for i in UDL:

        for i2 in i:
            if i2 == WLplace:
                newWLboard1.append(PLAYER)
            else:
                newWLboard1.append(i2)
        newWLboard2.append(newWLboard1)
        newWLboard1 = []

    if TTTCBL.get() == 'Top':
        UD1 = newWLboard2
    elif TTTCBL.get() == 'Middle':
        UD2 = newWLboard2
    elif TTTCBL.get() == 'Bottom':
        UD3 = newWLboard2


    PLAYERN += 1
    labelsPrint()
    WLsolution()


def WLsolution():
    global PLAYER
    global UDL

    if TTTCBL.get() == 'Top':
        UDL = UD1
    elif TTTCBL.get() == 'Middle':
        UDL = UD2
    elif TTTCBL.get() == 'Bottom':
        UDL = UD3

    clear()

    for i in range(3):
        if UDL[i-1][0] == PLAYER and UDL[i-1][1] == PLAYER and UDL[i-1][2] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)

        elif UDL[0][i-1] == PLAYER and UDL[1][i-1] == PLAYER and UDL[2][i-1] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)


    if UD1[0][0] == PLAYER and UD1[1][1] == PLAYER and UD1[2][2] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)
    if UD1[0][2] == PLAYER and UD1[1][1] == PLAYER and UD1[2][0] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)


    if UD2[0][0] == PLAYER and UD2[1][1] == PLAYER and UD2[2][2] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)
    if UD2[0][2] == PLAYER and UD2[1][1] == PLAYER and UD2[2][0] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)

    if UD3[0][0] == PLAYER and UD3[1][1] == PLAYER and UD3[2][2] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)
    if UD3[0][2] == PLAYER and UD3[1][1] == PLAYER and UD3[2][0] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)

    for i in range(3):
        if UD1[i-1][0] == PLAYER and UD2[i-1][0] == PLAYER and UD3[i-1][0] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)
        if UD1[0][i-1] == PLAYER and UD2[0][i-1] == PLAYER and UD3[0][i-1] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)
        if UD1[i-1][i-1] == PLAYER and UD2[i-1][i-1] == PLAYER and UD3[i-1][i-1] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)

    if UD1[0][0] == PLAYER and UD2[1][1] == PLAYER and UD3[2][2] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)

    if UD1[0][2] == PLAYER and UD2[1][1] == PLAYER and UD3[2][0] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)

    if UD1[2][2] == PLAYER and UD2[1][1] == PLAYER and UD3[0][0] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)

    if UD1[2][0] == PLAYER and UD2[1][1] == PLAYER and UD3[0][2] == PLAYER:
        lock()
        labelWL.config(text='%s wins!' % PLAYER)

    for i in range(3):
        if UD1[i-1][0] == PLAYER and UD2[i-1][1] == PLAYER and UD3[i-1][2] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)

        elif UD1[i-1][2] == PLAYER and UD2[i-1][1] == PLAYER and UD3[i-1][0] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)

        elif UD1[0][i-1] == PLAYER and UD2[1][i-1] == PLAYER and UD3[2][i-1] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)
        elif UD1[2][i-1] == PLAYER and UD2[1][i-1] == PLAYER and UD3[0][i-1] == PLAYER:
            lock()
            labelWL.config(text='%s wins!' % PLAYER)



def lock():
    ButtonS.config(state = DISABLED)
    ButtonC.config(text = 'New Game?', command = clearboard)


def clearboard():
    global UD1
    global UD2
    global UD3
    global UDS1
    global UDS2
    global UDS3
    global PLAYERN
    global PLAYER
    global UDL

    PLAYERN = 0
    PLAYER = ' X '

    clear()

    for i in range(3):
        UDS1[i - 1][0] = '___'
        UDS1[i - 1][1] = '___'
        UDS1[i - 1][2] = '___'

        UDS2[i - 1][0] = '___'
        UDS2[i - 1][1] = '___'
        UDS2[i - 1][2] = '___'

        UDS3[i - 1][0] = '___'
        UDS3[i - 1][1] = '___'
        UDS3[i - 1][2] = '___'

    for i in range(3):
        if i == 1:
            UDL = UD1
        elif i == 2:
            UDL = UD2
        elif i == 3:
            UDL = UD3
        for i2 in range(3):
            for i3 in range(3):
                place = str('%s%s%s'%(i,i2+1,i3+1))
                UDL[i3][i2] = place

    UD1[0][0] = '111'
    UD1[0][1] = '121'
    UD3[0][0] = '311'
    UD3[0][1] = '321'
    UD3[0][2] = '331'
    UD3[1][0] = '312'
    UD3[1][1] = '322'
    UD3[1][2] = '332'
    UD3[2][0] = '313'
    UD3[2][1] = '323'
    UD3[2][2] = '333'

    makeboard1()
    makeboard2()
    makeboard3()

    labelsPrint()
    ButtonC.config(text = 'Clear', command = clear)


def clear():
    a=' X'
    if PLAYERN == 0:
        a = ' X'
    elif PLAYERN == 1:
        a = ' O'
    labelWL.config(text="It Is Now Player%s's Turn" % a)
    LayerChoice.set('')
    ColumnChoice.set('')
    RowChoice.set('')
    ButtonS.config(state=NORMAL)

def about():
    top = Toplevel()
    top.title("About")
    top.minsize(width=200, height=100)
    top.resizable(width=FALSE, height=FALSE)
    msg = Message(top, text='About')
    msg2 = Message(top, text='V 1.0.1\nKeenan Hui\n11/11/18')
    msg3 = Message(top, text = '...')
    msg.pack()
    msg2.pack()
    msg3.pack()
    button = Button(top, text="Close", command=top.destroy)
    button.pack()


def howtoplay():
    top = Toplevel()
    top.title("About")
    top.minsize(width=300, height=200)
    top.resizable(width=FALSE, height=FALSE)
    msg = Message(top, text='How to play - \n\n1 - You select what layer, column, and row you want to place your icon.\n\n2 - You get three in a row to get Tic Tac Toe (you win). You can never draw.\n\nThe game is two players, so X starts first, than O goes next.')
    msg2 = Message(top, text='...')
    msg.pack()
    msg2.pack()
    button = Button(top, text="Close", command=top.destroy)
    button.pack()


# variables
LayerChoice = StringVar()
ColumnChoice = StringVar()
RowChoice = StringVar()


# Entry Box
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label = 'Exit', command = root.quit)
menubar.add_cascade(label = 'File', menu = filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label='About', command=about)
helpmenu.add_command(label='How To Play', command=howtoplay)
menubar.add_cascade(label='Help', menu=helpmenu)
root.config(menu=menubar)

# Labels
labelT = Label(root, text='3D Tic Tac Toe')  # Title
labelT.grid(row=0, column=2)

def labelsPrint():  #Made it a function so I oculd have the tic tac toe boards update

    TTT_L1 = Label(root, text='Top' + '\n\n' + textFUD1[0] + '\n' + textFUD1[1] + '\n' + textFUD1[2], borderwidth=2,relief="groove")  # L1 = layer 1  TTT = Tic Tac Toe
    TTT_L1.config(height=3, width=10)  # textFUD1[0]+'\n'+textFUD1[1]+'\n'+textFUD1[2] -- prints one layer
    TTT_L1.grid(row=1, column=1, sticky=NSEW)

    TTT_L2 = Label(root, text='Middle' + '\n\n' + textFUD2[0] + '\n' + textFUD2[1] + '\n' + textFUD2[2], borderwidth=2,relief="groove")  # L2 = layer 2
    TTT_L2.config(height=3, width=10)
    TTT_L2.grid(row=1, column=2, sticky=NSEW)

    TTT_L3 = Label(root, text='Bottom' + '\n\n' + textFUD3[0] + '\n' + textFUD3[1] + '\n' + textFUD3[2], borderwidth=2,relief="groove")  # L3 = layer 3
    TTT_L3.config(height=3, width=10)
    TTT_L3.grid(row=1, column=3, sticky=NSEW)

labelsPrint()

# Combo box
labelL = Label(root, text='Layer')
labelL.grid(row=2, column=1, sticky=(N, S, E, W))
TTTCBL = ttk.Combobox(root, state='readonly', values=['Top', 'Middle', 'Bottom'], textvariable=LayerChoice,width=10)  # L = layer
TTTCBL.bind("<<ComboboxSelected>>")
TTTCBL.grid(row=3, column=1, sticky=(N, S, E, W))

labelC = Label(root, text='Column')  # C = column
labelC.grid(row=2, column=2, sticky=(N, S, E, W))
TTTCBC = ttk.Combobox(root, state='readonly', values=['1', '2', '3'], textvariable=ColumnChoice, width=10)
TTTCBC.bind("<<ComboboxSelected>>")
TTTCBC.grid(row=3, column=2, sticky=(N, S, E, W))

labelR = Label(root, text='Row')  # R = row
labelR.grid(row=2, column=3, sticky=(N, S, E, W))
TTTCBR = ttk.Combobox(root, state='readonly', values=['1', '2', '3'], textvariable=RowChoice, width=10)
TTTCBR.bind("<<ComboboxSelected>>")
TTTCBR.grid(row=3, column=3, sticky=(N, S, E, W))

# Buttons
ButtonS = Button(root, text='Submit', command = check)
ButtonS.grid(row=4, column=2, sticky=(N, S, E, W))

ButtonC = Button(root, text='Clear', command = clear)
ButtonC.grid(row=4, column=3, sticky=(N, S, E, W))

# Win or lose label
labelWL = Label(root, text = "It Is Now Player X's Turn")
labelWL.grid(row=5, column=1, columnspan=3)

# Others
ttk.Sizegrip(root).grid(column=999, row=999, sticky=(N, S, E, W))
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_columnconfigure(3, weight=1)
root.grid_columnconfigure(4, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_rowconfigure(5, weight=1)
root.minsize(width=350, height=350)

root.title('3D Tic Tac Toe')
root.mainloop()
root.destroy()