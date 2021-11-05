_______________________________________________

### **Discord Storage** _V.3.5_ (Beta)

**Made by *BoKa***

*Enjoy Discords free and unlimited storage...*

_______________________________________________	


# Usage

## Prepare

Clone this from Github,
make sure there is a folder called temp and a file called savefile.boka in the cloned folder.
If not create those (empty).

You need the following [PIP](https://pypi.org/project/pip/) packages:

##### Discord:

	sudo pip install discord

##### Filesplit:

	sudo pip install filesplit

You will need a Discord "servers" token too. This may help you:

Download Discord and generate one

	sudo pamac install snapd

	sudo snap install discord --classic

an API key for this server is required:

[Here](https://www.youtube.com/watch?v=gT_1c9YFffk) is how to create one.

Open DiscordStorageV3Beta5.py and paste the bot token between `TOKEN = "` and `"` in line 5.



## Use it as CLI 

Execute StorageCLI.sh in Linux console.

or execute StorageCLI.py in cmd with using python.



## Use it as API

	import StorageAPI.py

### Upload: 

	upload(FileName)

 Uploads a file. If you have already uploaded another file with the same name it will throw an exception,
 so make sure that the name of the file you want to upload was not used before or use the Overwrite method. 
 If you want to check which filenames are already in use look at getall() filename defines two things:
 The file u want to upload, and its the string u have to use in the download method to get your file back.

### Download:

	download(FileName)

 Downloads a file. If the file doesn't exists it will throw an exception. Paste in the filename u have used in the upload function,
 and the requested file will apear in the folder where this file is probably in.

### Get all filenames:

	getall()

 Returns all the filenames from the savefile. 

### Delete:

	delete(FileName)

 Deletes old files, u can reuse the filenames afterwards

### Overwrite:

	overwrite(FileName)

 If theres already a file with the given filename it does the same thing like upload just deleting the filename first.
 If there is not it throws an exception.


##### And the most important: Have fun.





