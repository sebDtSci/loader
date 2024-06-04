from halo import Halo
import time
import random


class Loader:
    # def __init__(self):
        
    
    def __selectRandom(sentences):
            return random.choice(sentences)
    
# Le cool
    def funLoader(color, spinner):
        sentences = ["Patience vieux ça arrive ! ", "C'est bon je suis là ! ", "Un grand sage a dit un jour, un truc à propos de la sagesse et la patience, tu à le temps de chercher là "]
        spinner = Halo(text=Loader.__selectRandom(sentences), spinner=spinner, color = color) #'dots'
        spinner.start()

    def __text(y):
            if y == None: # or if title is None:
                y = "Loading"
            return y
    
    # Le classic
    def classicLoader(title = None):
        for x in range (0,5):
            b =Loader.__text(title) + "." * x
            print (b, end="\r")
            time.sleep(1)
