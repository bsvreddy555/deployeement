from django.shortcuts import render,redirect
from .models import Employee_model
# Create your views here.
def insert_emp_view(request):
    if request.method=="POST":
        f_name=request.POST.get("f_name")
        l_name=request.POST.get("l_name")
        mobile=request.POST.get("mobile")
        email=request.POST.get("email")
        salary=request.POST.get("salary")
        experience=request.POST.get("experience")
        location=request.POST.get("location")
        company=request.POST.get("company")

        data=Employee_model(
            f_name=f_name,
            l_name=l_name,
            mobile=mobile,
            email=email,
            salary=salary,
            experience=experience,
            location=location,
            company=company
        )
        data.save()
        return redirect("home")

    return render(request,"insert_emp_details.html")


def Employee_details_view(request):
    employees=Employee_model.objects.all()
    context={"employee":employees}
    return render(request,"employee_details.html",context)


def Delete_employee_Details(request,pk):
    employee=Employee_model.objects.get(id=pk)
    employee.delete()
    return redirect("home")


def Update_Data(request,pk):
    employee=Employee_model.objects.get(id=pk)
    return render(request,"Update_employee_details.html",{"employee":employee})


def Save_update_data(request,pk):
    empluyee=Employee_model.objects.get(id=pk)
    empluyee.f_name=request.POST.get("f_name")
    empluyee.l_name=request.POST.get("l_name")
    empluyee.mobile=request.POST.get("mobile")
    empluyee.email=request.POST.get("email")
    empluyee.salary=request.POST.get("salary")
    empluyee.experience=request.POST.get("experience")
    empluyee.location=request.POST.get("location")
    empluyee.company=request.POST.get("company")

    empluyee.save()
    return redirect("home")