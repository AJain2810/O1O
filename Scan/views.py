from django.shortcuts import render
from .forms import WebURLForm
# Create your views here.
from django.views import generic
from .models import Website
import datetime

def evaluateWebsite(web_url):
    pass

def driverView(request):

    if request.method == 'POST':
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
                    # res: either a list or dictionary of results
                    #render res

                else:
                    #website checked in the last 24 hours
                    #retrieve the earlier result
                    pass
                #if last checked is more than 24 hours ago, check again
                #function call

            else:
                #run the check on the website
                web_obj = Website()

                res = evaluateWebsite(web_url)
                #render res
                pass


        #return render(request, 'catalog/book_renew_librarian.html', context)

    pass

