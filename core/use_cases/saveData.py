from core.models import saveData
from rest_framework.authtoken.models import Token
import humanize


class CreatesaveDataUseCase:
    def __init__(self, savedataDomain, token):
        self.savedataDomain = savedataDomain
        self.token = token
    
    def execute(self):
        user = Token.objects.filter(key = self.token).exists()
        if not user:
            return {
                'status': 'Authentication Failed',
                'remark': 'API key didnt matched with the database'
            }
        user = Token.objects.get(key = self.token)

        if saveData.objects.filter(key=self.savedataDomain.key).exists():
                saveDataEntity = saveData.objects.get(key = self.savedataDomain.key)
                id = saveDataEntity.id
                return {
                    'status': 200,
                    'remark': 'Data already created with this field!!',
                    'next_action':'Either update the data or use different key',
                    'ToUpdate': f'Use PUT request with url /saveDataAPI/{id}/'
                }
        
        saveDataModel = saveData(
            key = self.savedataDomain.key,
            value = self.savedataDomain.value,
            note = self.savedataDomain.note,
            user = user.user
        )
        saveDataModel.save()  
        
        return {
            'status': 200,
            'remark': "data creation successful!!"
        }

        
class RetrievesaveDataUsecase:
    def __init__(self, json_data, token):
        self.key = json_data.get('key')
        self.token = token
    
    def execute(self):
        user = Token.objects.filter(key = self.token).exists
        if not user:
            return {
                'status': 'Authentication Failed',
                'remark': 'API key didnt matched with the database'
            }
        
        if not self.key:
            return {
                'status': "KeyError",
                'remark': "Invalid key, please use {'key':'value'} payload"
            }

        print('searching with the field', self.key)
        
        user = Token.objects.get(key = self.token).user

        if not saveData.objects.filter(key = self.key).exists():
            return {
                'status': 'ERROR 404',
                'remark': "No data found with the field!!"
            }
        
        saveDataEntity = saveData.objects.get(key = self.key)

        if saveDataEntity.user  != user and not user.user.is_superuser:
            return {
                'status': " UnAuthorized access",
                'remark': 'You are not authorized to access this data'
            }
        
        return {
            'status': 'Data Fetch successful!!',
            'key': self.key,
            'value': saveDataEntity.value,
            'id': saveDataEntity.id,
            'note': saveDataEntity.note,
            'created_on': [humanize.naturaldate(saveDataEntity.created_on), saveDataEntity.created_on],
            'updated_on': [humanize.naturaldate(saveDataEntity.updated_on) ,saveDataEntity.updated_on]
        }

class UpdatesaveDataUsecase:
    def __init__(self, json_data, token, id):
        self.json_data = json_data
        self.id = id
        self.key = json_data.get('key')
        self.value = json_data.get('value')
        self.note = json_data.get('note')
        self.token = token
    
    def execute(self):
        user = Token.objects.filter(key = self.token).exists()
        if not user:
            return {
                'status': "404",
                'remark': 'User not found'
            }
        
        user = Token.objects.get(key = self.token).user

        if not saveData.objects.filter(id = self.id).exists():
            return {
                'status': "Content 404",
                'remark': "This content not found"
            }
        
        saveDataEntity = saveData.objects.get(id = self.id)

        if user!= saveDataEntity.user and not user.is_superuser:
            return {
                'status': 'UnAuthorized Access',
                'remark': 'You are not allowed to update this data!!'
            }
        saveDataEntity.key = self.key
        saveDataEntity.value = self.value
        if self.note:
            saveDataEntity.note = self.note
        saveDataEntity.save()

        return {
            'status': 'Update Successfull!!',
            'key':saveDataEntity.key,
            'value': saveDataEntity.value,
            'note': saveDataEntity.note
        }