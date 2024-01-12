import os
import random
import taichi as ti
import numpy as np

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

num_vertices = 1000
pos = ti.Vector.field(3, dtype=ti.f32, shape=(10, 10, 10))
rgba = ti.Vector.field(4, dtype=ti.f32, shape=(10, 10, 10))


@ti.kernel
def place_pos():
    for i, j, k in pos:
        pos[i, j, k] = 0.1 * ti.Vector([i, j, k])


@ti.kernel
def move_particles():
    for i, j, k in pos:
        pos[i, j, k] += ti.Vector([0.1, 0.1, 0.1])


@ti.kernel
def fill_rgba():
    for i, j, k in rgba:
        rgba[i, j, k] = ti.Vector(
            [ti.random(), ti.random(), ti.random(), ti.random()])


place_pos()
work_dir = next_tbd_dir()
series_prefix = os.path.join(work_dir, 'example.ply')
# series_prefix = "example.ply"
for frame in range(10):
    move_particles()
    fill_rgba()
    # now adding each channel only supports passing individual np.array
    # so converting into np.ndarray, reshape
    # remember to use a temp var to store so you dont have to convert back
    np_pos = np.reshape(pos.to_numpy(), (num_vertices, 3))
    np_rgba = np.reshape(rgba.to_numpy(), (num_vertices, 4))
    # create a PLYWriter
    writer = ti.PLYWriter(num_vertices=num_vertices)
    writer.add_vertex_pos(np_pos[:, 0], np_pos[:, 1], np_pos[:, 2])
    writer.add_vertex_rgba(np_rgba[:, 0], np_rgba[:, 1], np_rgba[:, 2], np_rgba[:, 3])
    writer.export_frame_ascii(frame, series_prefix)

# blender
# install stop-motion-obj https://github.com/neverhood311/Stop-motion-OBJ/wiki#download--install
# file-import-motionsequence
#    file-type: PLY
#    filename: example
#    material per frame
