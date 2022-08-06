class Node:
    """Class Node"""
    def __init__(self,datoInicial):
        self.Data = datoInicial
        self.next = None

    def GetData(self):
        return self.Data

    def GetNext(self):
        return self.siguiente

    def AssignData(self,nuevodato):
        self.dato = nuevodato

    def AssignNext(self,nuevosiguiente):
        self.siguiente = nuevosiguiente

class ListaNoOrdenada:
    """ Class No Ordered List """
    def __init__(self):
        self.head = None

    def IsEmpty(self):
        return self.head == None
    
    def add(self,item):
        temp = Node(item)
        temp.AssignNext(self.head)
        self.head = temp

    def size(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador = contador + 1
            actual = actual.GetNext()
    
        return contador

    def search(self,item):
        actual = self.head
        encontrado = False
        while actual != None and not encontrado:
            if actual.GetData() == item:
                encontrado = True
            else:
                actual = actual.GetNext()
    
        return encontrado

    def delete(self,item):
        actual = self.head
        previo = None
        encontrado = False
        while not encontrado:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.GetNext()
    
        if previo == None:
            self.head = actual.GetNext()
        else:
            previo.asignarSiguiente(actual.GetNext())

class Words():
    
    def __init__(self):
        self.words = [None]*27
    
    def addWord(self, word):
        #Get the key of the first letter of the word
        Key = self.GetKey(word[0])
        
        #Get the list of words that start with the same letters
        list = self.words[Key]
    
        if list == None:
            #Create a new list of words
            list = ListaNoOrdenada()
            self.words[Key] = list
            self.words[Key].add(word)
        else:
            #Check if the word is already in the list
            if not (self.words[Key]).search(word):
                #If not, add the word to the list
                list.add(word)
    
    def GetKey(self, letter):
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        return letters.index(letter.lower())

Words = Words()
Words.addWord("Hola")

Words.addWord("hola")
Words.addWord("Xoel")
int("a")
