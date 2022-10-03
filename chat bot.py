
A = "Hello world"

B = "I Am writing this on IDLE"

C = "Thats cool"

D = "Mine too!"

E = "Thats cool my favourite film is batman"

bestName = "Joe"

bestMovie = "Batman"
secondBestMovie = "Seven"

BestSong = " hypnotise"
SecondBestSong = " still D.R.E"

Positive_feelings = [ "happy","joyful", "loved", "awe","grateful"]
Negative_feelings = [ "sad", "un-eventful", "stressful", "depressing"] 

def printfunction():
    print(A) 
    print(B)
#user inputs their name
    name = input("What is your name?") 
#checks name agaist bestName
    if (name == bestName):
        print (D)
    else:
        print ("Well that's not as cool as "+ bestName +" but Welcome " + name +"!")
               #Well thats not as cool as Joe but Welcome Jeff!

    MovieChoice = input ("What's your favourite movie?")
#check MoviceChoice agaist bestMovie
    if (MovieChoice == bestMovie):
        print ("That's cool my favourite movie is also" + bestMovie +"!")
               #Thats cool my favourite movie is also Batman!
    elif (MovieChoice == secondBestMovie):
        print ("That's cool that's my second favourite movie. My favourite is also" + bestMovie +"!")
               #Thats cool thats my second favourite movie. My favourite is also Batman!
    else:
        print ("Oh! "+ MovieChoice +" That's a good film! My favourite is " + bestMovie +"!")
               #Oh! seven Thats a good film! My favourite is Batman!

    SongChoice = input ("What's your favourite song?")
#check SongChoice agaist bestSongs
    if (SongChoice == BestSong):
        print ("That's cool my favourite song is also" + BestSong +"!")
               #Thats cool my favourite song is also Hypnotize!
    elif (SongChoice == SecondBestSong):
        print ("That's cool that's my second favourite song. My favourite is also " + BestSong +"!")
               #Thats cool thats my second favourite song. My favourite is also Hypnotise!
    else:
        print ("Oh! "+ SongChoice +" That's a good Song! My favourite is " + BestSong +"!")
               #Oh! still D.R.E Thats a good song! My favourite is Hypnotise!        
 
printfunction() 
