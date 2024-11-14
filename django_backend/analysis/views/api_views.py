from rest_framework import generics 
from ..serializers import BatchDataSerializer
import csv 
import os

class BatchDataUploadView(generics.CreateAPIView):
    serializer_class = BatchDataSerializer
    def perform_create(self, serializer):
        batch_data = serializer.validated_data
        file_path = "./temp/batch_data.csv"
        with open(file_path, mode = 'w', newline = '') as file :
             writer = csv.DictWriter(file, fieldnames=batch_data.keys())
             writer.writeheader()
             writer.writerows(batch_data)
             