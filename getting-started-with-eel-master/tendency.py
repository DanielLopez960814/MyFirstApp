import cv2
import os
import sys


path = '/home/daniel/Documentos/tutorialElectron/electron-quick-start/_images/plot.png'

im = cv2.imread(path)
cv2.imshow('Window',im)
cv2.waitKey(0)
cv2.destroyAllWindows()

print('Hope this tool would be usefull')
sys.stdout.flush()