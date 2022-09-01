from math import inf
from copy import deepcopy
import time


def mat(size):
    res = [[0] for _ in range(size)]
    for i in res:
        i.extend([0 for _ in range(size - 1)])
    return res


def isSubArray(A, B):
    n = len(A)
    m = len(B)
    i = 0
    j = 0
    while i < n and j < m:
        if A[i] == B[j]:
            i += 1
            j += 1
            if j == m:
                return True
        else:
            i = i - j + 1
            j = 0
    return False


class test:
    @staticmethod
    def row(grid, xr, yr):
        for x in range(xr[0], xr[1]):
            comptmax = 0
            comptmin = 0
            for y in range(yr[0], yr[1]):
                if grid[x][y] == 1:
                    comptmax += 1
                    comptmin = 0
                elif grid[x][y] == -1:
                    comptmin += 1
                    comptmax = 0
                else:
                    comptmax = 0
                    comptmin = 0
                if not (comptmax < 5 and comptmin < 5):
                    break
            if comptmin >= 5:
                return -1
            elif comptmax >= 5:
                return 1
        return 0

    @staticmethod
    def column(grid, xr, yr):
        for y in range(yr[0], yr[1]):
            comptmax = 0
            comptmin = 0
            for x in range(xr[0], xr[1]):
                if grid[x][y] == 1:
                    comptmax += 1
                    comptmin = 0
                elif grid[x][y] == -1:
                    comptmin += 1
                    comptmax = 0
                else:
                    comptmax = 0
                    comptmin = 0
                if not (comptmax < 5 and comptmin < 5):
                    break
            if comptmin >= 5:
                return -1
            elif comptmax >= 5:
                return 1
        return 0

    @staticmethod
    def diagonal_TLBR(grid, x, y):
        for k in range(x[0], x[1] + 1):
            i = k
            j = y[0]
            comptmin = 0
            comptmax = 0
            while i >= x[0] and j <= y[1] and comptmax < 5 and comptmin < 5:
                if grid[i][j] == 1:
                    comptmax += 1
                    comptmin = 0
                elif grid[i][j] == -1:
                    comptmin += 1
                    comptmax = 0
                else:
                    comptmax = 0
                    comptmin = 0
                i -= 1
                j += 1
            if comptmin >= 5:
                return -1
            elif comptmax >= 5:
                return 1
        for k in range(y[0] + 1, y[1] + 1):
            i = x[1]
            j = k
            comptmin = 0
            comptmax = 0
            while j <= y[1] and i >= x[0] and comptmax < 5 and comptmin < 5:
                if grid[i][j] == 1:
                    comptmax += 1
                    comptmin = 0
                elif grid[i][j] == -1:
                    comptmin += 1
                    comptmax = 0
                else:
                    comptmax = 0
                    comptmin = 0
                i -= 1
                j += 1
            if comptmin >= 5:
                return -1
            elif comptmax >= 5:
                return 1
        return 0

    @staticmethod
    def diagonal_BLTR(grid, x, y):
        for k in range(x[1], x[0] - 1, -1):
            i = k
            j = y[0]
            comptmin = 0
            comptmax = 0
            while i <= x[1] and j <= y[1] and comptmax < 5 and comptmin < 5:
                if grid[i][j] == 1:
                    comptmax += 1
                    comptmin = 0
                elif grid[i][j] == -1:
                    comptmin += 1
                    comptmax = 0
                else:
                    comptmax = 0
                    comptmin = 0
                i += 1
                j += 1
            if comptmin >= 5:
                return -1
            elif comptmax >= 5:
                return 1
        for k in range(y[0], y[1] + 1):
            i = x[0]
            j = k
            comptmin = 0
            comptmax = 0
            while j <= y[1] and i <= x[1] and comptmax < 5 and comptmin < 5:
                if grid[i][j] == 1:
                    comptmax += 1
                    comptmin = 0
                elif grid[i][j] == -1:
                    comptmin += 1
                    comptmax = 0
                else:
                    comptmax = 0
                    comptmin = 0
                i += 1
                j += 1
            if comptmin >= 5:
                return -1
            elif comptmax >= 5:
                return 1
        return 0

    @staticmethod
    def searchSpace(grid, size):
        delta = 4
        min_x = inf
        max_x = -inf
        min_y = inf
        max_y = -inf
        for i in range(size):
            for j in range(size):
                if grid[i][j] != 0:
                    if min_x > i:
                        min_x = i
                    if max_x < i:
                        max_x = i
                    if min_y > j:
                        min_y = j
                    if max_y < j:
                        max_y = j
        min_x -= delta
        max_x += delta
        min_y -= delta
        max_y += delta
        if min_x < 0:
            min_x = 0
        if min_y < 0:
            min_y = 0
        if max_x >= size:
            max_x = size - 1
        if max_y >= size:
            max_y = size - 1
        return [min_x, max_x], [min_y, max_y]


class gomoku:
    def __init__(self, size=15):
        self.size = size
        self.grid = mat(self.size)
        self.tour = True  # false : min joue || true : max joue
        self.x = [0, size - 1]
        self.y = [0, size - 1]
        self.shapesMax = []
        self.shapesMin = []
        self.history = []

    def InitShapes(self):
        ma = 1
        mi = -1
        c = 1
        self.shapesMax = []
        # patterns de 6
        self.shapesMax.append([[0, ma, ma, ma, ma, 0], c * 50000])
        self.shapesMax.append([[0, ma, ma, ma, 0, 0], c * 15000])
        self.shapesMax.append([[0, 0, ma, ma, ma, 0], c * 15000])
        self.shapesMax.append([[0, ma, ma, 0, ma, 0], c * 15000])
        self.shapesMax.append([[0, ma, 0, ma, ma, 0], c * 5000])
        self.shapesMax.append([[0, 0, ma, ma, 0, 0], c * 100])
        self.shapesMax.append([[0, 0, ma, 0, ma, 0], c * 100])
        self.shapesMax.append([[0, ma, 0, ma, 0, 0], c * 100])
        self.shapesMax.append([[0, 0, 0, ma, 0, 0], c * 10])
        self.shapesMax.append([[0, 0, ma, 0, 0, 0], c * 10])
        # patterns de 5
        self.shapesMax.append([[ma, ma, ma, ma, ma], c * 1000000])
        self.shapesMax.append([[ma, ma, ma, ma, 0], c * 20000])
        self.shapesMax.append([[0, ma, ma, ma, ma], c * 20000])
        self.shapesMax.append([[ma, ma, 0, ma, ma], c * 20000])
        self.shapesMax.append([[ma, 0, ma, ma, ma], c * 20000])
        self.shapesMax.append([[ma, ma, ma, 0, ma], c * 20000])
        self.shapesMax.append([[ma, ma, 0, ma, 0], c * 15000])
        self.shapesMax.append([[0, ma, 0, ma, ma], c * 15000])
        self.shapesMax.append([[ma, ma, 0, 0, ma], c * 15000])
        self.shapesMax.append([[ma, 0, 0, ma, ma], c * 15000])
        self.shapesMax.append([[ma, 0, ma, 0, ma], c * 15000])
        self.shapesMax.append([[0, ma, 0, ma, 0], c * 2500])
        self.shapesMax.append([[ma, 0, 0, 0, 0], c * 30])
        self.shapesMax.append([[0, ma, 0, 0, 0], c * 30])
        self.shapesMax.append([[0, 0, ma, 0, 0], c * 30])
        self.shapesMax.append([[0, 0, 0, ma, 0], c * 30])
        self.shapesMax.append([[0, 0, 0, 0, ma], c * 30])
        # patterns de 4
        self.shapesMax.append([[ma, ma, ma, 0, 0], c * 750])
        self.shapesMax.append([[0, 0, ma, ma, ma], c * 750])
        self.shapesMax.append([[0, ma, 0, ma, 0], c * 750])
        self.shapesMax.append([[ma, 0, ma, 0, 0], c * 750])

        ma = -1
        mi = 1
        c = 2
        self.shapesMin = []

        self.shapesMin.append([[0, ma, ma, ma, ma, 0], c * 50000])
        self.shapesMin.append([[0, ma, ma, ma, 0, 0], c * 15000])
        self.shapesMin.append([[0, 0, ma, ma, ma, 0], c * 15000])
        self.shapesMin.append([[0, ma, ma, 0, ma, 0], c * 15000])
        self.shapesMin.append([[0, ma, 0, ma, ma, 0], c * 500])
        self.shapesMin.append([[0, 0, ma, ma, 0, 0], c * 100])
        self.shapesMin.append([[0, 0, ma, 0, ma, 0], c * 100])
        self.shapesMin.append([[0, ma, 0, ma, 0, 0], c * 100])
        self.shapesMin.append([[0, 0, 0, ma, 0, 0], c * 10])
        self.shapesMin.append([[0, 0, ma, 0, 0, 0], c * 10])
        # patterns de 5
        self.shapesMin.append([[ma, ma, ma, ma, ma], c * 1000000])
        self.shapesMin.append([[ma, ma, ma, ma, 0], c * 20000])
        self.shapesMin.append([[0, ma, ma, ma, ma], c * 20000])
        self.shapesMin.append([[ma, ma, 0, ma, ma], c * 20000])
        self.shapesMin.append([[ma, 0, ma, ma, ma], c * 20000])
        self.shapesMin.append([[ma, ma, ma, 0, ma], c * 20000])
        self.shapesMin.append([[ma, ma, 0, ma, 0], c * 15000])
        self.shapesMin.append([[0, ma, 0, ma, ma], c * 15000])
        self.shapesMin.append([[ma, ma, 0, 0, ma], c * 15000])
        self.shapesMin.append([[ma, 0, 0, ma, ma], c * 15000])
        self.shapesMin.append([[ma, 0, ma, 0, ma], c * 15000])
        self.shapesMin.append([[0, ma, 0, ma, 0], c * 2500])
        self.shapesMin.append([[ma, 0, 0, 0, 0], c * 30])
        self.shapesMin.append([[0, ma, 0, 0, 0], c * 30])
        self.shapesMin.append([[0, 0, ma, 0, 0], c * 30])
        self.shapesMin.append([[0, 0, 0, ma, 0], c * 30])
        self.shapesMin.append([[0, 0, 0, 0, ma], c * 30])
        # patterns de 4
        self.shapesMin.append([[ma, ma, ma, 0, 0], c * 750])
        self.shapesMin.append([[0, 0, ma, ma, ma], c * 750])
        self.shapesMin.append([[0, ma, 0, ma, 0], c * 750])
        self.shapesMin.append([[ma, 0, ma, 0, 0], c * 750])

    def Score(self):
        scoring = 0
        # rows
        for i in range(self.x[0], self.x[1] + 1):
            cur = []
            for j in range(self.y[0], self.y[1] + 1):
                cur.append(self.grid[i][j])
            for k in self.shapesMax:
                if isSubArray(cur, k[0]):
                    scoring += k[1]
            for l in self.shapesMin:
                if isSubArray(cur, l[0]):
                    scoring += l[1]

        # cols
        for j in range(self.y[0], self.y[1] + 1):
            cur = []
            for i in range(self.x[0], self.x[1] + 1):
                cur.append(self.grid[i][j])
            for k in self.shapesMax:
                if isSubArray(cur, k[0]):
                    scoring += k[1]
            for l in self.shapesMin:
                if isSubArray(cur, l[0]):
                    scoring += l[1]

        # diagonale_BLTR
        for k in range(self.x[1], self.x[0] - 1, -1):
            i = k
            j = self.y[0]
            cur = []
            while i <= self.x[1] and j <= self.y[1]:
                cur.append(self.grid[i][j])
                i += 1
                j += 1
            for l in self.shapesMax:
                if isSubArray(cur, l[0]):
                    scoring += l[1]
            for m in self.shapesMin:
                if isSubArray(cur, m[0]):
                    scoring += m[1]
        for k in range(self.y[0], self.y[1] + 1):
            i = self.x[0]
            j = k

            while j <= self.y[1] and i <= self.x[1]:
                cur.append(self.grid[i][j])
                i += 1
                j += 1
            for l in self.shapesMax:
                if isSubArray(cur, l[0]):
                    scoring += l[1]
            for m in self.shapesMin:
                if isSubArray(cur, m[0]):
                    scoring += m[1]

        # diagonale_TLBR
        for k in range(self.x[0], self.x[1] + 1):
            i = k
            j = self.y[0]
            cur = []
            while i >= self.x[0] and j <= self.y[1]:
                cur.append(self.grid[i][j])
                i -= 1
                j += 1
            for l in self.shapesMax:
                if isSubArray(cur, l[0]):
                    scoring += l[1]
            for m in self.shapesMin:
                if isSubArray(cur, m[0]):
                    scoring += m[1]
        for k in range(self.y[0] + 1, self.y[1] + 1):
            i = self.x[1]
            j = k
            cur = []
            while j <= self.y[1] and i >= self.x[0]:
                cur.append(self.grid[i][j])
                i -= 1
                j += 1
            for l in self.shapesMax:
                if isSubArray(cur, l[0]):
                    scoring += l[1]
            for m in self.shapesMin:
                if isSubArray(cur, m[0]):
                    scoring += m[1]
        return scoring

    def LimitSearchSpace(self):
        self.x, self.y = test.searchSpace(self.grid, self.size)

    def Actions(self):
        res = []
        for i in range(self.x[0], self.x[1] + 1):
            for j in range(self.y[0], self.y[1] + 1):
                if self.grid[i][j] == 0:
                    res.append([i, j])
        return res

    def CloseActions(self):
        res = []
        for i in range(self.x[0], self.x[1] + 1):
            for j in range(self.y[0], self.y[1] + 1):
                if self.grid[i][j] != 0:
                    for k in range(i - 1, i + 2):
                        for l in range(j - 1, j + 2):
                            if 0 <= k < self.size and 0 <= l < self.size:
                                if self.grid[k][l] == 0:
                                    res.append((k, l))
        res = list(set(res))
        return res

    def Result(self, a):
        res = []
        for i in a:
            new = []
            new = deepcopy(self.grid)
            if self.tour:
                new[i[0]][i[1]] = 1
            else:
                new[i[0]][i[1]] = -1
            res.append([new, i[:]])
        return res

    def TerminalTest(self):
        if test.row(self.grid, self.x, self.y) != 0:
            return True
        if test.column(self.grid, self.x, self.y) != 0:
            return True
        if test.diagonal_TLBR(self.grid, self.x, self.y) != 0:
            return True
        if test.diagonal_BLTR(self.grid, self.x, self.y) != 0:
            return True
        if len(self.Actions()) == 0:
            return True

        return False

    def Utility(self):
        row = test.row(self.grid, self.x, self.y)
        col = test.column(self.grid, self.x, self.y)
        diag_TLBR = test.diagonal_TLBR(self.grid, self.x, self.y)
        diag_BLTR = test.diagonal_BLTR(self.grid, self.x, self.y)
        return row + col + diag_BLTR + diag_TLBR

    def __str__(self):
        res = ""
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
        numbers = [str(i) for i in range(15, -1, -1)]
        correspondances = {1: "O", -1: "X", 0: " "}
        compt = 0

        for i in self.grid:
            if int(numbers[compt]) >= 10:
                res += f"|{numbers[compt]}|"
            else:
                res += f"| {numbers[compt]}|"
            for j in i:
                res += f" {correspondances[j]} |"
            res += "\n"
            compt += 1
        res += "   | "
        for i in letters:
            res += f"{i} | "
        return res

def conversioncoord(a, b):
    y = ord(a.lower()) - 97
    x = 15 - int(b)
    return [x, y]

def minmax(node: gomoku, depth, alpha, beta):
    if depth == 0 or node.TerminalTest():
        return node.Utility()
    else:
        if not node.tour:
            v = inf
            for fils in node.Result(node.CloseActions()):
                new = gomoku()
                new.grid = fils[0][:]
                new.tour = True
                new.LimitSearchSpace()
                vmin = minmax(new, depth - 1, alpha, beta)
                v = min(v, vmin)
                if alpha >= v:
                    return v
                beta = min(beta, v)
        else:
            v = -inf
            for fils in node.Result(node.CloseActions()):
                new = gomoku()
                new.grid = fils[0][:]
                new.tour = False
                new.LimitSearchSpace()
                vmax = minmax(new, depth - 1, alpha, beta)
                v = max(v, vmax)
                if v >= beta:
                    return v
                alpha = max(alpha, v)
    return v


def path(state, style):
    moves = state.Result(state.CloseActions())
    l = []
    for grille in moves:
        new = gomoku()
        new.grid = grille[0][:]
        new.InitShapes()
        val = new.Score()
        move = grille[1]
        l.append([val, [move]])

    j = sorted(l, key=lambda x: x[0], reverse=style)
    return j[0]


def pathminmax(state, depth, style):
    heur = path(state, style)[1][0]
    print(heur)
    next_move = 0
    val1 = -inf
    alpha = -inf
    beta = inf
    moves = state.Result(state.CloseActions())
    T0 = time.time()
    for grille in moves:
        T1 = time.time()
        if T1 - T0 < 4.9:
            new = gomoku()
            new.grid = grille[0][:]
            new.tour = False

            val = minmax(new, depth - 1, alpha, beta)
            T1 = time.time()

            if val > val1:
                next_move = grille[1]
                val1 = val

            alpha = max(alpha, val1)

    if val == 1:
        style = True
        next_move = heur
    if minmax(new, depth - 1, alpha, beta) == -1:
        style = False
        print("attention")
        next_move = heur
    if val == 0:
        next_move = heur
        style = False

    return next_move, style


def partieContreIA():
    new = gomoku()
    print("Qui joue en premier 2.IA 1.joueur ?")
    tour = input()
    style = False
    if tour == "2":
        # Premier tour IA
        new.grid[7][7] = 1
        print(new)
        while not new.TerminalTest():

            print("x:")
            x = input()
            print("y:")
            y = input()
            l = conversioncoord(x, y)
            new.grid[l[0]][l[1]] = -1
            new.LimitSearchSpace()
            new.InitShapes()
            if not new.TerminalTest():
                # print(style)
                t0 = time.time()
                l2, style = pathminmax(new, 3, style)
                new.grid[l2[0]][l2[1]] = 1
                print(new)
                T1 = time.time()
                delta = T1 - t0
                # print(delta)

    if tour == "1":
        while not new.TerminalTest():

            # Premier tour joeur
            print("x:")
            x = input()
            print("y:")
            y = input()
            l = conversioncoord(x, y)
            new.grid[l[0]][l[1]] = -1
            new.LimitSearchSpace()
            new.InitShapes()
            if not new.TerminalTest():
                t0 = time.time()
                # l2 = path(new)[1][0]
                l2, style = pathminmax(new, 3, style)
                new.grid[l2[0]][l2[1]] = 1
                T1 = time.time()
                delta = T1 - t0
                print(new)
                # print(delta)

    print(new)
    a = test.row(new.grid, new.x, new.y) + test.column(new.grid, new.x, new.y) + test.diagonal_BLTR(new.grid, new.x,
                                                                                                    new.y) + test.diagonal_TLBR(
        new.grid, new.x, new.y)
    if a == 1:
        a = "joueur 1"
    if a == -1:
        a = "joueur 2"
    print("bravo " + a + " a gagné")


partieContreIA()
