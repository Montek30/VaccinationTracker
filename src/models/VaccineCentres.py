from constants import ROOT_API_URL, ROOT_API_HEADER
import requests

class VaccineCentres:
    def __init__(self):
        pass
        
    def search(self, request_data):
        search_method = request_data.get("search_method", "")
        search_value = request_data.get("search_value", "")
        date = request_data.get("date", "")

        result = {
            'status': 1,
			'message':'',
			'total': 0,
			'data':[]
		}

        if search_method not in ['pincode', 'district']:
            result['status'] = 0
            result['message'] = "Invalid Search Type"

        if search_value == "":
            result['status'] = 0
            result['message'] = "Invalid Search Value"
    	
        if date == "":
            result['status'] = 0
            result['message'] = "Invalid Date"

        if result['status'] == 1:
            url = ROOT_API_URL

            if search_method == "pincode":
                url += "/findByPin?pincode=" + search_value + "&date=" + date
            else:
                url += "/calendarByDistrict?district_id=" + search_value + "&date="+ date

            header = ROOT_API_HEADER
	    	#API Call
            response = requests.get(url, headers = header)

            if response.status_code == 200:
                data = response.json()

                if search_method == "pincode":
                    res = self.modify_pincode_search_data(data)
                else:
                    res = self.modify_district_search_data(data)
                
                if res['total'] == 0:
                    result['status'] = 0
                    result['message'] = "No Data"    

                result['total'] = res['total']
                result['data'] = res['data']
            else:
                result['status'] = 0
                result['message'] = "Something went wrong!!"


        return result


    def modify_district_search_data(self, data):
    	return_data = {
			'total': len(data['centers']),
			'data':[]
    	}

    	for item in data['centers']:
    		temp = {}
    		temp['center_id'] = item['center_id']
    		temp['name'] = item['name']
    		temp['address'] = item['address']
    		temp['fee_type'] = item['fee_type']
    		temp['fee'] = item['vaccine_fees'][0]['fee']
    		temp['state'] = item['state_name']
    		temp['pincode'] = item['pincode']
    		temp['slots'] = item['sessions']
    		return_data['data'].append(temp)

    	return return_data


    def modify_pincode_search_data(self, data):
    	return_data = {
    					'total': len(data['sessions']),
    					'data':[]
    				}

    	for item in data['sessions']:
    		temp = {}
    		temp['center_id'] = item['center_id']
    		temp['name'] = item['name']
    		temp['address'] = item['address']
    		temp['fee_type'] = item['fee_type']
    		temp['fee'] = item['fee']
    		temp['available_capacity_dose1'] = item['available_capacity_dose1']
    		temp['available_capacity_dose2'] = item['available_capacity_dose2']
    		temp['slots'] = item['slots']
    		return_data['data'].append(temp)
    		
    	return return_data


    def search_v2(self, request_data):
        search_method = request_data.get("search_method", "")
        search_value = request_data.get("search_value", "")
        
        result = {
            'status': 1,
            'message':'',
            'total': 0,
            'data':[]
        }

        if search_method not in ['pincode', 'district']:
            result['status'] = 0
            result['message'] = "Invalid Search Type"

        if search_value == "":
            result['status'] = 0
            result['message'] = "Invalid Search Value"
        
        
        if result['status'] == 1:
            



            if response.status_code == 200:
                data = response.json()

                if search_method == "pincode":
                    res = self.modify_pincode_search_data(data)
                else:
                    res = self.modify_district_search_data(data)
                
                if res['total'] == 0:
                    result['status'] = 0
                    result['message'] = "No Data"    

                result['total'] = res['total']
                result['data'] = res['data']
            else:
                result['status'] = 0
                result['message'] = "Something went wrong!!"


        return result

