'''
Created on Apr 22, 2014

@author: anca
'''
from api_test_tool import ApiTestCase
from tests import fixtures, session, token



class ImageUploadTestCase(ApiTestCase):

    source_file = './tests/test2.png'
    source_file2 = './tests/second file.txt'
    source_file3 = './tests/test2.png'
    
    
    session = session
    token = token

    @classmethod  
    def setUp(self):
        # reset app
        fixtures.init('/HR/User')

       
    def test_image_upload1(self):
        #uploading the image       
        with open(self.source_file, 'rb') as image_file:
            self.POST('/Content/ItemImage', files=[('file', (
                    'test',
                    image_file,
                    'image/png')), ]
                      )
        self.expect_status(201)
           
        # check image itself
        uploaded_image_url = self.json_response['href'] 
                  
        self.GET(uploaded_image_url, add_server=False, stream=True)
        self.expect_status(200)
        
        userimage_url = self.json_response['href']
        self.assertEqual(
            uploaded_image_url,
            userimage_url,
            "Links to image do not match.")
        
    def test_notimage_upload(self):
        #uploading a different type of file
        with open(self.source_file2, 'rb') as file:
            self.POST('/Content/ItemImage', files=[('file', (
                    'second file',
                    file,
                    'image/png')), ]
                      )
        self.expect_status(400)
            
        
          
    def test_default_rendition_generation(self):
        #uploading the image   
        with open(self.source_file3, 'rb') as image_file:
            self.POST('/Content/ItemImage', files=[('file', (
                    'test2',
                    image_file,
                    'image/png')), ]
                      )
        self.expect_status(201)
        #checking if it is automatically renditioned    
        uploaded_image_url = self.json_response['href']+'Rendition'
        
        self.GET(uploaded_image_url, add_server=False, stream=True)
        self.expect_status(200)
        self.expect_json({'href': uploaded_image_url+'default'})

        
       
        
        

