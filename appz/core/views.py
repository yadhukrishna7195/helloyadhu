from django.shortcuts import render
from django.conf import settings
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
import json
import json as simplejson
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template,render_to_string
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.


def home(request):

    



    return render(request,'core/home.html')




def about(request):



    return render(request,'core/about.html')




def skills(request):



    return render(request,'core/skills.html')





def contact(request):

    rp = request.POST.get
    response_data = {}
    print(rp,'qqqqqqqqqqqqqqqq')
    
    if request.POST:

        if rp('type') == "contact":

            Contact.objects.create(name=rp('name'),phone=rp('phone'),email=rp('email'),subject=rp('subject'),message=rp('message'),
            )
            ctx = {'e': Contact.objects.filter(email=rp('email')).order_by('-added')[0],}
            mail_subject = 'Enquiry'
            message = get_template('email/enquiry.html').render(ctx)
            msg = EmailMessage(mail_subject, message, to=[settings.TO_MAIL])
            msg.content_subtype = 'html'
            msg.send()

            response_data['status'] ='success'
            response_data['message'] ='Your enquiry has been successfully submitted'
            return HttpResponse(json.dumps(response_data), content_type='application/json')




    return render(request,'core/contact.html')





