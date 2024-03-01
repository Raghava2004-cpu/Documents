class Browser:
    def __init__(self,homepage):
        self.tabs = [homepage]                                         #self.tabs is a list to store the url given
        self.current_tab_index = 0                                          #giving that the present index to  be zero
        print(self.tabs[self.current_tab_index])
        
    def visit(self,url):                                               #to visit another tab
        self.tabs.append(url)                                        #it keeps the visit(url) to last position in self.tabs
        self.current_tab_index +=1                                    #update the current index
        return (self.tabs[self.current_tab_index])
        
    def go_back(self,x):                                 #go back : 'x' is how many tabs after your wished tab will come
        change_index = self.current_tab_index-x                     #subtract the current tab index and x
        self.current_tab_index = change_index   
                              
        if change_index < 0:                           #if prev tabs less than x by default return initial tab
            return (self.tabs[0])
        else :    
            return (self.tabs[change_index])
            
    def go_front(self,y):                                    # same here if i am in tab 1 i want to go tab 3 then y should be 2             
        change_index1 = self.current_tab_index + y
        self.current_tab_index = change_index1
        
        if change_index1 > len(self.tabs)-1:              
            return (self.tabs[len(self.tabs)-1])
        else :    
            return (self.tabs[change_index1])  
              
    def change_tab(self):
        change_index2 = self.current_tab_index-1                  #by default the change_tab goes to  previous back tab
        return (self.tabs[change_index2])       
        
        
user1 = Browser("https://www.google.com")  
print(user1.visit("https://www.gmail.com"))
print(user1.visit("https://www.youtube.com") ) 
print(user1.go_back(2))
print(user1.go_front(1))    
        
           