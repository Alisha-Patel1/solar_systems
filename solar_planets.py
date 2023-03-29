import cv2
img = cv2.imread("solar-system.jpg")
cv2.putText(img, 
            "Sun",
            (20, 300),
            cv2.FONT_HERSHEY_COMPLEX,
            1, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Mercury",
            (100, 200),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Venus",
            (180, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Earth",
            (270, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Mars",
            (370, 180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Jupiter",
            (480, 60),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Saturn",
            (770, 120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Uranus",
            (940, 130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.putText(img, 
            "Neptune",
            (1100, 150),
            cv2.FONT_HERSHEY_COMPLEX,
            0.6, 
            (255, 255, 255)
            )
cv2.imshow("Solar Output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)
