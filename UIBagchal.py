from tkinter import *

from bagh_goat import *
import time

# from ChalMove import createBagh

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

    def __init__(self, canvas, statustext,root):
        self.root=root
        self.canvas = canvas  # Canvas where board is drawn
        self.statustext = statustext  # gives information about grid
        self.board_grid_x = [80, 180, 280, 380, 480]  # x cordinates for lines

        self.board_grid_y = [80, 180, 280, 380, 480]
        self.board_rect = [50, 50, 512, 512]
        self.coordinate_index_map = {}
        self.draw_board()
        self.create_PlaceGoatButton()

        self.coordinate_mapping()


    def draw_board(self):
        self.canvas.create_rectangle(*self.board_rect, fill='yellow')

        board_min_x = self.board_grid_x[0]
        board_max_x = self.board_grid_x[-1]
        board_min_y = self.board_grid_y[0]
        board_max_y = self.board_grid_y[-1]
        board_center_x = self.board_grid_x[2]
        board_center_y = self.board_grid_y[2]

        # create points chart:
        self.canvas.create_rectangle(680,25,795,49,fill="yellow")
        self.canvas.create_text(720, 38, text="Points",font=("Purisa", 13))

        self.canvas.create_rectangle(680,49,770,74,fill="yellow")
        self.canvas.create_rectangle(770,49,795,74,fill="white",outline="black")
        self.canvas.create_text(720, 65, text="Bagh",font=("Purisa", 13))
        
        self.canvas.create_rectangle(680,75,770,100,fill="yellow")
        self.canvas.create_rectangle(770,75,795,100,fill="white",outline="black")
        self.canvas.create_text(720, 90, text="Goat",font=("Purisa", 13))
        
        
        self.canvas.create_rectangle(680,180,770,205,fill="yellow")
        self.canvas.create_rectangle(770,180,795,205,fill="white",outline="black")
        self.canvas.create_text(720, 190, text="Alive Goat",font=("Purisa", 11))
        for x in self.board_grid_x:
            self.canvas.create_line(x, board_min_y, x, board_max_y)  # vertical lines

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
    # this function create a place goat button in the UI, this button adds a goat in the board
    def create_PlaceGoatButton(self):
        # create button to place goat, 680,235
           
  
        # Creating a Button , which calles creat_goat function on press, 
        placeGoatbtn = Button(self.root, text = 'Place a new Goat',bd=4,bg="yellow",font=("Purisa", 10), command=creat_goat)
  
        #    Set the position of button to coordinate (100, 20)
        placeGoatbtn.place(x=680, y=235)


    def new_game(self):
        print("Not Yet Implemented")

    def coordinate_mapping(self):
        k = 0
        for j in range(len(self.board_grid_x)):
            for i in range(len(self.board_grid_y)):
                self.coordinate_index_map[k] = (self.board_grid_x[i], self.board_grid_y[j])
                k += 1


# this class will be responsible to show, whose chal is pending
class whotomove():
    def __init__(self, canvas):
        self.bagbox = None
        self.canvas = canvas
        self.draw_baghngoat_box()
        self.baghToMove = True
        self.goatToMove = False

    # creates initial bxes, orange one will be on to move, i.e bagh
    def draw_baghngoat_box(self):
        self.bagbox = self.canvas.create_rectangle(138, 2, 230, 23, outline="black", fill="orange")
        self.baghboxtxt = self.canvas.create_text(176, 12, text="Tiger", font=("Purisa", 15))
        self.goatbox = self.canvas.create_rectangle(230, 2, 300, 23, outline="black", fill="lightblue")
        self.goatboxtxt = self.canvas.create_text(266, 12, text="Goat", font=("Purisa", 15))

    # this function will switch after a mouse click , who to move
    def switchRole(self, eventorigin):
        print("switch")
        if self.baghToMove:  # if bagh is active, it's for goats turn to orange
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


def get_index(coordinate):
    key_list = list(coordinate_index_map.keys())
    val_list = list(coordinate_index_map.values())
    position = val_list.index(coordinate)
    key_dictionary = key_list[position]
    return key_dictionary  # key of value


def about_bagchal():
    print("Implemented Not Yet")


def configure():
    print("Implemented Not Yet")


def getorigin(eventorigin):
    global x, y
    x = eventorigin.x
    y = eventorigin.y
    print(x, y)


def openPhoto():
    global baghPhoto, goatPhoto
    baghPhoto = PhotoImage(file="bagh.png")
    goatPhoto = PhotoImage(file="goat.png")


def createBagh(canvas, baghPhoto):
    baghObj1 = baghClass(480, 80, canvas, baghPhoto)
    baghList.append(baghObj1)
    baghObj1 = baghClass(480, 480, canvas, baghPhoto)
    baghList.append(baghObj1)
    baghObj1 = baghClass(80, 80, canvas, baghPhoto)
    baghList.append(baghObj1)
    baghObj1 = baghClass(80, 480, canvas, baghPhoto)
    baghList.append(baghObj1)

    print("bagh count : "+str(len(baghList)))
# this function creates a goat, & adds on board
def creat_goat():
    goatObj1 = goatClass(80, 180, canvas, goatPhoto)
    goatList.append(baghObj1)




   
# move bagh[0] to the point mouse clicked
def possibleMoveForBagh(mousex,mousey,i):
    

    print(str(mousex-baghList[i].x)+" "+str(mousey-baghList[i].y))

    from_position = get_index((baghList[i].x, baghList[i].y))
    print(from_position)
    path_list = baghList[i].possible_move_list(from_position)
    oval_list = possible_path_circle(path_list)
    return oval_list
    # print(str(mousex - baghList[0].x) + " " + str(mousey - baghList[0].y))

    
def moveBagh(mousex,mousey,i):
    from_position = get_index((baghList[i].x, baghList[i].y))
    rint("moving")
    # canvas.move(img object, what to minus form imageY,what to add to imageY)
    if baghList[i].is_valid_move(from_position, mousex, mousey)[0]:
        val = baghList[i].is_valid_move(from_position, mousex, mousey)[1]
        tup_x, tup_y = coordinate_index_map[val]
        # print(tup)
        canvas.move(baghList[i].baghImg, mousex - baghList[i].x, mousey - baghList[i].y)
        baghList[i].x = tup_x  # update bagh[0]'s coordinate
        baghList[i].y = tup_y
        print("moved")
        #clear_possible_ovals(oval_list)

def clear_possible_ovals(oval_list):
    for oval_name in oval_list:
        canvas.delete(oval_name)
        print("deleted "+str(oval_name))
    oval_list.clear()

def possible_path_circle(path_list):
    r = 15
    oval_list = list()
    for i in path_list:
        x, y = coordinate_index_map[i]
        oval_name = create_circle(x, y, r, canvas)
        oval_list.append(oval_name)
        #canvas.delete(oval_name)
        print(oval_name)
    print("oval lists :")
    print(oval_list)
    return oval_list


def create_circle(x, y, r, canvasName):  # center coordinates, radius
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1)

#def checkifClickedOnBagh(eventorigin):

def mouseControl(eventorigin):
    
    mousex = eventorigin.x
    mousey = eventorigin.y
    baghOvalList=list()
    banghNo = 0
    global baghClickedFlag
    if baghClickedFlag:
        moveBagh(mousex,mousey,baghNo)
        baghClickedFlag=False
        clear_possible_ovals(baghOvalList)
    # check if click on a bagh : 
    for i in range(4):
        if baghList[i].if_clicked_on_bagh(mousex,mousey):
            baghOvalList=possibleMoveForBagh(mousex,mousey,i)
            print("bagh "+str(i)+" clicked")
            baghClickedFlag = True
            baghNo=i
            break
    

def application():
    root = Tk()
    root.geometry("800x600")
    root.title("Bagchal by Sadnan,Zulker and Iftakhar")
    root.resizable(False, False)
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=1)
    global canvas
    canvas = Canvas(frame, width=700, height=550, bg="white")
    canvas.pack(fill=BOTH, expand=1, side=TOP, padx=1, pady=1)
    statustext = StringVar()
    status = Label(frame, textvariable=statustext,
                   borderwidth=2, relief=RIDGE)
    status.pack(expand=1, side=BOTTOM, fill=X)
    game = UIBaghchal(canvas, statustext,root)
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

    # open the two photos
    openPhoto()
    # create 4 bagh aat 4 corners
    createBagh(canvas, baghPhoto)
    # baghList[0].x=280
    # baghList[0].y=280
    # canvas.move(baghList[0].baghImg,80,280) # this move is done by adding values to x,y
    # time.sleep(10)

    # root.after(2000,createBagh(canvas, baghPhoto))

    # canvas.delete(bagh1)  #delete bagh image

    # this binding of button 1 is for left mouse click, if click happens, tiger & goat box
    # will switch color

    # root.bind("<Button 1>",whotomoveobj.switchRole)
    # root.bind("<Button 1>",getorigin)  # get coordinate on mouse click

    root.bind("<Button 1>", mouseControl)
    print(type(baghList[0]))
    root.mainloop()


baghList=[] # baghlist global variable
goatList=[]
application()
