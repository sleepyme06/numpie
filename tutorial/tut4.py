import numpy as np
import matplotlib.pyplot as plt
import os

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.random.rand(3, 3)
array3 = np.zeros((4, 4))

#save to flat files
np.save("array1.npy",array1)

loaded_array=np.load('array1.npy')
print(loaded_array)

logo_path = 'tutorial/numpy-logo.npy'
if os.path.exists(logo_path):
	logo = np.load(logo_path)
	dark=1-logo
	plt.imshow(logo)
	plt.show()
	plt.imshow(dark)
	plt.show()
else:
	print(f"File '{logo_path}' not found. Please check the path and ensure the file exists.")
