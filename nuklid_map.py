import numpy as np
import Weizsaecker as WS
import matplotlib.pyplot as plt




z_bins = np.array(range(1,201))
n_bins = np.array(range(1,201))

z_n_map = np.meshgrid(n_bins, z_bins)


print(z_n_map)

def ws_eval(Z,N):
    return WS.Weizsaecker(Z,N).evaluate()

ws_map = np.vectorize(ws_eval)

z_n_map_eval = ws_map(z_n_map[0],z_n_map[1])


print(z_n_map_eval)


plt.switch_backend("agg")
plt.rc("text",usetex=True)

fig, ax = plt.subplots()

ax.set_title("nuklid map")
ax.set_xlabel("N")
ax.set_ylabel("Z")

levels = np.linspace(0.,np.max(z_n_map_eval),5000)
plt_cont = ax.contour(n_bins, z_bins, z_n_map_eval.T, levels=levels, cmap = "rainbow")
z_bar = fig.colorbar(plt_cont, format="%.2f")
z_bar.set_label("$E_{B}/A$ [MeV]")
plt.savefig('nuklid_map.pdf')
