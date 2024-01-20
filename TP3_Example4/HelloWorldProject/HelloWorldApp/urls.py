
from django.urls import path
from .views import *

urlpatterns = [
    path('bad_request/', my_bad_request_view, name='bad_request_view'),
    path('not_found/', my_not_found_view, name='not_found_view'),
    path('server_error/', my_server_error_view, name='server_error_view'),
    path('json/', my_json_view, name='json_view'),
    path('streaming/', my_streaming_view, name='streaming_view'),
    path('file/<int:file_id>/', my_file_download_view, name='file_download_view'),
    path('', homepage, name='homepage'),
    path('file_upload/', file_upload, name='file_upload'),
    path('file_upload/success/', upload_success, name='upload_success'),
    path('list_uploaded_files/', list_uploaded_files, name='list_uploaded_files'),
]
