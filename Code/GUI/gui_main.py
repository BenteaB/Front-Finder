from tkinter import *
import tkinter
import tkinter.filedialog as filedialog
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import ImageTk, Image
from tkinter import messagebox as mb
from classifier.classifier import Classifier

def filterImage(image_path, colored):
    image = mpimg.imread(image_path)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    filtered = np.zeros_like(image, np.uint8)
    if (colored == True):
        red_mask = cv2.inRange(rgb_image, (254, 50, 0), (254, 50, 0))
        blue_mask = cv2.inRange(rgb_image, (0, 50, 254), (0, 50, 254))
        purple_mask = cv2.inRange(rgb_image, (229, 50, 229), (229, 50, 229))
        imask = red_mask > 0
        filtered[imask] = image[imask]
        imask = blue_mask > 0
        filtered[imask] = image[imask]
        imask = purple_mask > 0
        filtered[imask] = image[imask]
    else:
        for x in range(rgb_image.shape[0]):
            for y in range(rgb_image.shape[1]):
                if (rgb_image[x, y] > 75).all():
                    rgb_image[x, y] = 255
        filtered = rgb_image

    filtered_img = cv2.cvtColor(filtered, cv2.COLOR_RGBA2RGB)

    if (colored == True):
        for x in range(filtered_img.shape[0]):
            for y in range(filtered_img.shape[1]):
                if (filtered_img[x, y] == 0).all():
                    filtered_img[x, y] = 255
                else:
                    filtered_img[x, y] = 0

    pil_img = Image.fromarray(filtered_img)
    return pil_img


def upload_image(colored):
    global img
    imgFile = filedialog.askopenfilename()
    if(imgFile == ""):
        mb.showerror(title = "Error", message = "You need to upload a file!")
        return
    if(".gif" not in imgFile):
        mb.showerror(title = "Error", message = "You need to upload a gif file!")
        return
    global pil_img
    pil_img = filterImage(imgFile, colored)
    img = ImageTk.PhotoImage(pil_img)
    label.configure(image=img)
    label.pack()
    

def send_image(image):
    if(image == None):
        mb.showerror(title = "Error", message = "You need to upload an image first!")
    else:
        global result_img
        result_img = Classifier().predict_image(image)
        result_img = ImageTk.PhotoImage(result_img)
        label.configure(image=result_img)
        label.pack()

def setLabelImage(image):
    img = ImageTk.PhotoImage(image)
    label.configure(image=img)
    label.pack()

root = Tk()
root.title('FrontFinder')
root.geometry("1920x1080+10+20")

label = tkinter.Label(root, text="upload image", width=30)

global img
global pil_img
pil_img = None
global result_img
result_img = None

menu = Menu(root)
upload_menu = Menu(menu, tearoff=0)
upload_menu.add_command(label="Colored", command=lambda: upload_image(True))
upload_menu.add_command(label="Black & White", command=lambda: upload_image(False))
menu.add_cascade(label="Upload", menu=upload_menu)
menu.add_command(label="Analyze", command=lambda: send_image(pil_img))

root.config(menu=menu)

fr = Frame(root)
fr.pack(expand=1, fill=BOTH)
fr.place(anchor='center', relx=0.5, rely=0.5)
label = Label(fr)

root.mainloop()
