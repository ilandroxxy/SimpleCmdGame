from random import randint as rand


def randbool(r,mxr):
    t = rand(0,mxr)
    return(t<= r)

def randcell(w, h):
    tw = rand(0, w - 1 ) #ширина
    th = rand(0, h - 1) #высота
    return(th, tw)

#генерирует на какую клетку пападаем
def randcell2(x,y):
    #        вверх  направо  вниз   налево
    moves = [(-1,0), (0,1), (1,0), (0,-1)]
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1]
    return(x + dx, y + dy)