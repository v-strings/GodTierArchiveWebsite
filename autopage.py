from internetarchive import get_item
import os
import urllib

# ACCESS_KEY = 
CHANNEL = "crimsonarchive"
# SECRET_KEY = 
IndexTemplate = ["[channel-name]", "\n=","\n", "\n", "\n", ".. toctree:: \n\t:maxdepth: 2\n\n\tvideos"]
VideoTemplate = ["Archived Videos", "\n================\n", "\nTermination Reason\n ------------------\n" , "\n.. _Videos:\n\nVideos\n-------\n"]

def main():
    creator:str = ""

    item = get_item(CHANNEL)
    if (item.exists):
        creator = item.metadata['creator']
        title = item.metadata['title']
        description = item.metadata['description']
        if (item.metadata['mediatype'] == "account"):

            print(item)
        if (item.metadata['mediatype'] == "movies"):
            create_folder_template(creator,title,item)


            
    else:
        print("This channel does not exist.")

def create_rst_file():
    pass

def create_folder_template(name,title,data):
    newpath = "source\channels\\" + name 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
        with open(newpath + "\index.rst", "w") as f:
            IndexTemplate[0] = title
            IndexTemplate[1] = "\n" + ("=" * len(IndexTemplate[0]))
            f.writelines(IndexTemplate)
            
        with open(newpath + "\\videos.rst", "w" ,encoding='utf8') as f:
            f.writelines(VideoTemplate)

            for i in data.files:
                if i['format'] == 'MPEG4':
                    f.write(".. dropdown:: " + i["name"].replace(".mp4",''))
                    # f.write("\n\n\t.. raw:: html\n")
                    # f.write("\n\t\t<iframe src=\"https://archive.org/embed/" + CHANNEL + "/" + i["name"].replace(" ", "%20") + "\" width=\"640\" height=\"580\" frameborder=\"0\" webkitallowfullscreen=\"true\" mozallowfullscreen=\"true\" allowfullscreen></iframe>")
                    # f.write("\n\n")
                    
                    writepath =  data.d1 +  data.dir + "/" + i["name"]
                    writepath = "https://" + urllib.parse.quote(writepath.encode('utf8'))
                    f.write("\n\n\t.. video:: " + writepath)
                    f.write("\n\t\t:width: 640")
                    f.write("\n\t\t:height: 480")
                    f.write("\n\t\t:poster: " + writepath.replace(".mp4",'.jpg'))
                    f.write("\n\n")
            
    else:
        print("There is already a path that exists")
        exit(0)
   
if __name__ == "__main__":
    main()