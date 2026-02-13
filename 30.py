import cv2

face = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

img = cv2.imread("1.png")

if img is None:
    print("Image not found")

else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        smiles = smile.detectMultiScale(roi_gray, 1.7, 20)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 255, 0), 2)

    cv2.imshow("Result", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
