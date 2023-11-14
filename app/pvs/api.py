
import json
import autopep8


#Local Class
from .controller import VulnerabilityScanner
from .utils import SharedUtils

"""
Maintain all the api request and each function name prefix with API method(GET/POST)
"""
class API(SharedUtils):

    # def post__model_feature_count(self, request):
    #     if not request.data: return API.return_error("Error: Request payload must be provided.")
    #     print(request.data)
    #     record : dict = json.loads(request.data) 
    #     model_name= record.get("model_name", None)
    #     if not model_name: return API.return_error("Error: Model name not provided.")
        
    #     try:
    #         ret_val = 0
    #         ret_data = Akida().get_model_feature_count(model_name)
    #         return {
    #             "status": ret_val,
    #             "data": ret_data
    #         }
    #     except Exception as e:
    #         return API.return_error("Error: " + str(e))

    def file_writing(self, file_name, result):
        file_path = self.get_base_dir()+ '/app/pvs/source_code/' + file_name
        with open(file_path, 'w') as file:
            file.writelines(result)
        return file_path

    def post__vul_scanner(self, request):
        if not request.data: return API.return_error("Error: Request payload must be provided.")
            
        record : dict = json.loads(request.data) 
        source_code= record.get("source_code", None)
        # input_data = record.get("input_data", None)
        if not source_code: return API.return_error("Error: Source Code not provided.")
        # if not input_data: return API.return_error("Error: Input data not provided.")
        
        try:
            file_path= self.file_writing("vul_code.py", source_code)
            vul_scanner= VulnerabilityScanner()
            bandit_scan_report= vul_scanner.bandit_scan_report(file_path)
            if len(bandit_scan_report)>0:
                return {
                    "status": 0,
                    "data": {
                        "vulnerability": bandit_scan_report
                    },
                    "msg": "Found Vulerabilities"
                }
            else:
                return {
                    "status": 0,
                    "msg": "No Vulnerability Found"
                }
        except Exception as e:
            return API.return_error("Error: " + str(e))
        
    def post__auto_format(self, request):
        if not request.data: return API.return_error("Error: Request payload must be provided.")
            
        record : dict = json.loads(request.data) 
        source_code= record.get("source_code", None)
        if not source_code: return API.return_error("Error: Source Code not provided.")        
        try:
            formatted_code = autopep8.fix_code(source_code)
            if source_code == formatted_code:
                return {
                    "status": 0,
                    "data": formatted_code,
                    "msg": "Source code already in correct format"
                }
            else:
                return {
                    "status": 0,
                    "data": formatted_code,
                    "msg": "Succesfully Autoformatted"
                }
        except Exception as e:
            return API.return_error("Error: " + str(e))