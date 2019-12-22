import cv2
import os
from multiprocessing import Pool

def detect_cat(sample):
    try:
        print('START', sample)
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
        print('DONE', sample)
    except:
        print(f'fail to process {sample}')


def main():
    samples = os.listdir('./sample')
    pool = Pool(4)
    pool.map(detect_cat, samples)

if __name__ == '__main__':
    main()
