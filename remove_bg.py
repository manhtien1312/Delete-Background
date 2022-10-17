import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation

segmentor = SelfiSegmentation()

# chèn file ảnh vào bằng đường dẫn 
imgOffice = cv2.imread('D:\\python\\background-removal-project\\test_images\\test11.png')

# màu nền 
white = (0, 0, 0)

# xóa nền cũ
imgNoBg = segmentor.removeBG(imgOffice, white, threshold=0.25)

# ghi ảnh đã xóa nền ra file mới
cv2.imwrite("D:\\python\\background-removal-project\\removed_bg_images\\result11.png", imgNoBg)

