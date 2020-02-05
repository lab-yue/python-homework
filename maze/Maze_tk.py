import tkinter as tk
import sys
import time
from random import randint, choice


class Direction:
    UP = [0, -1]
    DOWN = [0, 1]
    LEFT = [-1, 0]
    RIGHT = [1, 0]

    ALL = [
        UP,
        DOWN,
        LEFT,
        RIGHT,
    ]
    MAP = {
        "w": UP,
        "s": DOWN,
        "a": LEFT,
        "d": RIGHT,
    }


class Cell:
    PLAYER = "👻"
    OPEN = "yellow"
    CLOSE = "black"
    GOAL = "blue"

    def __init__(self):
        self.status = Cell.CLOSE
        self.options = [*Direction.ALL]

    def open(self):
        self.status = Cell.OPEN

    @property
    def isClose(self):
        return self.status == Cell.CLOSE


class Maze:

    def __init__(self, size=5):
        self._visited = []
        self._width = size
        self._height = size
        self._map = [[Cell() for _ in range(size)] for _ in range(size)]
        self._created = False
        self._movingPostion = None
        self._goalPostion = None
        self._path = []

        [x, y] = self.randomPoint()
        startPoint = self._map[x][y]
        startPoint.open()
        self._path.append(startPoint)
        self._visited.append([x, y])

    @property
    def playerPostion(self):
        return self._movingPostion if self._created else self._visited[-1]

    def getCell(self, x, y) -> Cell:
        if (
            0 <= x <= self._width - 1 and
            0 <= y <= self._height - 1
        ):
            return self._map[x][y]
        else:
            return None

    def dig(self) -> int:
        [x, y] = self.playerPostion
        cell = self._map[x][y]

        while len(cell.options):
            option = choice(cell.options)
            cell.options.remove(option)
            [dx, dy] = option
            one_forward_position = [x + dx, y + dy]
            two_forward_position = [x + 2 * dx, y + 2 * dy]
            one_forward = self.getCell(*one_forward_position)
            two_forward = self.getCell(*two_forward_position)
            if (
                one_forward and
                two_forward and
                one_forward.isClose and
                two_forward.isClose
            ):
                one_forward.open()
                two_forward.open()
                self._path.append(one_forward_position)
                self._path.append(two_forward_position)
                self._visited.append(two_forward_position)
                return
        self._visited.pop()
        if len(self._visited) == 0:
            self._created = True
            self._movingPostion = [x, y]
            while True:
                maybe_goal_postion = self.randomPointfromMap()
                if maybe_goal_postion != self.playerPostion:
                    self._goalPostion = maybe_goal_postion
                    break
            print(self._goalPostion)

    def randomPoint(self) -> [int, int]:
        return [randint(0, self._width - 1), randint(0, self._height - 1)]

    def randomPointfromMap(self) -> [int, int]:
        [x, y] = choice(self._path)
        return [x, y]


class Game(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.level = 5
        self.create_widgets()
        self.master.bind('<Configure>', self.resize)
        self.maze = Maze(self.level)
        self.do_one_frame()
        self.focus_set()
        self.bind_keys()

    def bind_keys(self):
        self.bind("<Key>", self.handle_key)

    def handle_key(self, event):
        if not self.maze._created:
            print("please wait")
            return
        key = event.char
        print(key)
        if key == 'q':
            sys.exit(0)
        if (key not in Direction.MAP):
            return
        [x, y] = self.maze.playerPostion
        [dx, dy] = Direction.MAP[key]
        cell = self.maze.getCell(x+dx, y+dy)

        if cell and not cell.isClose:
            self.maze._movingPostion = [x+dx, y+dy]
            self.draw()

        if self.maze._goalPostion == [x+dx, y+dy]:
            self.level += 2
            self.maze = Maze(self.level)

            self.canvas.config(
                width=self.level*30+10,
                height=self.level*30+10
            )
            self.do_one_frame()

    def resize(self, event):
        self.w = event.width
        self.h = event.height

    def do_one_frame(self):

        if not self.maze._created:
            self.maze.dig()
            self.draw()
            self.after(100, self.do_one_frame)
        else:
            self.draw()

    def create_widgets(self):
        self.title = tk.Label(self, font=("Courier", 30))
        self.title.pack(side="top")
        self.canvas = tk.Canvas(self)
        self.canvas.config(width=400, height=400)
        self.canvas.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def draw(self):
        self.title.config(text=f"level- {self.level}x{self.level}")
        for x, row in enumerate(self.maze._map):
            for y, cell in enumerate(row):
                fill = "red"

                if (self.maze.playerPostion == [x, y]):
                    fill = "red"
                elif self.maze._goalPostion == [x, y]:
                    fill = "blue"
                else:
                    fill = cell.status
                self.canvas.create_rectangle(
                    x * 30,
                    y * 30,
                    x * 30 + 25,
                    y * 30 + 25,
                    fill=fill
                )


if __name__ == '__main__':
    root = tk.Tk()
    app = Game(master=root)
    app.mainloop()
