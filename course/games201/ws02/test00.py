import taichi as ti
import numpy as np

hfe = lambda x,y,eps=1e-5: np.max(np.abs(x-y)/(np.abs(x)+np.abs(y)+eps))

# ti.init(arch=ti.opengl)
ti.init(arch=ti.cuda)


RESOLUTION = 600
ti_vector2 = ti.Vector(2, dt=ti.f32, shape=(RESOLUTION, RESOLUTION))
ti_vector3_0 = ti.Vector(3, dt=ti.f32, shape=(RESOLUTION, RESOLUTION))
ti_vector3_1 = ti.Vector(3, dt=ti.f32, shape=(RESOLUTION, RESOLUTION))


@ti.func
def clip_index(array2d, ind0, ind1):
    N0,N1 = array2d.shape
    ret = array2d[max(0, min(ind0, N0-1)), max(0, min(ind1, N1-1))]
    return ret


@ti.func
def bilinear_interp(vf, s, t):
    iu, iv = int(s), int(t)
    fu, fv = s - iu, t - iv
    a = clip_index(vf, iu, iv)
    b = clip_index(vf, iu+1, iv)
    c = clip_index(vf, iu, iv+1)
    d = clip_index(vf, iu+1, iv+1)
    tmp0 = a + fu*(b-a)
    tmp1 = c + fu*(d-c)
    ret = tmp0 + fv*(tmp1-tmp0)
    return ret


@ti.kernel
def advect(vf:ti.template(), qf:ti.template(), new_qf:ti.template(), dt:ti.f32):
    for i, j in vf:
        tmp0 = i - dt*vf[i,j][0]
        tmp1 = j - dt*vf[i,j][1]
        new_qf[i, j] = bilinear_interp(qf, tmp0, tmp1)


def np_advect(vf, qf, dt):
    '''
    vf(np,float,(N0,N1,2))
    qf(np,float,(N0,N1,N2))
    dt(float)
    (ret)(np,float,(N0,N1,N2))
    '''
    dtype = vf.dtype
    N0,N1,_ = vf.shape
    s = np.arange(N0, dtype=dtype)[:,np.newaxis] - dt*vf[:,:,0]
    t = np.arange(N1, dtype=dtype) - dt*vf[:,:,1]
    fu,iu = np.modf(s)
    iu = iu.astype(np.int32)
    fv,iv = np.modf(t)
    iv = iv.astype(np.int32)
    ind0 = np.clip(iu, 0, N0-1)
    ind1 = np.clip(iu+1, 0, N0-1)
    ind2 = np.clip(iv, 0, N1-1)
    ind3 = np.clip(iv+1, 0, N1-1)
    a = qf[ind0, ind2]
    b = qf[ind1, ind2]
    c = qf[ind0, ind3]
    d = qf[ind1, ind3]
    tmp0 = a + fu[:,:,np.newaxis]*(b-a)
    tmp1 = c + fu[:,:,np.newaxis]*(d-c)
    ret = tmp0 + fv[:,:,np.newaxis]*(tmp1-tmp0)
    return ret


def test_advect():
    dt = 0.03
    np0 = np.random.rand(RESOLUTION, RESOLUTION, 2).astype(np.float32)
    np1 = np.random.rand(RESOLUTION, RESOLUTION, 3).astype(np.float32)
    ti_vector2.from_numpy(np0)
    ti_vector3_0.from_numpy(np1)
    np2 = np_advect(np0, np1, dt)
    advect(ti_vector2, ti_vector3_0, ti_vector3_1, dt)
    ret_ = ti_vector3_1.to_numpy()
    assert hfe(ret_, np2) < 1e-3
