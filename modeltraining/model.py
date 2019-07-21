### Load image dataset

import imageio
import numpy as np
import h5py
import matplotlib.pyplot as plt
import PIL
# import scipy.misc

f = h5py.File('../training_dataset.hdf5', 'r')
# console: list(f.keys())
# out: ['test_img', 'test_labels', 'train_img', 'train_labels']
dset = f['test_img']
data = np.array(dset[:,:,:])
plt.imshow(dset[1]) # change index to whatever pic to see
imageio.imwrite('test2.jpg', dset[1])