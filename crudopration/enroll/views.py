from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import UserProfile

#http method
#post 
#get
#delete
#put - update
#patch -partial-update
def add_show(request):
    if request.method == 'POST':   #POST method
        fm =StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration() 
    else:
        fm = StudentRegistration()  #GET method
    stud = UserProfile.objects.all()
    return render(request,'enroll/addandshow.html',{'form':fm, 'stu':stud})


def delete_data(request,id):
    if request.method == 'POST':
        pi = UserProfile.objects.get(pk=id)
        pi.delete()
    return redirect('/enroll')
    
    
def update_data(request,id):
    if request.method == 'POST':
        pi = UserProfile.objects.get(pk = id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            
    else:
        pi = UserProfile.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
        
    return render(request,'enroll/update.html',{'form':fm})