from rembg import remove
from PIL import Image

image = Image.open("car.png")
output = remove(image)
output.save("output.png")