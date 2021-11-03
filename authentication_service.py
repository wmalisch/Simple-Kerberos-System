"""
 Contains the class representing an authentication server to authenticate
 users through the kerberos protocol.
 @author Sajal Saha & Kirk Vander Ploeg
"""
import shared_secret_key
import dataset
import random
import ticket_granting_service

class AS:
    def __init__(self):
        self.SSK = shared_secret_key.SHARED_KEY_BTN_USER_AS  #Secret key shared between user and authentication server
        self.TGS = ticket_granting_service.TGS()  #Ticket granting service object, used to access the TGT list
    """
    This method authenticates the encrypted user name and returns a TGT to 
    the user. Use the following steps to complete this method:
        1) decrypt the encrypted username
        2) if the decrypted username is valid (in the dataset):
            a) generate a random index between 0-4 and use it to retrieve
            a Ticket Granting Ticket (TGT) from the list in the TGS object 
            (self.TGS). 
            b) return the tgt
        3) If the decrypted username was not valid, return None. For this
        task, assume that the TGTs are already encrypted. IE. you can return 
        the exact element from the list.
    
    @param encryptedUserName encrypted user name
    @return tgt if authentication successful otherwise return 0
    """
    def authenticate(self, encryptedUserName):
        """
        Implementation Here. Replace None with correct statements on each line. 
        """
        decryptedUserName = self.decryptUserInfo(encryptedUserName)    # Decrypt the passed encrypted username
        if decryptedUserName in dataset.USER_LIST:                    # Update the condition in the if statement.You need to check whether our Dataset's USER_LIST contains the decryptedUserName or not. 
            index = random.randint(0, len(self.TGS.TGT) - self.SSK)            # Generate random index fulfilling the above condition. 
            tgt = self.TGS.TGT[index]              # Use the index to access corresponding TGT from TGS. 
            # Aren't I supposed to encrypt the TGT
            return tgt              # return tgt
        else:
            return None             # user not valid, return None
    

    """
    This function decrypts the user information (username). 
    To do this, we must undo the encryption that was done in user.py and is
    left for you to figure out!
    @param value user information to be decrypted
    @return decrypted user name
    """
    def decryptUserInfo(self, value):
        """
        Implementation Here. Read the provided document
        carefully before implementing. 
        """
        decryptedUserInfo = ""
        for ch in value:
           decryptedUserInfo += chr(ord(ch) - 1)
        return decryptedUserInfo  #return the decryptedUserInfo