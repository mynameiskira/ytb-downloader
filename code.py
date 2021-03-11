#Make sure you have installed pytube3 on your system. If not done, follow these steps:-
#Open your anaconda or python3 app and use the following command:
# pip install pytubeX
#This will install the pytubeX which will be required.

from pytube import YouTube

#Asking for all the video links
n = int(input("Combien de vidéos voulez-vous télecharger :   "))
links=[]
print("\nVeuillez entrer les liens des vidéos à télecharger ( 1 lien par ligne ):")

for i in range(0,n):
    temp = input()
    links.append(temp)

#Showing all details for videos and downloading them one by one
for i in range(0,n):
    link = links[i]
    yt = YouTube(link)
    print("\nDétails de la vidéo :",i+1,"\n")
    print("Titre de la video:   ",yt.title)
    print("Nombre de vues:  ",yt.views)
    print("Durée de la vidéo:  ",yt.length,"seconds")
    stream = str(yt.streams.filter(progressive=True))
    stream = stream[1:]
    stream = stream[:-1]
    streamlist = stream.split(", ")
    print("\nDifférentes résolutions:\n")
    for i in range(0,len(streamlist)):
        st = streamlist[i].split(" ")
        print(i+1,") ",st[1]," and ",st[3],sep='')
    tag = int(input("\nQuelle résolution voulez-vous télecharger :   "))
    ys = yt.streams.get_by_itag(tag)
    print("\nEn télèchargement...")
    ys.download()
    print("\nVidéo télechargée!!")
    print()
