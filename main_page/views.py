from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'main_page.html')
def about_us(request):
    return render(request,'about_us.html')
def sources(request):
    return render(request,'sources.html')
def privacy_policy(request):
    return render(request,'privacy_policy_page.html')
def contactus(request):
    return render(request,'contact_us.html')
def exams(request):
    return render(request,'exam_main_page.html')
def exam_subpage(request):
    return render(request,'exam_subpage.html')
def hof_army(request):
    return render(request,'hof_army.html')