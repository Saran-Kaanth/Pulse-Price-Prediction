from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import request
from django.contrib import messages
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request,"pulse/home.htm")

def result(request):
    pulse_job=joblib.load(filename='pulse\\Data\\predicion.sav')
    month_name={1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}


    df=pd.read_csv("pulse\\Data\\pulse_price.csv")
    item=LabelEncoder()

    df.item_name=item.fit_transform(df["item_name"])

    pulse_name=item.transform([request.GET['Pulse']])[0]
    months=int(request.GET['month'])
    years=int(request.GET['year'])
    pulse_ori_name=request.GET['Pulse']

    if(int(months)>=1 and int(months)<=12) and (int(years)>1000 and int(years)<=2500):
        name=month_name[int(months)]
        
        lis=[pulse_name,months,years]
        pulse_img="pulse/Pictures/black_gram.jpg"
        predictor=round(pulse_job.predict([lis])[0],2)
        print(type(months),type(years))
        return render(request,"pulse/result.html",locals())
        # return HttpResponseRedirect(reverse('home'),"pulse/home.htm",args=locals())
    else:
        messages.success(request,"Please Choose a Valid Month")
        return render(request,"pulse/home.htm")
    
    
    # except:
    #     messages.error(request,"Pleaso Choose a Valid Month")
    #     return render(request,"pulse/home.htm")