import imageio
import os

input_file = "DDIM_results/DDIM25.png"
output_dir = input_file.split(".")[0]
os.makedirs(output_dir, exist_ok=True)

images = []
subimg_border = 2 # px
subimg_res = (128, 128)

def cut_images(input_file):
    img = imageio.imread(input_file)
    rows = []
    for i in range(subimg_border, img.shape[0], subimg_res[0]+subimg_border):
        row = []
        for j in range(subimg_border, img.shape[1], subimg_res[1]+subimg_border):
            subimg = img[i:i+subimg_res[0], j:j+subimg_res[1]]
            assert subimg.shape[:2] == subimg_res
            row.append(subimg)
        rows.append(row)
    
    return rows

def save_gif(rows, output_dir):
    for i, row in enumerate(rows):
        frames = row[0:1] + row[2:] + row[-1:]
        out_path = os.path.join(output_dir, f"{i:04d}.gif")
        imageio.mimsave(out_path, frames, duration=150, loop=10000)

rows = cut_images(input_file)
save_gif(rows, output_dir)


        