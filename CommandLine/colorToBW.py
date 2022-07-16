from PIL import Image
from PIL import ImageOps

from os.path import exists
import os

from platform import uname

deleteComd ={"Windows":"del ","Linux":"rm "}            # delete cammand for different os
allowed_extentions = {"jpeg","jpg","png"}               # set of allowes extention
file_path = input("Enter file path:")                   # take path of image as input
if exists(file_path):                                   # check if path exists or not
    path_list=file_path.split('\\')                     # get file name out the path
    extention = path_list[-1].split('.')[-1]            # extract the extension out of the name
    if extention in allowed_extentions:                 # check if the extension is allowed or not
        img = Image.open(file_path)                     # open image
        img_gray = ImageOps.grayscale(img)              # convert to grayscsale
        img_gray.mode:L
        saveAs = "grayed_"+path_list[-1]
        img_gray.save(saveAs)                           # save image as graye+<name of image>.extension
        preview = Image.open(saveAs)                    # preview the gray scaled image
        preview.show()                      
        print("You want to save the image")             # ask if they want to save the image or not
        save = input("[Y]es/[N]o\n")
        if save=='Y' or save =='N':                     # check whether the option is Y or N
            if save=='N':                               # if N then delete the gray scaled image
                os.system(deleteComd[uname()[0]]+saveAs)
            else:
                print("File successfully saved")
        else:                                           # if the option is not Y or N, image will be saved as default
            print("Invalid input! Saving file....")
    else:                                               # if the extension is invalid terminate
        print("Invalid file format. Try using a jpg,jpeg or a png file.")
            

else:                                                   # if Path is invalid terminate
    print("Invalid Path entered Please try again.")
