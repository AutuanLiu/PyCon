from PIL import Image
import numpy as np 

im = np.array(Image.open("E:\MyVideo\img\动物世界.png"))
print(im.shape, im.dtype)
b = [255, 255, 255, 255] - im
im1 = Image.fromarray(b.astype("uint8"))
im1.save("E:\MyVideo\img\change.jpg")