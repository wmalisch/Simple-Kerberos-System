"""
 Contains the class and methods to create a user which can be authenticated
 using Kerberos.
 @author Sajal Saha & Kirk Vander Ploeg
"""
import file_server
import shared_secret_key
import authentication_service
import ticket_granting_service

class User:
    def __init__(self):
        self.userName = None
        self.AS = authentication_service.AS()
        self.TGS = ticket_granting_service.TGS()
        self.SSK = shared_secret_key.SHARED_KEY_BTN_USER_AS #Secret key shared between user and authentication server

    """
    This function sends a request to the file server to access a specific file. 
    @param fs file server reference
    @param f file reference
    """
    def sendRequest(self, fs, f):
        """
        Implementation goes Here. Replace None with correct statements on each
        line. Call getFile method from fileserver providing appropriate 
        parameters. Hint: One line code is enough. No Return.
        """
        fs.getFile(self, f)


    


    """
    This method generates an encrypted user name and password to send to
    the Authentication Service (AS) for authentication purposes. AS will 
    return an encrypted Ticket Granting Token after successful authentication. 
    Finally, the TGT needs to be sent to the TGS for further authentication. 
    The TGS will return a token after verification which is then returned by 
    this method. The steps for completion are:
        1) encrypt the User name by calling the appropriate function (in this 
        class)
        2) Pass the encrypted username to the appropriate Authenticate method 
        in the AS
            a) this should result in an encryptedTGT being returned from the AS
        3) Pass the encryptedTGT to to the ticket granting service to recieve a 
        token
            b) Use ticket_granting_service method which authenticates a TGT and 
            returns a token
        4) Return the aquired token
    @return token from TGS
    """
    def getAuthenticatedKeyByKDC(self):
        """
        Implementation Here. Replace None with correct statements on each line.
        Hint: Variables are initialize with default value.
        You have to just call proper function to assign the new value.
        """
        encryptedUserName = self.encryptUserInfo(self.userName) # Step 1: Call encrypt function with proper parameter.
        encryptedTGT =  self.AS.authenticate(encryptedUserName)     # Step 2: Send encrypted user name to AS for authentication. 
        token = self.TGS.authenticateTGT(encryptedTGT)            # Send encryptedTGT to TGS for authentication. Call proper function
        return token             # Return the token
    
    """
    This method takes the username as input for the encryption. The encryption 
    formula as follow: 
        encrypted message = a shift of ASCII value for each individual 
        character in the message by SHARED_KEY_BTN_USER_AS.
    @param value the actual message
    @return encrypted message
    """
    def encryptUserInfo(self, username):

        """
        Implementation Here. Read the provided document
        carefully before implementing. 
         
        Hint: Encryption formula explained in the assignment document.
        """
        
        encryptedUserName = "" #variable used to create/hold encrypted user name
        for ch in username:
            encryptedUserName += chr(ord(ch) + self.SSK)
        return encryptedUserName

    """
    Getter method for the userName field.
    @return user name 
    """
    def  getUserName(self):
        return self.userName

    """
    Setter method for the userName field.
    @param userName user name
    """
    def setUserName(self, username):
        self.userName = username
    
