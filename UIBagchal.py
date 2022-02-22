from tkinter import *

from bagh_goat import *
#from ChalMove import createBagh

""" 
class baghClass():
    #baghphoto  = PhotoImage(file="bagh.png")
    def __init__(self,x,y,canvas,baghPhoto):
        self.x=x
        self.y = y
        self.canvas = canvas
        self.baghPhoto=baghPhoto
        
        self.draw_bagh()
        
        
    def draw_bagh(self):
        self.bagh = self.canvas.create_image(self.x, self.y,  image=self.baghPhoto) # bagh image created
   """   
  
    
class UIBaghchal(object):
    '''UI class of Bagchal game'''

    def __init__(self, canvas, statustext):
        self.canvas = canvas #Canvas where board is drawn
        self.statustext = statustext #gives information about grid
        self.board_grid_x = [80, 180, 280, 380, 480]#x cordinates for lines
        self.board_grid_y = [80, 180, 280, 380, 480]
        self.board_rect = [50, 50, 512, 512]
        self.draw_board()

    def draw_board(self):
        self.canvas.create_rectangle(*self.board_rect, fill='yellow')

        board_min_x = self.board_grid_x[0]
        board_max_x = self.board_grid_x[-1]
        board_min_y = self.board_grid_y[0]
        board_max_y = self.board_grid_y[-1]
        board_center_x = self.board_grid_x[2]
        board_center_y = self.board_grid_y[2]

        for x in self.board_grid_x:
            self.canvas.create_line(x, board_min_y, x, board_max_y)#vertical lines

        for y in self.board_grid_y:
            self.canvas.create_line(board_min_x, y, board_max_x, y)
        self.canvas.create_line(board_min_x, board_min_y,
                                board_max_x + 1, board_max_y + 1)
        self.canvas.create_line(board_min_x, board_max_y,
                                board_max_x, board_min_y)

        self.canvas.create_line(board_center_x, board_min_y,
                                board_max_x, board_center_y)
        self.canvas.create_line(board_max_x, board_center_y,
                                board_center_x, board_max_y)
        self.canvas.create_line(board_center_x, board_max_y,
                                board_min_x, board_center_y)
        self.canvas.create_line(board_min_x, board_center_y,
                                board_center_x, board_min_y)

    def new_game(self):
        print("Not Yet Implemented")
# this class will be responsible to show, whose chal is pending
class whotomove():
    def __init__(self, canvas):
        self.canvas = canvas
        self.draw_baghngoat_box()
        self.baghToMove = True
        self.goatToMove = False
    # creates initial bxes, orange one will be on to move, i.e bagh
    def draw_baghngoat_box(self):
        self.bagbox = self.canvas.create_rectangle(138,2,230,23,outline = "black", fill = "orange")
        self.baghboxtxt = self.canvas.create_text(176, 12, text="Tiger",font=("Purisa", 15))
        self.goatbox = self.canvas.create_rectangle(230,2,300,23,outline = "black", fill = "lightblue")
        self.goatboxtxt = self.canvas.create_text(266, 12, text="Goat",font=("Purisa", 15))
        
    #this function will switch after a mouse click , who to move
    def switchRole(self,eventorigin):
        print("switch")
        if self.baghToMove: # if bagh is active, it's for goats turn to orange
            self.canvas.itemconfig(self.bagbox, fill='lightblue')
            self.canvas.itemconfig(self.goatbox, fill='orange')
            self.baghToMove = False
            self.goatToMove = True
        else:
            self.canvas.itemconfig(self.bagbox, fill='orange')
            self.canvas.itemconfig(self.goatbox, fill='lightblue')
            self.baghToMove = True
            self.goatToMove = False
def rules_bagchal():
    import webbrowser
    webbrowser.open("https://en.wikipedia.org/wiki/Bagh_Chal")


def about_bagchal():
    print("Implemented Not Yet")


def configure():
    print("Implemented Not Yet")

def getorigin(eventorigin):
      global x,y
      x = eventorigin.x
      y = eventorigin.y
      print(x,y)

def openPhoto():
    global baghPhoto,goatPhoto
    baghPhoto  = PhotoImage(file="bagh.png")
    goatPhoto  = PhotoImage(file="goat.png")
def createBagh(canvas,baghPhoto):
   
    
    baghObj1 = baghClass(480, 80, canvas, baghPhoto)
    baghList.append(baghObj1)
    baghObj1 = baghClass(480, 480, canvas, baghPhoto)
    baghList.append(baghObj1)
    baghObj1 = baghClass(80, 80, canvas, baghPhoto)
    baghList.append(baghObj1)
    baghObj1 = baghClass(80, 480, canvas, baghPhoto)
    baghList.append(baghObj1)
    print("bagh count : "+str(len(baghList)))

def application():
    root = Tk()
    root.title("Bagchal by Sadnan,Zulker and Iftakhar")
    root.resizable(False, False)
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=1)
    canvas = Canvas(frame, width=700, height=550, bg="white")
    canvas.pack(fill=BOTH, expand=1, side=TOP, padx=1, pady=1)
    statustext = StringVar()
    status = Label(frame, textvariable=statustext,
                   borderwidth=2, relief=RIDGE)
    status.pack(expand=1, side=BOTTOM, fill=X)
    game = UIBaghchal(canvas, statustext)
    menu = Menu(root)
    root['menu'] = menu
    gamemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label='Game', menu=gamemenu)

    gamemenu.add_command(label='New Game', command=game.new_game)
    gamemenu.add_separator()
    gamemenu.add_command(label='Undo')
    gamemenu.add_separator()
    gamemenu.add_command(label='Quit', command=root.destroy)

    settings = Menu(menu, tearoff=0)
    menu.add_cascade(label='Settings', menu=settings)

    settings.add_command(label='Preferences', command=configure)

    help = Menu(menu, tearoff=0)
    menu.add_cascade(label='Help', menu=help)

    help.add_command(label='Rules', command=rules_bagchal)
    help.add_command(label='About', command=about_bagchal)
    print(statustext)

    # create whotomove box
    whotomoveobj = whotomove(canvas)
    #whotomoveobj.switchRole()
    # open the two photos
    openPhoto()
    createBagh(canvas, baghPhoto)
   
    #baghObj2 = baghClass(480, 480, canvas, baghPhoto)
    #bagho = canvas.create_image(80,480 , image=baghPhoto) # bagh image created
  
    #canvas.delete(bagh1)  #delete bagh image

    # this binding of button 1 is for left mouse click, if click happens, tiger & goat box
    # will switch color
    root.bind("<Button 1>",whotomoveobj.switchRole)
    #root.bind("<Button 1>",getorigin)  # get coordinate on mouse click
    root.mainloop()

baghList=[]
application()
