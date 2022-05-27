import cv2
import imutils
fotograf = cv2.imread('yaya9.jpg')
fotograf = imutils.resize(fotograf, width=min(500, fotograf.shape[1]))

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

(insanlar, _) = hog.detectMultiScale(fotograf, winStride=(5, 5), padding=(3, 3), scale=1.21)

for (x, y, w, h) in insanlar:
    cv2.rectangle(fotograf, (x, y),
                  (x + w, y + h),
                  (0, 255, 0), 2)

print('Belirlenen İnsan Sayısı : ', len(insanlar))

cv2.imshow("Fotograf", fotograf)
cv2.waitKey(0)

cv2.destroyAllWindows()

