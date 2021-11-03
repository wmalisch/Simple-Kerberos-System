"""
 Contains the class and methods to create a FileServer secured with Kerberos.
 @author Sajal Saha & Kirk Vander Ploeg
"""
import ticket_granting_service
import shared_secret_key


class FileServer:
    def __init__(self):
        self.TGS = ticket_granting_service.TGS()
    """
    This method takes a user object and requested file as input.
    It checks whether the user is authenticated to get
    access to the file or not. This is done through the following steps:
        1) Get an encrypted token from the user by requesting the user to be 
        authenticated from the KDC. (user method getAuthenticatedKeyByKDC)
        2) Decrypt the tokento 
        3) check whether it is valid or not.
            a) If TGS token list contain the decrypted key then
            print Authorized otherwise Not Authorized
    @param user user who sends the request
    @param f required file
    """
    def getFile(self, user, f):
        """
        Implementation Here.
        Complete following three lines of code. Replace None with correct statements on each line.
        """
        token = user.getAuthenticatedKeyByKDC()                       #Call function from user to get an authenticated key by KDC.
        if token != None:                          #Change condition to check if token was recieved 
            decryptedToken = self.decryptTokenToInt(token)         #Call proper function to decrypt the token.
            if decryptedToken in self.TGS.TOKEN:                      #Update the if condition to see weather the decrypted token in TGS TOKEN list or not. 
                print(user.getUserName() + " is Authorized")
            else:
                print(user.getUserName() + " is Unauthorized")
        else:
            print(user.getUserName() + " is Unauthorized")
    
    """
    This method decrypts the token and converts it into an
    actual token using the key shared with the ticket granting service
    (accessed with shared_secret_key.SHARED_KEY_BTN_TGS_FS)
    @param token encrypted token
    @return decrypted token.
    """
    def decryptTokenToInt(self, token):
        """
        Implementation Here. Replace None with correct statements on each 
        line. Read the provided document carefully before implementing. 
        *Hint: see from_bytes() here: 
        https://docs.python.org/3/library/stdtypes.html
        """
        bais = int.from_bytes(token,byteorder='big') - shared_secret_key.SHARED_KEY_BTN_TGS_FS    #Use bais to create/hold decrypted token
        return bais     #return decrypted token