from .serializer import Job_Serializer
from rest_framework.response import Response
from .models import Job
from rest_framework.decorators import api_view



@api_view(['GET'])
def job_list_api(request):
    list=Job.objects.all()
    josn_data=Job_Serializer(list,many=True).data

    return Response({'josn_data':josn_data})