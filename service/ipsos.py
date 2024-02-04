import model.action
import json
class IpsosService:
    
    def __init__(self):
        self.data_dict = dict()
        self.load_data()

    def load_data(self):
        data_file=open('data.json','r')
        self.data_dict=json.load(data_file)['actions']
        data_file.close()
        
    def find_code(self,int):
        return list(filter(lambda x:x["codeword"]==int,self.data_dict))
    
    def find_id(self,str):
        return list(filter(lambda x:x["id"]==str,self.data_dict))
