from PIL import Image, ImageEnhance, ImageFilter
import os 

path = './Python-Projects/samples'
pathOut = '/Python-Projects/editedsample2'

for file_name in os.listdir(path):
    img = Image.open('{}/{}'.format(path ,file_name))
    
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(file_name)[0]
    
    edit.save(f'.{pathOut}/{clean_name}_edited.jpg')