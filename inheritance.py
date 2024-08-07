class parent_a:
    def __init__(self,ear,nose,face,eyes):
        self.ear = ear
        self.nose = nose
        self.face = face
        self.eyes = eyes
    
    def character(self):
        print("this is parent a ")

class parent_b:
    def __init__(self,hands,legs,head):
        self.hands = hands
        self.legs = legs
        self.head = head
    
    def character(self):
        print("This is parent b")

class child(parent_a,parent_b):
    def __init__(self,ear,nose,face,eyes,hands,legs,head,gender):
        parent_a.__init__(ear,nose,face,eyes)
        parent_b.__init__(hands,legs,head)
        self.gender = gender

    def character(self):
        return(f'I am {self.gender} child,{parent_a.ear},ear,{nose}.{head}')


obj1 = child('me','mn','mf','mee','fh','fl','fl','boy')

obj1.character()
#This is a new comment