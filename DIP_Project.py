# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 14:13:16 2021

@author: dell
"""

import cv2
import pyautogui
import numpy as np

vid = cv2.VideoCapture(0)
previous_pose ="neutral"

while(1):
       _,frame = vid.read()
       frame = cv2.flip(frame,1)
       frame = frame[:300,300:600]
       frame = cv2.GaussianBlur(frame,(5,5),0)
       lower_skin = np.array([13,16,25])
       upper_skin = np.array([125,100,125])
       super_1 = cv2.inRange(frame,lower_skin,upper_skin)
       _,thresh= cv2.threshold(super_1,127,255,cv2.THRESH_BINARY)
       contours , hierachy =cv2.findContours(thresh , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
       if len(contours) == 0:
           continue
       
       max_contour = max(contours, key=cv2.contourArea)
        
       M =cv2.moments(max_contour)
       try:
            x= int(M['m10']/M['m00'])
            y= int(M['m01']/M['m00'])
       except ZeroDivisionError:
            continue
       frame = cv2.circle(frame, (x,y),10,(255,0,0),2)
       frame = cv2.drawContours(frame,max_contour, -1, (0,0,0),3)
        
       frame = cv2.line(frame,(75,0) , (75,299) , (255,255,255) ,2)
       frame = cv2.line(frame,(225,0) , (225,299) , (255,255,255),2)
       frame = cv2.line(frame,(75,200) , (225,200) , (255,255,255),2)
       frame = cv2.line(frame,(75,250) , (225,250) , (255,255,255),2)
        
       cv2.imshow('SAM',frame)
        
       if x<75:
            current_pose ="left" 
       elif  x>225:
            current_pose ="right"
       elif x>75  and x<225 and y>250:
            current_pose ="down"
       elif x>75 and x<225 and y<200:
            current_pose="up"
       elif x>75 and x<225 and y<250 and y>200:
            previous_pose ="neutral"
         
       if current_pose !=previous_pose:
            if current_pose!="neutral":
              pyautogui.press(current_pose)
            previous_pose = current_pose 
       if  cv2.waitKey(1) == ord('q'):
            break
vid.release()
cv2.destroyAllWindow()        
       
       