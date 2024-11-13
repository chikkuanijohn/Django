from django.shortcuts import render,redirect

# Create your views here.

emp=[]
def add_emp(req):
    if req.method=='POST':
       name=req.POST['name']
       age=req.POST['age']
       position=req.POST['position']
       emp.append({'name':name,'age':age,'position':position})
       print(emp)
       return redirect(add_emp)
    else:
        return render(req,'sample.html',{'employee':emp})
def  edit(req,id):
    emp_dtls=''
    for i in emp:
        if i['roll_no']==id:
            emp_dtls=i
    print(emp_dtls)
    if req.method=='POST':
        name=req.POST['name']
        age=req.POST['age']
        position=req.POST['position']
        emp_dtls['name']=name
        emp_dtls['age']=age
        emp_dtls['position']=position
        return redirect(add_emp)
    return render(req,'edit.html',{'employee':emp_dtls})
