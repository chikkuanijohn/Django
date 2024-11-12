from django.shortcuts import render,redirect


# Create your views here.

std=[]
def add_std(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        std.append({'roll_no':roll,'name':name,'age':age})
        print(std)
        return redirect(add_std)
    else:
        return render(req,'home.html',{'student':std})
    
    def edit(req,id):
        std_dtls=''
        for i in std:
            if i['roll_no']==id:
                std_dtls=i
                print(std_dtls)
                if req.method=='POST':
                    roll=req.POST['roll_no']
                    name=req.POST['name']
                    age=req.POST['age']
                    std_dtls['roll_no']=roll
                    std_dtls['name']=name
                    std_dtks['age']=age
                    return redirect(add_std)
                return render(req,'edit.html',{'student':std_dtls})
                  

