import PIL, os
from PIL import Image
from tkinter.filedialog import *


def compress_img(path):
    
    # Extracting info from path
    img_name = path.split("/")[-1]
    img_type = path.split('.')[-1]
    folder_path = path[0:-len(img_name)-1]
    
    # Create image from path & extract dimensions
    img = PIL.Image.open(path)
    myHeight,myWidth = img.size
    
    # Convert color mode to RGB
    if img_type == 'png':
      img = img.convert('RGB')

    # Resize extra large image
    short_side = min(myHeight, myWidth)
    if short_side > 1080:
      ratio = 1080/short_side
      if myHeight <= myWidth:
        myHeight = 1080
        myWidth = int(ratio*myWidth)
      else:
        myWidth = 1080
        myHeight = int(ratio*myHeight)
        
    # Compress image    
    img = img.resize((myHeight, myWidth), PIL.Image.ANTIALIAS)
    
    # Create a new path for compressed images
    if not os.path.exists(folder_path + '/compressed'):
      os.makedirs(folder_path + '/compressed')
    
    # Save image
    path = folder_path + '/compressed/' + img_name.split('.')[0] + '_c.jpg'
    img.save(path)
    
    
    
file_path = askopenfilenames()

for file in file_path:
  compress_img(file)
    