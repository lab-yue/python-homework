import cv2
import os


def detect_cat(sample):
    img = cv2.imread(f'./sample/{sample}')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    catCascade = cv2.CascadeClassifier("./cat_cascade.xml")
    faces = catCascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=2, minSize=(180, 180))
    for (x, y, w, h) in faces:
        img = cv2.rectangle(
            img,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3
        )
    # sift
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints = sift.detect(gray, None)

    img = cv2.drawKeypoints(img, keypoints, None)
    cv2.imwrite(f'./out/{sample}', img)
    print(sample, 'DONE')


if __name__ == '__main__':

    for sample in os.listdir('./sample'):
        try:
            detect_cat(sample)
        except:
            print(f'fall to process {sample}')
