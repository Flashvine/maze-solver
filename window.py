from tkinter import Tk, BOTH, Canvas

from graphics import Line

class Window():
    def __init__(self, height, width):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill="both", expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running == True:
            self.redraw()
        print("Window closed...")

    def close(self):
        self.__running = False

    def draw_line(self, line, color):
        line.draw(self.__canvas, color)