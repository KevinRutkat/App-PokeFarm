import tkinter as tk
from tkinter import ttk
import threading
import time
import queue

# Importación de librerías para la automatización
import pygetwindow as gw
import keyboard
import cv2
import numpy as np
import mss
import pytesseract
import pyautogui

MovimientoW = "W"
MovimientoA = "A"
MovimientoS = "S"
MovimientoD = "D"
inputHablar = "Z"
botonVuelo  = "9"
botonBici   = "1"
botonCaña   = "5"

time.sleep(1)
pyautogui.leftClick()
time.sleep(1)
time.sleep(0.2)
keyboard.press(MovimientoW)
time.sleep(4.5)
keyboard.release(MovimientoW)
time.sleep(0.2)
keyboard.press(inputHablar)
time.sleep(10)
keyboard.release(inputHablar)
time.sleep(0.2)
keyboard.press(MovimientoS)
time.sleep(3.5)
keyboard.release(MovimientoS)
