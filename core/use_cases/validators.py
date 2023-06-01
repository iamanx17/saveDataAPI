
class Validators:
    def __init__(self, json_data=None, request=None):
        self.json_data = json_data
        self.token = request.get('Authorization')
    
    def __check_token(self):
        response = None
        if not self.token:
            response= {
                'status': "Authenication Failed",
                'remark': 'invalid token'
            }
            return response, None
    
        token = self.token.split(' ')
        print('Token is splitted', token)
        if len(token)!=2:
            response = {
                'status': "Authentication Failed",
                'remark': 'invalid token'
            }
            return response, None
        
        return None, token[1]

    
    def createValidate(self):
        checktoken , token = self.__check_token()
        
        if checktoken:
            return checktoken, None
        
        response = None
        if not self.json_data.get('key'):
            response={
                'status': "KeyError",
                "remark": "key is a required field!!"
            }
            return response, None

        if not isinstance(self.json_data.get('key'), str):
            response= {
                'status': "TypeError",
                'remark': 'Key should be a str value'
            }
            return response, None
        
        if not self.json_data.get('value'):
            response ={
                'status': 'KeyError',
                'remark': 'Value is a required field!!'
            }
            return response, None

        if not isinstance(self.json_data.get('value'), list):
            response = {
                'status': "TypeError",
                'remark': "value should be a list value"
            }
            return response, None
        
        print('Create Validation successful !!')
        print("The client has used the token", token[1])
        return response, token
    
    def getValidate(self):
        checktoken, token = self.__check_token()
        if checktoken:
            return checktoken, None
        
        response = None

        if not self.json_data.get('key', None):
            response={
                'status': 'KeyError',
                'remark': 'key is a required field'
            }
            return response, None
        
        if not isinstance(self.json_data.get('key'), str):
            response = {
                'status': 'TypeError',
                'remark': 'key should have a str value'
            }
            return response, None
        
        print('Fetch Validation successful!!')
        return response, token
    
    def updateValidate(self):

        checktoken, token = self.__check_token()
        response = None

        if checktoken:
            return checktoken, None
        
        if not self.json_data.get('key', None):
            response = {
                'status':'KeyError',
                'remark': 'you must pass key for which you want to update the value!!'
            }
            return response, None
        
        if not self.json_data.get('value', None) or not isinstance(self.json_data.get('value'), list):
            response ={
                'status': 'KeyError/TypeError',
                'remark': 'you must pass Value and its type should be list'
            }
            return response, None
        
        print('Update Validation successful!!')
        return response, token