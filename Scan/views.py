from django.shortcuts import render
from .forms import WebURLForm
# Create your views here.
from django.views import generic
from .models import Website
from .Scripts.broken_authentication import Broken_Authentication
from .Scripts.xss import XSS
import datetime
from django.template import loader

def evaluateWebsite(web_url):
    obj = Broken_Authentication(web_url)
    obj.run_tests()
    resp_code = obj.get_status()
    obj2 = XSS(web_url)
    obj2.scan()
    resp_code2 = obj2.get_status()
    return resp_code or resp_code2

def index_view(request):
    if request.method == 'GET':
        template = loader.get_template('Scan/index.html')
        form = WebURLForm()
        context = {
            'form': form
        }
        return render(request,'Scan/index.html', context)


def driverView(request):

    if request.method == 'GET' or request.method == 'POST':
        form = WebURLForm(request.POST)

        if form.is_valid():
            #do the scanning process
            #analyze the result
            web_url = form.cleaned_data['website_name']
            db_record = Website.objects.filter(URL= web_url)
            db_record_count = Website.objects.filter(URL=web_url).count()
            if db_record_count > 0:
                #record already exists
                last_date = db_record['lastchecked']
                curr_date = datetime.date.today()
                if last_date - curr_date > 1:
                    res = evaluateWebsite(web_url)
                    if res == True:
                        pass
                    else:
                        pass
                    # res: either a list or dictionary of results
                    #render res

                else:
                    res = Website.objects.filter(URL= web_url)
                    score = res['sql_i_score']
                    if res == True:
                        pass
                    else:
                        pass
                    #website checked in the last 24 hours
                    #retrieve the earlier result
                    pass
                #if last checked is more than 24 hours ago, check again
                #function call

            else:
                res = evaluateWebsite(web_url)
                #run the check on the website
                web_obj = Website( lastchecked= datetime.datetime.today(), sql_i_score = res, URL= web_url)
                web_obj.save()
                if res == True:
                    pass
                else:
                    pass
                #render res
                pass

        #return render(request, 'catalog/book_renew_librarian.html', context)
    pass

