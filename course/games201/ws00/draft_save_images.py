import os
import taichi as ti

hf_file = lambda *x: os.path.join('tbd00', *x)
if not os.path.exists(hf_file()):
    os.makedirs(hf_file())

ti.init(arch=ti.cpu)

pixels = ti.field(ti.u8, shape=(512, 512, 3))

@ti.kernel
def set_pixels():
    for i, j, k in pixels:
        pixels[i, j, k] = ti.random(ti.float32)*255

set_pixels()
ti.imwrite(pixels.to_numpy(), hf_file('tbd00.png'))
