from re import L
from PIL import Image
from PIL import ImageOps
file_path = input("Enter file path:")
img = Image.open(file_path)
path_list=file_path.split('\\')
print(path_list[-1])
img_gray = ImageOps.grayscale(img)
img_gray.mode:L
saveAs = "grayed_"+path_list[-1]
img_gray.save(saveAs)
preview = Image.open(saveAs)
preview.show()