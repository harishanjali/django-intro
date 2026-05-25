from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def student(request):
    if request.method=='POST':
        student_name = request.POST.get('studentName')
        email = request.POST.get('email')
        course = request.POST.get('course')
        context = {
            'student_name':student_name,
            'course':course,
            'email':email
        }
        return render(request,'output.html',context)
    if request.method=='GET':
        return render(request,'st.html')