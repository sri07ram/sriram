from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializer import EmployeeSerializer

class EmployeeCreateView(CreateAPIView):
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer=self.get_serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.validated_data,status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeGetView(RetrieveAPIView):
    serializer_class = EmployeeSerializer

    def get(self,request,*args,**kwargs):
        try:
            employee=Employee.objects.all()
            serializer=EmployeeSerializer(employee,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeUpdateView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    lf='pk'
    def get_object(self):
        pk=self.kwargs.get(self.lf)
        return get_object_or_404(Employee,pk=pk)
    def put(self, request, *args, **kwargs):
        try:
            employee=self.get_object()
            serializer=self.get_serializer(employee,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EmployeeDeleteView(DestroyAPIView):
    serializer_class = EmployeeSerializer
    lf='pk'

    def get_object(self):
        pk=self.kwargs.get(self.lf)
        return get_object_or_404(Employee,pk=pk)

    def delete(self, request, *args, **kwargs):
        pk=self.kwargs.get(self.lf)
        try:
            employee=self.get_object()
            if employee.delete():
                return Response({"message":f"id - {pk} -deleted successfully"},status=status.HTTP_200_OK)
            return Response("Invalid Credentials",status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)