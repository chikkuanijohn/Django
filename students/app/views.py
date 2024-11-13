from django.shortcuts import render,redirect
from .models import*


# Create your views here.

std=[]
def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        data=Student.objects.create(roll_no=roll,name=name,age=age)
        data.save()
        # std.append({'roll_no':roll,'name':name,'age':age})
        print(std)
        return redirect(add_std)
    else:
        data=Student.objects.all()
        return render(req,'home.html',{'student':data})
    
def edit(req,id):
        # std_dtls=''
        # for i in std:
        #     if i['roll_no']==id:
        #         std_dtls=i
        # print(std_dtls)
        data=Student.objects.get(pk=id)
        if req.method=='POST':
            roll=req.POST['roll_no']
            name=req.POST['name']
            age=req.POST['age']
            # std_dtls['roll_no']=roll
            # std_dtls['name']=name
            # std_dtls['age']=age
            Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age)
            return redirect(add_std)
        return render(req,'edit.html',{'student':data})


def delete(req,id):
    # for i in std:
    #     if i['roll_no']==id:
    #         std.remove(i)
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(add_std)
                  

