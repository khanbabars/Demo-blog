import unittest
from Api.ProcessJson  import ProcessJson
from Apex.Web  import Web




class Testing(unittest.TestCase):
    get_api               = ProcessJson()
    json_array            = get_api.get_all_rows()
    api_id, api_data      = get_api.get_all_values(json_array)
    print(api_id, api_data)
    print(' ')
    print(' ')
    get_page_element = Web()
    web_id, web_data, = get_page_element.load_apex_application()
    print(' ')
    print(' ')
    print('========================================= ')
    print('Start test cases' )  
    print('========================================= ')
     
    def test_id(self):
        api_id = self.api_id[0]
        web_id = int(self.web_id[0])
        print(' ')
        print(' ')
        print('========================================= ')
        print('TestCase check id  1')  
        print('========================================= ')
        self.assertEqual(api_id, web_id)

    def test_data(self):
        api_data = self.api_data[0]
        web_data = self.web_data[0]
        print(' ')
        print(' ')
        print('========================================= ')
        print('TestCase check data title one' )  
        print('========================================= ')
        self.assertEqual(api_data, web_data)

if __name__ == '__main__':
    unittest.main()



