#Discord Token
from asyncio.windows_events import ERROR_CONNECTION_ABORTED


DiscordToken = 'OTkzMDkwNzI3MTgzNjY3MjUw.GGpX7c.w2lT-w4fRuH266hq02IxoWAJSG1H3Zwpp63ai0'

#Ban Word List
BanWords = []

#Class to storage a words
class Node:
    """Class Node"""
    def __init__(self,datoInicial):
        self.Data = datoInicial
        self.next = None
        self.repetitions = 0

    def GetData(self):
        return self.Data

    def GetNext(self):
        return self.siguiente

    def AssignData(self,nuevodato):
        self.dato = nuevodato

    def AssignNext(self,nuevosiguiente):
        self.siguiente = nuevosiguiente
    
    def AddRepetition(self):
        self.repetitions += 1

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
    
    def AddRepetition(self,item):
        """Fuction to add a repetition """
        actual = self.head
        encontrado = False
        while actual != None and not encontrado:
            if actual.GetData() == item:
                encontrado = True
                actual.AddRepetition()
            else:
                actual = actual.GetNext()

class WordsDataBase():
    
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
            else:
                list = self.words[Key]
                print(list)
                list.AddRepetition(word)
        
        print("The word '{}' was added to the list of words".format(word))
    
    
    
    def GetKey(self, letter):
        letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        return letters.index(letter.lower())

Words = WordsDataBase()


#Data Base for save all the users
class User():
    """Class to represent a user"""
    
    def __init__(self,name,id,roles, created_date, join_date, high_role):
        self.Name = name
        self.Id = id
        self.Warn = 0
        self.CreatedDate = created_date
        self.JoinedDate = join_date
        self.HighRole = high_role
        self.Roles = roles
    
    def AddWarning(self):
        self.Warn += 1

class UserDataBase():
    """Class to save the all users  """
    
    def __init__(self):
        self.user_list = []
    
    def AddUser(self, user):
        self.user_list.append(user)
        
    
    def RemoveUser(self, name):
        posicion = 0
        for user in self.user_list:
            if user.name == name:
                self.user_list.pop(posicion)
                break
            else:
                posicion += 1

    def GetWarn(self, name):
        """Function to get the warning of a user"""
        for user in self.user_list:
            if user.Name == name:
                return user.Warn
        return
    
    def AddWarning(self, name):
        for user in self.user_list:
            if user.Name == name:
                user.AddWarning()
                return
        return


UserDataBase = UserDataBase()