'''
Created on Sep 6, 2020

@author: shazib
'''
from Api.Request  import Request
from Apex.Config  import Config


class ProcessJson:
    conf = Config()
    endpoint = conf.api_endpoints
    def get_all_rows(self):
        demo = Request(self.endpoint)
        json, status_code = demo.get_api()
        print('Get demo Api from Oracle Rest Data Services')
        print(json['items'])
        print('api reply '+ str(status_code))
        print('printing all rows in the Api')
        if status_code == 200:
            for items in json['items']:
                id, data = items['id'], items['data']
                print(id, data)
                items = json['items']        
        return items     
    
    def get_all_values(self, json_array):
        id  = []
        data = []
        value = json_array[0]['id']
        if value == 1:
            print('')
            print('')
            print('===============================')   
            print('extract values from the Api reply')     
            print('===============================')   
            for i in range(6):
                id.append(json_array[i]['id'])
                data.append(json_array[i]['data'])
            return id, data    
        else:
            print(404, "Demo api not found")    

                    

    
        


        

