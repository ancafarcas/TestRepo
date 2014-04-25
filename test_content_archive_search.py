'''
Created on Apr 24, 2014

@author: anca
'''

from api_test_tool import ApiTestCase
from tests import fixtures, session, token

class ContentArchiveSearchTestCase(ApiTestCase):
    session = session
    token = token
    
    @classmethod
    def href(cls, obj_id):
        return cls.server_url + cls.uri(obj_id)
        

    @classmethod
    def setUpClass(cls):
        fixtures.init('/HR/User')



    def test_content_search(self):
        self.GET(
            '/Content/ItemImage?q.contentType=image')
            #headers={'X-Filter': 'href'})
        self.expect_status(200)
        self.inspect_json()
#         self.expect_json({
#                           'FileName': 'test',
#                           'href': self.get_url('/api-test/Content/ItemImage/1')})