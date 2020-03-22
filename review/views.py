from django.shortcuts import render,redirect

import pyrebase
from django.contrib import auth
import pyrebase
from django.contrib import auth
import time
from datetime import datetime, timezone
import pytz
import numpy as np
#import pickle
from django.http import HttpResponse
config = {
    'apiKey': "AIzaSyCz_jvYHydzLlB1W2Sra00Ydea3_JnSOEY",
    'authDomain': "diseases-ece6c.firebaseapp.com",
    'databaseURL': "https://diseases-ece6c.firebaseio.com",
    'projectId': "diseases-ece6c",
    'storageBucket': "diseases-ece6c.appspot.com",
    'messagingSenderId': "1005865594268",
    
  }
firebase = pyrebase.initialize_app(config);
authe = firebase.auth()
database=firebase.database()  
def home(request):
    return render(request, "home_rev.html") 
def sign(request):
    return render(request,"signIn.html")  
def postsign(request):
    email=request.POST.get('email')
    password=request.POST.get('password')

    try:
        doc = authe.sign_in_with_email_and_password(email,password)
    except:
        message = "invalid cerediantials"
        return render(request,"signIn.html",{"msg":message})
    print(doc['idToken'])
    session_id=doc['idToken']
    request.session['uid']=str(session_id)
    idtoken= request.session['uid']
    uid = doc['localId']
    name = database.child('doc').child(uid).child('name').get().val()
    return render(request,"review.html",{'name':name})   
def logout(request):
    auth.logout(request)
    return render(request,'signIn.html')
def signUp(request):
    return render(request,"signup.html") 
def postsignup(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    empno=request.POST.get('empno')
    password1=request.POST.get('password1')
    hospital_name=request.POST.get('hospital_name')
    if password==password1 :
       try:
         doc=authe.create_user_with_email_and_password(email,password)
         uid = doc['localId']
         data={"name":name,"username":email,"password":password,"empno":empno,"hospital_name":hospital_name}
         database.child('doc').child(uid).set(data)
       except:
         message="Unable to create account try again"
         return render(request,"signup.html",{"msg":message})
    else :
        message="Password did not match"
        return render(request,"signup.html",{"msg":message})     
    return render(request,"signIn.html")
def xcel(request):
    
    district=request.POST.get('district')
    case=request.POST.get('case')
    postive=request.POST.get('postive')
    password1=request.POST.get('password1')
    disease=request.POST.get('disease')
    datetoday=request.POST.get('datetoday')
    print(district)
    
    
    import gspread
    from oauth2client.service_account import ServiceAccountCredentials

    scope=['https://www.googleapis.com/auth/drive']
    credentials=ServiceAccountCredentials.from_json_keyfile_name('c.json',scope)
    client=gspread.authorize(credentials)
    sheet=client.open('trial').sheet1
    
    row=[district,disease,case,postive,password1,datetoday]
    index=2
    sheet.insert_row(row,index)
    return render(request,'index.html')
