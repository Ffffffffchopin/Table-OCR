import cv2
import numpy as np
ENLARGE=3
window_name="Image"
raw=cv2.imread(r"C:\Users\F.F.Chopin\Pictures\Screenshot_20220919_222336.jpg",1)
height,width=raw.shape[:2]
res=cv2.resize(raw,(width//ENLARGE,height//ENLARGE),interpolation=cv2.INTER_CUBIC)
#print(type(raw))
gray=cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)

binary=cv2.adaptiveThreshold(~gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,35,-5)


row,col=binary.shape
scale=20
kernel_row=cv2.getStructuringElement(cv2.MORPH_RECT,(col//scale,1))
eroded_row=cv2.erode(binary,kernel_row,iterations=1)
dilater_row=cv2.dilate(eroded_row,kernel_row,iterations=1)

kernel_col=cv2.getStructuringElement(cv2.MORPH_RECT,(1,row//scale))
eroded_col=cv2.erode(binary,kernel_col,iterations=1)
dilater_col=cv2.dilate(eroded_col,kernel_col,iterations=1)

#ss_row=np.hstack((dilater_row,binary))
ss_col=np.hstack((dilater_col,binary))
#ss=np.hstack((binary,cv2.add(dilater_col,dilater_row)))
#cv2.imshow(window_name,np.hstack((eroded_row,dilater_row)))

bitwise_and=cv2.bitwise_and(dilater_col,dilater_row)
#cv2.imshow("bitwise",bitwise_and)

add=cv2.add(dilater_col,dilater_row)
#cv2.imshow("add",add)

subtract=cv2.subtract(binary,add)
#cv2.imshow("subtract",subtract)

new_kenerl=cv2.getStructuringElement(cv2.MORPH_RECT,(2,2))
erode_image=cv2.morphologyEx(subtract,cv2.MORPH_OPEN,new_kenerl)
#cv2.imshow("new_kenerl",new_kenerl)

merge=cv2.add(erode_image,bitwise_and)
cv2.imshow("merge",merge)
cv2.imshow("原图",binary)
cv2.waitKey()

#import cv2


