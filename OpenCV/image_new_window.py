# open image in new window
import cv2

new_window = cv2.imread('flipped.jpg')

while True:
    cv2.imshow('puppy', new_window)
    # if we've waited at least 1 ms AND we've pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
cv2.destroyAllWindows()
