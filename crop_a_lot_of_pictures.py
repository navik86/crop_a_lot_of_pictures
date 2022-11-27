import os
from PIL import Image


path = "your_folder_with_pictures"
file_list = os.listdir(path)
full_list = [os.path.join(path, i) for i in file_list]
time_sorted_list = sorted(full_list, key = os.path.getmtime)

 
def crop_center(pil_img, crop_width: int, crop_height: int) -> Image:
    """
    Функция для обрезки изображения по центру.
    """
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

i = 1

for j in time_sorted_list:
    im = Image.open(j)
    im_new = crop_center(im, 1100, 870)
    im_new.save(f'your_other_folder_for_save/{i}.png', quality=100)
    i += 1
