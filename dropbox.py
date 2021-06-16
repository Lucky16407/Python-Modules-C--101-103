import cv2
import dropbox
import time
import random

start_time = time.time()
def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        image_name = "Picture" + str (number) + ".png"
        cv2.imwrite(image_name,frame)
        start_time = time.time
        result = False
    return image_name
    print ("Snapshot taken, have a nice day! :D")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token = "sl.AvtQI62p5-t0kLP7GdjNDI4eedkKIQEexLvqH_iDPgjvfLtud7fBQfJn4RIJjLEWaoRzMupYADH6gjeyVkEhxbrfvEWeVQaLrMnjzcvMAr_hBFi0ZEEkIAFSBexrXRHculX0Fyg"
    file = img_counter
    file_from = file 
    file_to = "/newfolder/"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("Alright, we have uploaded your file! :D")

def main():
    while(True):
        if((time.time()-start_time)>= 300):
            name = take_snapshot()
            upload_file( name )

main()
