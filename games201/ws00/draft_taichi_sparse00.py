import taichi as ti

ti.init(arch=ti.cuda)

n = 512
x = ti.field(dtype=ti.i32)
res = n + n // 4 + n // 16 + n // 64
img = ti.field(dtype=ti.f32, shape=(res, res))

block1 = ti.root.pointer(ti.ij, n // 64)
block2 = block1.pointer(ti.ij, 4)
block3 = block2.pointer(ti.ij, 4)
block3.dense(ti.ij, 4).place(x)

@ti.kernel
def activate(t: ti.f32):
    tmp0 = ti.Matrix.rotation2d(ti.sin(t))
    for i, j in ti.ndrange(n, n):
        p = ti.Vector([i, j]) / n
        p = tmp0 @ (p - 0.5) + 0.5
        if ti.taichi_logo(p) == 0:
            x[i, j] = 1

@ti.func
def scatter(i):
    return i + i // 4 + i // 16 + i // 64 + 2

@ti.kernel
def paint():
    for i, j in ti.ndrange(n, n):
        t = x[i, j]
        t += ti.is_active(block1, ti.rescale_index(x, block1, [i, j]))
        t += ti.is_active(block2, ti.rescale_index(x, block2, [i, j]))
        t += ti.is_active(block3, ti.rescale_index(x, block3, [i, j]))
        img[scatter(i), scatter(j)] = 1 - t / 4

img.fill(0.05)
gui = ti.GUI('Sparse Grids', (res, res))
i = 0
while gui.running:
    block1.deactivate_all()
    activate(i * 0.05)
    paint()
    gui.set_image(img)
    gui.show()
    i += 1
