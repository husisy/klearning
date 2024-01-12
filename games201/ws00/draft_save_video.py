import os
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

pixels = ti.field(ti.u8, shape=(512, 512, 3))

@ti.kernel
def paint():
    for i, j, k in pixels:
        pixels[i, j, k] = ti.random(ti.float32) * 255

result_dir = next_tbd_dir()
video_manager = ti.VideoManager(output_dir=result_dir, framerate=24, automatic_build=False)

for _ in range(50):
    paint()
    video_manager.write_frame(pixels.to_numpy())

video_manager.make_video(gif=True, mp4=True)
print(video_manager.get_output_filename('.mp4'))
print(video_manager.get_output_filename('.gif'))
