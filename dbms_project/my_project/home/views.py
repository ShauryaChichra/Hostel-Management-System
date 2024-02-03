from django.shortcuts import render
from django.http import HttpResponse

from logic import details, allotment, authenticate

# Create your views here.


data = details.detail
rollno = data[0]
fname = data[1]
lname = data[2]
cgpa = data[6]


def home_page(request):
    return render(request, 'home.html')

def info_page(request):
    if request.method == "POST":
        rollno = request.POST.get('rollno')
        dob123 = request.POST.get('dob')
        return render(request, 'info.html',{'rn':rollno, 'fn':fname, 'ln':lname,'cg':cgpa})

    # return render(request, 'info.html',{'rn':rollno, 'fn':fname, 'ln':lname,'cg':cgpa})

def allotment_page(request):
    if request.method == "POST":
        # rollno123 = request.POST.get('rollno')
        #list=allotment.allot(rollno)
        return render(request, 'allotment.html',{'details':rollno}) 

    # return render(request, 'allotment.html') 
