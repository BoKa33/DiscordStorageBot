*********************************

Discord Storage V.3.5 (Beta)

Made by BoKa

*********************************

Enjoy Discords free and unlimited storage...



Prepare:

Clone this from Github,
make sure there either a folder called temp or a file called savefile.boka in the cloned folder.
if not create them (empthy).

you need the following PIP packages:

Discord:

	sudo pip install discord

Filesplit:

	sudo pip install filesplit

you will need a Discord "server"s token too. This could help you:

Download Discord and generate one

	sudo pamac install snapd

	sudo snap install discord --classic

an api key for this server is required:

here is how to create one:

	https://www.youtube.com/watch?v=gT_1c9YFffk

open DiscordStorageV3Beta5.py and paste the bot token between <TOKEN = "> and <"> in line 5.

Use it as CLI 

execute StoragCLI.sh in linux Console.

Use it as API

	Import StorageAPI.py

Uploading: 

		upload(FileName)

			Uploads a file. If you have already uploaded another file with the same name it will throw an exception,

			so make sure that the name of the file you want to upload was not used before or use the Overwrite method. 
		
			If you want to check which filenames are already in use look at getall() filename defines two things:

			The file u want to upload, and its the string u have to use in the download method to get your file back.

Download:

		download(FileName)

			Downloads a file. If the file doesn't exists it will throw an exception. Paste in the filename u have used in the Upload function,

			and the requested file will apear in the folder where this file is probably in.

Get all filenames:

		getall()

			Returns all the filenames from the Savefile. 

Delete:

		delete(FileName)

			Deletes old files, u can reuse the filenames afterwards

Overwrite:

		overwrite(Filename)

			if theres already a file with the given filename it does the same thing like upload just deleting the filename first.

			if there is not it throws an exception.


Have fun.





