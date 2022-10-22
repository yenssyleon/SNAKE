import random
class Food:
    def __init__ (self):
        self.color=(222,0,0)
        self.x=0
        self.y=0
        self.size=10
        self.status="inactive"
        
    def putfood(self,x_max,y_max):
        #Generate a rand of x 
        
        self.x=random.randint(0,x_max)
        self.y=random.randint(0,y_max)
        
        return(self.x,self.y)
        