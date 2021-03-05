from django.shortcuts import render,redirect
from .models import Job
from django.core.paginator import Paginator
from django.urls import reverse
from .form import ApllyForm,post_jobForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .filters import job_Filter


# Create your views here.

def job_list(request):
    job_list=Job.objects.all()

    my_filter = job_Filter(request.GET, queryset=job_list)
    job_list=my_filter.qs

    paginator = Paginator(job_list,3)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    context={'jobs':page_obj,'my_filter':my_filter} 

    return render (request,'job/job_list.html',context)


def job_details(request,slug):
    job_details=Job.objects.get(slug=slug)
    if request.method=='POST':
        form=ApllyForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_details
            myform.save()

    else:
        form=ApllyForm()    


    context={'details':job_details,'form':form}
    return render (request,'job/job_details.html',context)

@login_required
def job_post(request):

    if request.method=='POST':
        form=post_jobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form=post_jobForm() 

    return render(request,'job/job_post.html',{'form':form})            


    