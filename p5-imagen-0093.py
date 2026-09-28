import cv2
img = cv2.imread('GTR-NISSAN-0093.jpg')
#Determinar el ripo de imagen "numpy.ndarray."
print(type(img))
#mostrar pixeles (415, 739, 3)   
print(img.shape)
#Mostrando Imagen en ventana
cv2.imshow('GTR-NISSAN', img)
#Tiempo de espacio
cv2.waitKey(0)
#destruir todas las ventanas
cv2.destroyAllWindows()
