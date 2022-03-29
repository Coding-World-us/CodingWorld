from django.shortcuts import render
from django.http import StreamingHttpResponse
from wsgiref.util import FileWrapper
import mimetypes
import os
# from django.contrib import messages
# Create your views here.

def Home(request):
    return render(request , 'Home.html')

def Contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_list = request.POST.get('message')

        data = {
            'name' : name , 
            'email' : email , 
            'subject' : subject ,
            'message' : message_list
        }

        message = f'''
            Full Name : {name}

            Email : {email}

            Subject : {subject}
            
            Message : {message_list}
        '''.format(data['name'] , data['email'] , data['subject'] , data['message'])

        send_mail(data['subject'] , message ,'' ,  ['codingworld412@gmail.com'])
    return render(request , "Contact.html")

def About(request):
    return render(request , "About.html")

def Playlists(request):
    return render(request , "Playlists.html")

def Python_Video_0(request):
    return render(request , "Python_Video_0.html")

def video_0(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = '000_Python_Course_Announcement.pdf'
    filepath = base_dir + '/Templates/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile , 'rb') , chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment ; filename = %s" % filename
    return response

def Python_Video_1(request):
    return render(request , "Python_Video_1.html")

def video_1(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = '001_Python_Tutorial_1.pdf'
    filepath = base_dir + '/Templates/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile , 'rb') , chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment ; filename = %s" % filename
    return response

def Python_Video_2(request):
    return render(request , "Python_Video_2.html")

def video_2(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename = '002_Python_Tutorial_2.zip'
    filepath = base_dir + '/Templates/' + filename
    thefile = filepath
    filename = os.path.basename(thefile)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(thefile , 'rb') , chunk_size),content_type=mimetypes.guess_type(thefile)[0])
    response['Content-Length'] = os.path.getsize(thefile)
    response['Content-Disposition'] = "Attachment ; filename = %s" % filename
    return response

