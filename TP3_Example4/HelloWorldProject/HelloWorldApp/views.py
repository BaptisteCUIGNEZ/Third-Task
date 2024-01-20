
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, JsonResponse, StreamingHttpResponse, FileResponse
from django.shortcuts import get_object_or_404
#from .models import MyFileModel
from .models import UploadedFile
from .forms import FileUploadForm
from django.contrib import messages
import time




def my_bad_request_view(request):
    if not request.GET.get('param'):

        return HttpResponseBadRequest("The 'param' parameter is required. Please go back and continue exploring my website.")


    return render(request, 'my_bad_request_view.html')

def my_not_found_view(request):


    if True:

        return HttpResponseNotFound("The requested resource was not found. Please go back and continue exploring my website.")

    #return HttpResponse("Success!")

def my_server_error_view(request):
    try:
        result = 1 / 0  
    except Exception as e:

        return HttpResponseServerError("An error occurred: {}. Please go back and continue exploring my website.".format(str(e)))


    return HttpResponse("Success!")

def my_json_view(request):

    data = {'This is': 'a test', 'Name': 'CUIGNEZ Baptiste', 'Message': 'Please go back and continue exploring my website'}

    return JsonResponse(data)

def my_streaming_view(request):
    def stream_response():
        for i in range(5):
            time.sleep(1)
            yield f"Data {i}, This is a test\n"
        time.sleep(1)
        yield "The streaming response is over.\nPlease go back and continue epxloring my website."

    return StreamingHttpResponse(stream_response(), content_type="text/plain")




def homepage(request):

    messages.success(request, 'Welcome to the HomePage!')

    return render(request, 'requests/message_home.html')




def file_upload(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']
            UploadedFile.objects.create(description=description, file=file)
            return redirect('success/')  
    else:
        form = FileUploadForm()

    return render(request, 'requests/my_file_upload_view.html', {'form': form})



from django.shortcuts import render

def upload_success(request):
    return render(request, 'requests/my_success_view.html')




def list_uploaded_files(request):
    files = UploadedFile.get_all_files()
    return render(request, 'requests/my_list_uploaded_file_view.html', {'files': files})


def my_file_download_view(request, file_id):
    file_instance = get_object_or_404(UploadedFile, pk=file_id)

    file_path = file_instance.file.path

    response = FileResponse(open(file_path, 'rb'))
    
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_instance.file.name)

    return response