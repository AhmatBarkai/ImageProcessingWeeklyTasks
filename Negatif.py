
import cv2
import matplotlib.pyplot as plt
import numpy as np
def negatePhoto(photo):
    L=np.max(photo)
    negatif_foto=L-photo
    return negatif_foto

photo = cv2.imread("./imag_processing/myimage.jpg",0)
negatif_foto= negatePhoto(photo)
yan_yana = np.hstack((photo, negatif_foto))
print("original foto:",photo.shape)
print("negatif foto:",negatif_foto.shape)
print("yan yana:", yan_yana.shape)

plt.imshow(yan_yana,cmap="gray")
plt.show()