import imageio
import glob
import os

for path in ["assembly", "basketball", "door-open", "hammer", "shelf-place"]:
    files = sorted(glob.glob(os.path.join(path, "subgoal_vis", "*.png")))
    ### save as gif with infinite loop
    imageio.mimsave(os.path.join(path, "subgoal_vis.mp4"), [imageio.imread(f) for f in files], fps=2)