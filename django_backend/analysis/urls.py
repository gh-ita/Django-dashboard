from django.urls import path
from views.api_views import BatchDataUploadView


urlpatterns = [
    path("upload/", BatchDataUploadView.as_view(), name = "batch_data_upload")
]