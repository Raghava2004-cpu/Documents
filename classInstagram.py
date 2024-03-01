class Instagram:
    def __init__(self):
        self.users = {}                                    #using dictionaries to store  user ids and post ids
        self.posts = {}
        self.story = {}
        self.followers = {}
        
    def post(self,user_id,post_id):                                          #takes the user_id and post_id
        self.post_id = post_id                                            
        if user_id not in self.users:                                         #checks whether user_id there or not 
            self.users[user_id] = []                                           #if not exist creates a new list to the user_id
        self.users[user_id].append(self.post_id)                            #insert the post_id to the respective user_id in the last
          
    def post_feed(self,user_id):
        new_list = self.users[user_id]                                #new_list stores the respective user_id post in the form of list
        return (new_list[::-1])                                          #return the elements in the list in reverse order last upload post come first
        
    def upload_story(self,user_id,story_id):                             #take user_id and story_id
        if user_id  not in self.story:                              #cerates a seperate list in self.story with resp to user_id if not exists
            self.story[user_id] = []
        self.story[user_id].append(story_id)                          #insert the story id in last of self.story 
             
        
    def story_feed(self,user_id):                            
        story_list = self.story[user_id]
        return (story_list[::-1])                       #return the story of respective user_id last upload story come first
            
    def follow(self,user_id1,user_id2):                                 #user_id1 follows the user_id2
        if user_id2 not in self.followers:
            self.followers[user_id2] = []
        self.followers[user_id2].append(user_id1)  
        
    def unfollow(self,user_id1,user_id2):                                 #user_id1 unfollows the user_id2
        self.followers[user_id2].remove(user_id1)
                    
        
person = Instagram()    
person.post(1,101)
person.post(2,102)
person.post(1,103)   
print(person.post_feed(1))
person.upload_story(1,201)
person.upload_story(2,202)
(person.follow(2,1))
(person.follow(3,1))
(person.unfollow(2,1))
print(person.story_feed(1))
