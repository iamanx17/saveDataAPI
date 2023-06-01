from rest_framework.authentication import TokenAuthentication
from .serializers import saveDataSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from .models import saveData
from core.use_cases.validators import Validators
from core.use_cases.saveData import CreatesaveDataUseCase, RetrievesaveDataUsecase,UpdatesaveDataUsecase
from core.domains.saveData import saveDataDomain
import json


class saveDataAPI(viewsets.ViewSet):
    queryset = saveData.objects.all()
    searializer_class = saveDataSerializer
    authentication_classes = [TokenAuthentication]

    def create(self, request):
        data = json.loads(request.body)      
        print("request headers is", request.headers)
        check_validation, token = Validators(data, request.headers).createValidate()

        if check_validation:
            return Response(check_validation)
        
        print('data available for domain is', data)
        resDomain = saveDataDomain.from_dict(data)
        response = CreatesaveDataUseCase(resDomain, token).execute()
        return Response(response)
    
    def list(self, request):
        if not request.body:
            return Response({
                'status': 'ValueError',
                'remark': 'payload is required!!'
            })
        
        data = json.loads(request.body)

        print('request data is', data)

        check_validation, token = Validators(data, request.headers).getValidate()

        if check_validation:
            Response(check_validation)
        
        print('data available for fetch operation is', data)

        response = RetrievesaveDataUsecase(data, token).execute()
        return Response(response)
    
    def update(self, request, pk=None):
        if not pk:
            return Response({
                'status':'EntityError',
                'remark': "please use /saveDataAPI/<id>/ to update the data"
            })

        if not request.body:
            return Response({
                'status': 'ValueError',
                'remark': 'Payload is required!!'
            })
        
        data = json.loads(request.body)
        
        check_validation, token = Validators(data, request.headers).updateValidate()

        if check_validation:
            return Response(check_validation)
        
        response = UpdatesaveDataUsecase(data, token, pk).execute()
        return Response(response)
    

        
        

        

