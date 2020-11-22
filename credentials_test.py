import unittest 
from credential import Credential


class TestCredential(unittest.TestCase):
    def setUp(self):
       
        self.new_credential = Credential("Eid","Eid","12345a","eidabdullahi10@gmail.com") # create Account object

    
    def test_init(self):
        

        self.assertEqual(self.new_credential.credential_name,"Eid")
        self.assertEqual(self.new_credential.user_name,"Eid")
        self.assertEqual(self.new_credential.password,"12345")
        self.assertEqual(self.new_credential.email,"eidabdullahi10@gmail.com")

    def test_save_credential(self):
       '''
       test to save the credentials
       '''
        self.new_credential.save_credential() # saving the new account
        self.assertEqual(len(Credential.credential_list),1)  


    def tearDown(self):
            '''
            test to clean up the credential list in the credential.py
            '''
            Credential.credential_list = []    


    def test_save_multiple_credential(self):
            '''
            to save multiple credentials
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0717062455","test@user.com") 
            test_credential.save_credential()
            self.assertEqual(len(Credential.credential_list),2)


    def test_delete_credential(self):
            '''
            to delete credentials
            '''
            self.new_credential.save_credential()
            test_credential = Credential("Test","user","0717062455","test@user.com") 
            test_credential.save_credential()

            self.new_credential.delete_credential()
            self.assertEqual(len(Credential.credential_list),1) 

    def test_find_credential_by_credential_name(self):
       '''
       to find credential by credential name
       '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0717062455","test@user.com") 
        test_credential.save_credential()

        found_credential = Credential.find_by_name("Test")

        self.assertEqual(found_credential.email,test_credential.email)  



    def test_credential_exists(self):
        '''
        to check whether the credential exists
        '''

        self.new_credential.save_credential()
        test_credential = Credential("Test","user","0717062455","test@user.com") # new account
        test_credential.save_credential()

        credential_exists = Credential.credential_exist("0712345678")
        self.assertTrue(credential_exists)    
        
                       


if __name__ == '__main__':
    unittest.main()    
