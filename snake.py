class Snake:
    def __init__ (self):
        self.color=(0,0,255)
        self.direction="RIGHT"
        
        self.body=[(2,0),(1,0),(0,0)]
    
    def updateCoordinates(self, X,Y):
        if self.direction=="UP":
            Y=Y-1
        elif self.direction=="DOWN":
            Y=Y+1
            
        elif self.direction=="LEFT":
            X=X-1
            
        elif self.direction=="RIGHT":
            X=X+1
            
        return(X,Y)
            
        
    def eat(self):
        for i in range(0,10):
            (x,y)=self.body[0] 
            
            x,y=self.updateCoordinates(x,y)
            self.body.insert(0,(x,y))
            
    def move(self):
        (x,y)=self.body[0]
        x,y=self.updateCoordinates(x,y)
        self.body.insert(0,(x,y))
        
        #removemos la cola
        
        self.body.pop()