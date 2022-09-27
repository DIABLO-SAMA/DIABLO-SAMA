import os
from xml.dom.xmlbuilder import DocumentLS

files=os.listdir() #creating all giles into list

def creatIfnotExist(folder):
    if not os.path.exist(folder):
        os.makedirs(folder)

def move(folder_name,files):
    for file in files:
        os.replace(file,f"{folder_name}/{file}")

if __name__ == "__main__":
    file=os.listdir()
    flies.remove("cleaner.py")

    creatIfnotExist('images')
    creatIfnotExist('docus')
    creatIfnotExist('media')
    creatIfnotExist('others')

    imgexts=[".png",".jpg",".jpeg"]
    images=[file for files in files if os.path.splitext(file)[1].lower() in imgexts]

    docexts=[".txt",".pdf",".doc",".docx",".zip"]
    Doc=[file for files in files if os.path.splitext(file)[1].lower() in docexts]

    medexts=[".mp4",".mp3",".flv"]
    meds=[file for files in files if os.path.splitext(file)[1].lower() in medexts]
   
    others=[]
    ext=os.path.splitext(file)[1].lower()
    if(ext not in imgexts) and (exts not in docexts) and (exts not in medexts):
      others.append
    move("images",images)
    move("docus",Doc)
    move("media",meds)     




