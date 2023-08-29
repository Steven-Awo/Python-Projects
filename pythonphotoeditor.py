from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './samples'
pathOut = '/editedsample'

for file_name in os.listdir(path):
    img = Image.open('{}/{}'.format(path ,file_name))
    
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
    # factor = 1.5
    # enhancer =
    
    clean_name = os.path.splitext(file_name)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')