import dropbox,time,os
from dropbox.files import WriteMode 

StartTime = time.time()

fileSource = input("Enter File Path : ")

def upload(fileSource) :
    access_token = "AM9FI4pN-MoAAAAAAAAAARONzJAz1fDZ1kz1MTbClpItVrYuO6296MfZzINTSblB"
    fileTo = "/AutoSave/"
    for root,dir,files in os.walk(fileSource) :
           for i in files :
               localpath = os.path.join(root,i)
               rlpath = os.path.relpath(localpath,fileSource)
               dbpath = os.path.join(fileTo,rlpath)        
               with open(localpath,"rb")as f :
                   dropbox.Dropbox(access_token).files_upload(f.read(),dbpath,mode = WriteMode('overwrite'))
    

    print("File Uploaded")

def main() :
    while True :
        if ((time.time()-StartTime)>=300) :
            upload(fileSource)

main()

