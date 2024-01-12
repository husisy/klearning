# https://forum.taichi.graphics/t/homework0-barnsleyfern/804
import os
import math
import random
import taichi as ti

def next_tbd_dir(dir0='tbd00', maximum_int=100000):
    if not os.path.exists(dir0): os.makedirs(dir0)
    tmp1 = [x for x in os.listdir(dir0) if x[:3]=='tbd']
    exist_set = {x[3:] for x in tmp1}
    while True:
        tmp1 = str(random.randint(1,maximum_int))
        if tmp1 not in exist_set: break
    tbd_dir = os.path.join(dir0, 'tbd'+tmp1)
    os.mkdir(tbd_dir)
    return tbd_dir

ti.init(arch=ti.cpu)

width = 330 #660
height = 500 #1000
pixels = ti.field(ti.f32, shape=(width, height, 3))
pixels = ti.Vector.field(3, dtype=ti.f32, shape=(width, height))


@ti.func
def generatePoint(x, y, t):
    r = ti.random()
    nextX = 0.0
    nextY = 0.0
    if(r < 0.01):
        nextX = 0
        nextY = 0.16*y
    elif(r < 0.85):
        nextX = 0.85*x + (0.04 + t)*y
        nextY = -(0.04 + t)*x + 0.85*y + 1.6
    elif(r < 0.93):
        nextX =  0.20*x + -0.26*y
        nextY = 0.23*x + 0.22*y + 1.0
    else:
        nextX =  -0.15*x + 0.28*y
        nextY = 0.26*x + 0.24*y + 0.44
    return nextX, nextY

@ti.kernel
def drawPoint(t: ti.f32):
    for i in range(0, 100000):
        x = 0.0
        y = 0.0
        for j in range(0, 40):
            x, y = generatePoint(x, y, t)
            pixels[(int)((x/6+0.5)*width), (int)(y*height/10.5)][0] += 0.01
            pixels[(int)((x/6+0.5)*width), (int)(y*height/10.5)][1] += 0.02
            pixels[(int)((x/6+0.5)*width), (int)(y*height/10.5)][2] += 0.005


gui = ti.GUI("BarnsleyFern", (width, height))

# work_dir = next_tbd_dir()
# video_manager = ti.VideoManager(output_dir=work_dir, framerate=24, automatic_build=False)
t = 0.0
while gui.running:
    t += 0.08
    drawPoint(math.sin(t)*0.03)
    gui.set_image(pixels)
    gui.show()
    # video_manager.write_frame(pixels.to_numpy())
    pixels.fill(0)
# video_manager.make_video(gif=True, mp4=False)
