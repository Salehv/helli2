import turtle as t

def islamic_draw(repeat, rotation, pencolor, fillcolor, function, *args):
    t.speed(-1)
    t.home()
    t.color(pencolor, fillcolor)
    for i in range(repeat):
        begin_fill()
        function(*args)
        end_fill()
        t.left(rotation)
    t.color("black", "black")
    t.home()


    
