#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Haccer
import cv2

img = cv2.imread('E:\老男孩\图片\1.jpg')
cv2.namedwindow('Face 窗口')
cv2.imshow('Face to Face',img)
cv2.waitKey(0)
cv2.windowAllWindows()
