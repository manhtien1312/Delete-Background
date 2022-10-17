from PIL import Image 
from PIL import ImageFilter


def erode(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MinFilter(3))
    return image


def dilate(cycles, image):
    for _ in range(cycles):
        image = image.filter(ImageFilter.MaxFilter(3))
    return image


#xử lý ảnh đã xóa phông
filename = "D:\\python\\background-removal-project\\removed_bg_images\\result11.png"

with Image.open(filename) as img:
    img.load()

img_gray = img.convert("L")
#img_gray.show()

threshold = 0.5
img_threshold = img_gray.point(lambda x: 255 if x > threshold else 0)
img_threshold = img_threshold.convert("1")
# img_threshold.show()

step_1 = erode(12, img_threshold)
# step_1.show()

step_2 = dilate(58, step_1)
# step_2.show()

mask = erode(45, step_2)
# mask.show()

mask = mask.convert("L")
mask = mask.filter(ImageFilter.BoxBlur(20))
# mask.show()

blank = img.point(lambda _: 0)
img_segmented = Image.composite(img, blank, mask)
# img_segmented.show()


#chọn phông mới 
filename_bg = "D:\\python\\background-removal-project\\bg_images\\bg_image4.png"

with Image.open(filename_bg) as img_bg:
    img_bg.load()

img_bg.resize()

#ghép phông 
img_bg.paste(img.resize((img.width //5, img.height //5)), 
             (235, 70), 
             mask.resize((mask.width // 5, mask.height // 5)))
img_bg.save("D:\\python\\background-removal-project\\merged_imges\\result11.png")


