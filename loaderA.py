# Le cool
def funLoader(spinner, color):
    from halo import Halo
    import random
    sentences = ["Patience vieux ça arrive ! ", "C'est bon je suis là ! ", "Un grand sage a dit un jour, un truc à propos de la sagesse et la patience, tu à le temps de chercher là "]

    def selectRandom(sentences):
        return random.choice(sentences)

    spinner = Halo(text=selectRandom(sentences), spinner=spinner, color = color) #'dots'
    spinner.start()

# Le classic
def classicLoader(title = None):
    import time
    def text(y):
        if y == None: # or if title is None:
            y = "Loading"
        return y
    for x in range (0,5):
        b = text(title) + "." * x
        print (b, end="\r")
        time.sleep(1)
