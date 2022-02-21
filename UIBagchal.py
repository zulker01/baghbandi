from tkinter import *


class UIBaghchal(object):
    '''UI class of Bagchal game'''

    def __init__(self, canvas, statustext):
        self.canvas = canvas #Canvas where board is drawn
        self.statustext = statustext #gives information about grid
        self.board_grid_x = [80, 180, 280, 380, 480]
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


def rules_bagchal():
    import webbrowser
    webbrowser.open("https://en.wikipedia.org/wiki/Bagh_Chal")


def about_bagchal():
    print("Implemented Not Yet")


def configure():
    print("Implemented Not Yet")


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

    root.mainloop()


application()
