from django.shortcuts import render
from django.conf import settings
from .models import *
from django.http import HttpResponse,HttpResponseRedirect
import json
import json as simplejson
from django.template import Context
from django.core.mail import EmailMessage
import urllib.request
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
            recaptcha_response = rp('g-recaptcha-response')
            print(recaptcha_response,'*************************')
            url = 'https://www.google.com/recaptcha/api/siteverify'
            values = {
            'secret' : settings.RECAPTCHA_PRIVATE_KEY,
            'response' :  recaptcha_response
            }
            print(values,'***************5555**********')
            data = urllib.parse.urlencode(values).encode()
            print(data,'*************33333333333333**********')

            req = urllib.request.Request(url,data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())
            print(result,'rrrrrrrrrrrrrrrrrrr')
            if result['success']:

                ctx = {'e': Contact.objects.filter(email=rp('email')).order_by('-added')[0],}
                mail_subject = 'Enquiry'
                message = get_template('email/enquiry.html').render(ctx)
                msg = EmailMessage(mail_subject, message, to=[settings.TO_MAIL])
                msg.content_subtype = 'html'
                msg.send()

                response_data['status'] ='success'
                response_data['message'] ='Your enquiry has been successfully submitted'
                return HttpResponse(json.dumps(response_data), content_type='application/json')
            else:
                response_data['status'] ='error'
                response_data['message'] ='Please tick iam not a robot box and try again'
                return HttpResponse(json.dumps(response_data), content_type='application/json')
		




    return render(request,'core/contact.html')





