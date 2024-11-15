import csv
import logging
from rest_framework import generics
from ..serializers import BatchDataSerializer
from rest_framework.exceptions import ValidationError
import requests 
import logging
from django.conf import settings

# Set up logging
logger = logging.getLogger(__name__)

class BatchDataUploadView(generics.CreateAPIView):
    serializer_class = BatchDataSerializer

    def perform_create(self, serializer):
        try:
            logger.debug("Starting data processing.")
            batch_data = serializer.validated_data

            # Check if batch_data is a dictionary or a list of dictionaries
            if isinstance(batch_data, dict):
                batch_data = [batch_data]

            # Define the file path
            file_path = "analysis/temp/batch_data.csv"

            # Ensure the keys in the CSV match the expected fields in the serializer
            with open(file_path, mode='w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=batch_data[0].keys())
                writer.writeheader()
                writer.writerows(batch_data)
            
            logger.debug(f"Batch data written to {file_path}.")
            
        
        except Exception as e:
            logger.error(f"Error occurred while processing the batch data: {str(e)}")
            raise ValidationError(f"Error occurred while processing the batch data: {str(e)}")
        
        

