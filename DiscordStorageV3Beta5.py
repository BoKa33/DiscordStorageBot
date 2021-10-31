import asyncio, requests, time, os, discord, shutil, sys; from fsplit.filesplit import Filesplit;


fs = Filesplit()
TOKEN = None
Savechannel = None
FilesUploaded = 0
Filecount = 0

def setTokenAndId(Token,ID):
    global TOKEN
    TOKEN = Token
    global Savechannel
    Savechannel = ID
def println():
    print();print("*************************************************");print()
    
def getall():
    with open('savefile.boka','r') as savefile:
        Identifiers = []
        for line in savefile.readlines():
            Identifiers.append(line.split("#")[0].strip())
    return(Identifiers)

def split_cb(f, s):
    sys.stdout.write('\n'+"Currently splitting part "+ f.split("_")[1].split(".")[0] +" from " + str(Filecount))

def splitFiles(FileSrc):
    filesize = os.path.getsize(FileSrc)
    println()
    print("The file will be cutted in to pieces of 7MB now... WOAHRRRM... \nthis will be about "+str(round(filesize/7_000_000)+1)+" parts at the end");
    print()
    
    
    fs.split(file = FileSrc,output_dir = "temp/",split_size=7000000,callback=split_cb)
    
    print("\nFinished zipping" + 100*" ")
    println()
    
def checkIdenNotInUse(Identifier):
    if Identifier in getall():
        raise Exception("Identifier is already in use")

def clearTemp():
    try:
        shutil.rmtree("temp");os.mkdir("temp")
    except Exception as e:
        print(e)

def uploadFiles(Files,Token):

    
    
    if len(Files) > 4000:
        raise Exception("Too much files");
    
    async def upload(Files):
        global FilesUploaded
        Urls = []
        await client.wait_until_ready()
        try:
            for file in Files:
                message = await client.get_channel(Savechannel).send(file=discord.File(file, file)); sys.stdout.write("\n"+"Uploaded file " + str(FilesUploaded+1) + " from " + str(Filecount+1))
                Urls.append(message.attachments[0].url)
                FilesUploaded += 1
            await client.close(); asyncio.set_event_loop(asyncio.new_event_loop());
            return Urls
        except Exception as e:
            print(e)
            print("Error occured, repeating last task")
            await client.close(); asyncio.set_event_loop(asyncio.new_event_loop());
            return None
    client = discord.Client()
    task = client.loop.create_task(upload(Files))
    client.run(Token)
    if task.result() == None:
        time.sleep(10)
        return uploadFiles(Files,Token)
    for file in Files:
        os.remove(file)
    return task.result()
    
        
def upload(Identifier, FileSrc):
    
    checkIdenNotInUse(Identifier)
    clearTemp()

    global Filecount
    global FilesUploaded
    Filecount = round(os.path.getsize(FileSrc)/7_000_000)+1
    
    splitFiles(FileSrc)
    
    print("Uploading files:");print()
    
    svf = next(os.walk("temp"), (None, None, []))[2]

    Parts = []; 

    for file in svf:

        Parts.append(r"temp/"+str(file))

    PiecesPerStack = 400
        
    Stacks=[Parts[i:i + PiecesPerStack] for i in range(0, len(Parts), PiecesPerStack)]

    TotalUrls = []

    for Stack in Stacks:

        def a():

            try:
                asyncio.set_event_loop(asyncio.new_event_loop());
                return uploadFiles(Stack,TOKEN)

            except Exception as e:

                print(e)
                    
                return a()

        TotalUrls.extend(a())
        
    print("\n"+"Uploaded files sucessfully"+100*" ")

    clearTemp()
    
    with open('savefile.boka','a') as savefile:
        savefile.write("\n"+Identifier+"#"+str(TotalUrls))
    println();print("Upload ready");
    FilesUploaded = 0
    Filecount = 0
    
def merge_cb(f, s):
    pass;
    
def download(Identifier, FileSrc):
    clearTemp()
    with open('savefile.boka',"r") as savefile:
        for line in savefile:
            lineparts = line.split("#")
            if lineparts[0] == Identifier:
                try:
                    urls = eval(lineparts[1])
                    counter = 0
                    for url in urls:
                        counter += 1
                        print("Downloading part "+str(counter)+" from "+str(len(urls)))
                        file = requests.get(url,stream = True, allow_redirects=True).raw
                        if url.split("/")[6].split("_")[2] != "manifest.csv":
                            with open("temp/"+ Identifier.split(".")[0] +"_"+url.split("/")[6].split("_")[2], 'wb') as savehere:
                                shutil.copyfileobj(file, savehere)
                        else:
                            with open("temp/fs_manifest.csv", 'wb') as savehere:
                                shutil.copyfileobj(file, savehere)
                except Exception as e:
                    print(e)
    fs.merge(input_dir = "temp/",cleanup = True, callback=merge_cb)
    shutil.move("temp/"+Identifier,Identifier)
    println();print("Download ready");println();
    
def delete(Identifier):
    try:
        os.remove("tempsave.boka")
    except:
        pass
    if not Identifier in getall():
        raise Exception("Identifier not found")
    with open('savefile.boka',"r") as savefile:
        with open("tempsave.boka","a") as tmp:
            for line in savefile:
                if not line.split("#")[0] == Identifier:
                    tmp.write(line)
    with open("savefile.boka","w+") as savefile:
        with open("tempsave.boka","r") as tmp:
            savefile.write(tmp.read())
    os.remove("tempsave.boka")
    
def overwrite(Identifier, FileSrc):
    if Identifier in getall():
        delete(Identifier)
    upload(Identifier, FileSrc)
    
def rename(Identifier, NewIdentifier):
    if NewIdentifier in getall():
        raise Exception("The identifier you want to use as new name is already in use")
    try:
        os.remove("tempsave.boka")
    except:
        pass
    if not Identifier in getall():
        raise Exception("Identifier not found")
    with open('savefile.boka',"r") as savefile:
        with open("tempsave.boka","a") as tmp:
            for line in savefile:
                if not line.split("#")[0] == Identifier:
                    tmp.write(line)
                else:
                    tmp.write(NewIdentifier + "#" + line.split("#")[1])
    with open("savefile.boka","w+") as savefile:
        with open("tempsave.boka","r") as tmp:
            savefile.write(tmp.read())
    os.remove("tempsave.boka")
