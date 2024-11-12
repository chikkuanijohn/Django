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
        return render(req,'home.html',{'employee':emp})
