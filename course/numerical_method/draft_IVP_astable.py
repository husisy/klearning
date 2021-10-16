import math
import numpy as np
import matplotlib.pyplot as plt
plt.ion()

tableau_colorblind = [x['color'] for x in plt.style.library['tableau-colorblind10']['axes.prop_cycle']]
tableau_colorblind_rgb = np.array([(int(x[1:3],16),int(x[3:5],16),int(x[5:7],16)) for x in tableau_colorblind])

def demo_taylor_astable():
    # math5311-fig3.7
    order = 8
    xspan = np.linspace(-5,5,200)
    yspan = np.linspace(-5,5,200)
    xspan = np.tile(xspan[:,np.newaxis], (1,len(yspan)))
    yspan = np.tile(yspan[np.newaxis], (xspan.shape[0],1))

    tmp0 = xspan + 1j*yspan
    ret = []
    for order_i in range(1, order+1):
        ret.append(np.abs(1+sum(tmp0**x/math.factorial(x) for x in range(1,order_i+1)))<=1)
    fig,ax = plt.subplots()
    for x,y in zip(ret[::-1],tableau_colorblind):
        ax.contourf(xspan, yspan, x, levels=1, colors=['#FFFFFF00',y+'80'])
    fig.tight_layout()
