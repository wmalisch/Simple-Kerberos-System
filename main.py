import user
import sys
import file_server


"""
Don't edit anything here. See assignment handout for expecting output
"""
def main():

        #Create 6 new users, 4 of which are valid users and seen in the dataset   
        user1 = user.User()
        user1.setUserName("BOB")
        
        user2 = user.User()
        user2.setUserName("ALICE")
    
        user3 = user.User()
        user3.setUserName("ADLEMEN")
        
        user4 = user.User()
        user4.setUserName("REVEST")
        
        user5 = user.User()
        user5.setUserName("ADLEMAN")
        
        user6 = user.User()
        user6.setUserName("RIVEST")
        
        
        
        fs = file_server.FileServer() #create a file server Object
        
        #For each user, send a request for a file from the File server
        user1.sendRequest(fs, "D://")
        user2.sendRequest(fs, "D://")
        user3.sendRequest(fs, "D://")
        user4.sendRequest(fs, "D://")
        user5.sendRequest(fs, "D://")
        user6.sendRequest(fs, "D://")

if __name__ == '__main__':
    sys.exit(main())
