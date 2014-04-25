'''
Created on Apr 23, 2014

@author: anca
'''

from api_test_tool import ApiTestCase
from tests import fixtures, session, token
#from os.path import os

class ContentArchiveListTestCase(ApiTestCase):
    session = session
    token = token
    
    @classmethod
    def href(cls, obj_id):
        return cls.server_url + cls.uri(obj_id)
        

    @classmethod
    def setUpClass(cls):
        fixtures.init('/HR/User')
        
    def test_list_all(self):
        # shows all the items
        self.GET('/Content/Item')
        self.expect_status(200)
        self.expect_json({'href': self.get_url('/api-test/Content/Item')})
        
    def test_list_resource(self):
        #shows only resource type files (such as images and text files)
        self.GET('/Content/Item?contentType=resource')
        self.expect_status(200)
        self.expect_json_length(1)
        self.inspect_json()        
        
    def test_list_package(self):
        #shows only package type files
        self.GET('/Content/Item?type=package')
        self.expect_status(200)
#         urlnbr = os.path.basename(self.get_url('/api-test/ContentItem'))
#         print(urlnbr)
        self.expect_json({
            'collection': [
                {'href': self.get_url('/api-test/ContentItem/444')},
                ]})    
        
        
        
#     def test_search_no_results(self):
#         # search by 
#         self.GET(
#             '/Content/Item?type=png',
#             headers={'X-Filter': 'Item.GUID'})
#         self.expect_status(200)
#         self.expect_json({'collection': []})
#         #self.inspect_json()
#         
#     def test_search_success(self):
#         # search by file name
#         self.GET(
#             '/Content/Item',
#             headers={'X-Filter': 'href'})
#         self.expect_status(200)
#         #self.inspect_json()
#         self.expect_json({
#                           'FileName': 'test',
#                           'href': self.get_url('/api-test/Content/ItemImage/1')})