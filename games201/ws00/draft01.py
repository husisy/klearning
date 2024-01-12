# https://forum.taichi.graphics/t/homework-0-discrete-fourier-transform/493
# Follow https://homepages.inf.ed.ac.uk/rbf/HIPR2/fourier.htm
import math
import PIL.Image
import numpy as np
import taichi as ti
import skimage #only for test image

ti.init(arch=ti.gpu)

size = 512


pixels = ti.field(ti.f32, shape=(size, size))
results = ti.field(ti.f32, shape=(size, size))

@ti.kernel
def fourier():
    for k, l in results:
        v = ti.Vector([0.0, 0.0])
        for i in range(size):
            for j in range(size):
                center = size // 2
                kk = (k + center) % size
                ll = (l + center) % size
                angle = -2.0 * math.pi * (kk * i + ll * j) / float(size)
                p = ti.Vector([ti.cos(angle), ti.sin(angle)])
                v += pixels[i, j] * p
        center = size // 2
        results[k, l] = ti.log(1.0 + v.norm())


image = PIL.Image.fromarray(skimage.data.astronaut())
pixels.from_numpy(np.asarray(image.convert('L').resize([size, size]), dtype=np.float32)/255)

fourier()
data = results.to_numpy()
data = (data * (255/data.max())).astype(np.uint8)
PIL.Image.fromarray(data, 'L').show()
