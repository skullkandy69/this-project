import dropbox
class Transferdata :
    def __init__(self , access_token):
        self.access_token = access_token
    def upload_file (self,file_from , file_to ):
        dbx = dropbox.Dropbox(self.access_token)
        f= open(file_from , "rb")
        dbx.files_upload (f.read(), file_to)
def main():
    access_token = "8ccY-pSFy_EAAAAAAAAAAQNO2LDxACuMFT4E14ejbxAB5_rPsVYQrPn2nAOdQ5lD"
    transferdata = Transferdata(access_token)
    file_from = input("enter the file to transfer")
    file_to = input("enter the path to upload isamplr.txtsamplr.txtnto the dropbox")
    transferdata.upload_file (file_from ,file_to)
    print ("file has been uploaded")

if __name__ == "__main__" :
    main()
