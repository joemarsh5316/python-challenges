A = "Hello world"

B = "I Am writing this on IDLE"

C = "Thats cool"

D = "Mine too!"

E = "Thats cool my favourite film is batman"

bestName = "Joe"

bestMovie = "Batman"
secondBestMovie = "Seven"

BestSong = "hypnotize - the notorius B.I.G"
SecondBestSong = "still D.R.E - Dr Dre, Snoop Dogg"

def printfunction():
    print(A) 
    print(B)
#user inputs their name
    name = input("What is your name?") 
#checks name agaist bestName
    if (name == bestName):
        print (D)
    else:
        print ("Well thats not as cool as "+ bestName +" but Welcome " + name +"!")
               #Well thats not as cool as Joe but Welcome Jeff!

    MovieChoice = input ("Whats your favourite movie?")
#check MoviceChoice agaist bestMovie
    if (MovieChoice == bestMovie):
        print ("Thats cool my favourite movie is also" + bestMovie +"!")
               #Thats cool my favourite movie is also Batman!
    elif (MovieChoice == secondBestMovie):
        print ("Thats cool thats my second favourite movie. My favourite is also" + bestMovie +"!")
               #Thats cool thats my second favourite movie. My favourite is also Batman!
    else:
        print ("Oh! "+ MovieChoice +" Thats a good film! My favourite is " + bestMovie +"!")
               #Oh! seven Thats a good film! My favourite is Batman!

    SongChoice = input ("Whats your favourite song?")
#check SongChoice agaist bestSongs
    if (SongChoice == BestSong):
        print ("Thats cool my favourite song is also" + BestSong +"!")
               #Thats cool my favourite song is also Hypnotize!
    elif (SongChoice == SecondBestSong):
        print ("Thats cool thats my second favourite song. My favourite is also" + BestSong +"!")
               #Thats cool thats my second favourite song. My favourite is also Hypnotise!
    else:
        print ("Oh! "+ SongChoice +" Thats a good Song! My favourite is " + BestSong +"!")
               #Oh! still D.R.E Thats a good song! My favourite is Hypnotise!


printfunction() 
