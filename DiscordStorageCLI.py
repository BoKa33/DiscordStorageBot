from StorageAPI import *

line = ("\033[92m*\033[0m"*60)

# --- Beginning ---

welcome = "Welcome to the \033[92mDiscordStorage\033[0m commandLineInterface"


# --- General ---

usage = "Type \033[92mu\033[0m for \033[1muploading\033[0m a file, \033[92md\033[0m for \033[1mdownloading\033[0m a file, \033[92mr\033[0m for \033[1mremoving\033[0m a file, \nor type \033[92ml\033[0m to get a \033[1mlist\033[0m of all your uploaded files: \033[92m"



# --- Processing ---

# First Prompt after each command

uploading = "Copy the file u want to upload into the folder from this script... \nPress \033[92menter\033[0m if u are ready: \033[92m"

downloading = "Make sure that there is twice as much free space as u want to download on this disk. \n \n\033[92mType\033[0m in, the \033[92mfilename\033[0m of the file you want to download: \033[92m"

removing = "\033[92mEnter\033[0m the \033[92mfilename\033[0m of the file you want to get rid of: \033[92m"

listing = "Here is a list of all your uploaded stuff!"

# Following Prompts

uploadingY = "Now \033[92menter\033[0m the \033[92mfilename\033[0m of the file you want to upload, \nthis will be the filename under that u'll find the file later on. \nIf you want to use another name for it just rename it now, in this case enter the new filename here: \033[92m"

downloading2 = "Thanks, this will take a moment. \nPlease \033[92mdon't power\033[0m your \033[92mcomputer off\033[0m or close this until its ready, else this download will cancel and u need to restart it. \nU can \033[92mcontinue working in other programms\033[92m and will be able see the progress below this."

removingConfirm = "Are you sure u want to delete \033[1m'{0}'\033[0m ? \033[92mType y or n\033[0m if you got cold feet: \033[92m"

# Even more Prompts...

uploading3 = "Thanks, this will take a moment (about \033[1m15\033[0m minutes per GB). \nPlease \033[92mdont power\033[0m your \033[92mcomputer off or close\033[0m this until its ready, else this download will cancel and u need to restart it. \nU are be able see the progress below this. "

downloadingR = "Is there another job left?"

removingR = "File was succesfully removed!"

# ...

uploadingR = "Shall we download the file for you, to make sure its intact? Then remove the original file from the folder, and enter y, else \033[92mjust press Enter: "

#...

checkR = "CheckDownload is ready, you can check if the file is working now... Is there another job left?"

# --- Errors ---

uploadE = "Oops, there is something waiting to be fixed... \nMake sure that there is not a file with the same mame already uploaded,\n and that the token and channel id in StorageAPI.py is valid. \nDid you we ran out of storage? \nOr maybe theres an error because you are not connected to the internet, \naka. theres a firewall filtering Discord? \nIs there a 'savefile.boka' in this folder? If not create one. \nThen try again! "

downloadE = "Oops, there is something waiting to be fixed... \nDoes The file exists? did you ran out of storage? \nMaybe theres an error because you are not connected to the internet, \naka. theres a firewall filtering Discord?. \n \nTry again!"

removeE = "Oops, there is something waiting to be fixed... \nDoes The file exists?"

listE = "Oops, there is something waiting to be fixed... Is there a Savefile.boka inside this folder?"

def Println():
    print(line)
def Printline():
    print();Println();print()
def Welcome():
    Println();print();print(welcome);print();Println();print();Usage()

def Usage():
    operation = input(usage)
    
    Printline();
    
    if operation == "u":
        Oupload()
        
    elif operation == "d":
        Odownload()
        
    elif operation == "r":
        Oremove()
        
    elif operation == "l":
        Olist()
    Printline()
    Usage()
        
    
def Oupload():
    _ = input(uploading)
    Printline()
    file = input(uploadingY)
    Printline()
    print(uploading3)
    try:
        upload(file);
        Printline()
        check = input(uploadingR)
        Printline()
        if check == "y":
            print(downloading2)
            Printline()
            download(file)
            Printline()
            print(checkR)
        else:
            print(downloadingR)
    except Exception as e:
            Printline();print(e);Printline();print(uploadE)
    
def Odownload():
    file = input(downloading)
    Printline()
    print(downloading2)
    Printline()
    try:
        download(file)
        Printline()
        print(downloadingR)
    except Exception as e:
            Printline();print(e);Printline();print(uploadE)

def Oremove():
    file = input(removing)
    Printline()
    if input(removingConfirm.format(file)) == "y":
        try:
            delete(file)
            Printline()
            print(removingR)
        except Exception as e:
            Printline();print(e);Printline();print(removeE)
        
        
def Olist():
    print(listing)
    Printline()
    try:
        print(getall())
    except Exception as e:
            Printline();print(e);Printline();print(listE)
            
Welcome()
