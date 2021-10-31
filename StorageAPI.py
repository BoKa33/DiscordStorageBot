import DiscordStorageV3Beta5 as ds


##################################################################################################

# Put Your Token between the "" and your ID without " behind the , and before the closing Bracket

ds.setTokenAndId("",)

##################################################################################################


def upload(FileName):
    ds.upload(FileName, FileName)
    
def download(FileName):
    ds.download(FileName, FileName)
    
def overwrite(FileName):
    ds.overwrite(FileName, FileName)
    
def getall():
    return(ds.getall())
    
def delete(FileName):
    ds.delete(FileName)

