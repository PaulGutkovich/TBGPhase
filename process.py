import numpy as np
import os
import matplotlib.pyplot as plt

in_dir = "filtered_data/"
out_dir = "processed_data/data.npz"

alphas = ["0.02","0.04","0.06","0.08","0.10","0.20","0.30","0.40","0.50"]
Us = ["1.00","2.00","3.00","4.00"]
bands = ["CB", "VB"]
components = ["Re", "Im"]
layers = [1, 2]

images = []
outputs = []
i = 0
for alpha in alphas:
	for U in Us:
		image = []
		output = [alpha, U]
		for band in bands:
			for layer in layers:
				re_filename = f"sum_{alpha}_{U}_{band}_Re_{layer}.dat"
				im_filename = f"sum_{alpha}_{U}_{band}_Im_{layer}.dat"


				# transform datas into 2d np array
				re_data = np.genfromtxt(f'{in_dir}{re_filename}',dtype=np.dtype((float,3)))[:, 2]
				re_image = np.reshape(re_data, (201, 201))
				im_data = np.genfromtxt(f'{in_dir}{im_filename}',dtype=np.dtype((float,3)))[:, 2]
				im_image = np.reshape(im_data, (201, 201))

				# gets magnitude and phase data
				magnitude = np.sqrt(re_image**2+im_image**2)
				phase = np.arctan2(im_image, re_image)

				image.append(magnitude)
				image.append(phase)

				i += 2
				print(i)


		# add images, outputs to lists
		images.append(image)
		outputs.append(output)

np.savez(out_dir, images=images, outputs=outputs)