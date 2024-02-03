from django.shortcuts import render
from django.http import HttpResponse

from logic import details, allotment, authenticate, info
# Create your views here.


data = details.detail
rollno = 102103001
fname = data[1]
lname = data[2]
cgpa = data[6]

temp_rollno = 0
temp_dob = 0

def allotvalues(r, d):
    global temp_rollno
    temp_rollno = r
    global temp_dob
    temp_dob = d



def home_page(request):
    return render(request, 'home.html')

# def info_page(request):

    if request.method == "POST":
        rollno = request.POST.get('rollno')
        dob = request.POST.get('dob')
        return render(request, 'info.html',{'rn':rollno, 'fn':fname, 'ln':lname,'cg':cgpa})
    # return render(request, 'info.html',{'rn':rollno, 'fn':fname, 'ln':lname,'cg':cgpa})


def info_page(request):
    if request.method == "POST":
        rollno = request.POST.get('rollno')
        dob = request.POST.get('dob')

        allotvalues(rollno, dob)

        if authenticate.check_password(rollno, dob):
            i = info.inf(temp_rollno)
            h = info.hostel(temp_rollno)
            return render(request, 'info.html', {'rn':temp_rollno, 'fn':i[0][1], 'ln':i[0][2], 'cg':i[0][6], 'hos':h[0][2], 'room':h[0][1], 'fee':h[0][3]})  
        else:
            return HttpResponse('values are wrong')



def allotment_page(request):
    
    if request.method == "POST":
        l = allotment.allot(temp_rollno) 
        return render(request, 'allotment.html',{'details':l}) 

    return render(request, 'allotment.html') 

def fee_page(request):

    if request.method == "POST":
        pref = request.POST.get('preference')
        return render(request, 'sample.html',{'p': pref}) 
    
    # return HttpResponse(<h1>'didnot post'</h1>)
