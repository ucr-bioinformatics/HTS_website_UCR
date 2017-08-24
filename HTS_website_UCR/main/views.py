from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.forms import formset_factory
from .forms import ProjectSubmitForm
from .forms import FlowcellSubmitForm
from .forms import SampleSubmitForm
from .models import flowcell, project

def index(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/basic.html',{'content':['If you would like to contact me, please email me.’,’neerjabiotech@gmail.com']})

def projects_flowcells(request):
    return render(request, 'main/projects_and_flowcells.html')
    
def get_projects_flowcells(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = FlowcellSubmitForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
        	# process the data in form.cleaned_data as required
        	#id = request.POST.get(id=id, "")
        	label = request.POST.get('label', "")
        	status = request.POST.get('status', "")
        	date = request.POST.get('date', "")
        	time = request.POST.get('time', "")
        	qc_url = request.POST.get('qc_url', "")
        	flowcell_obj = flowcell(label=label, status=status, date=date, time=time, qc_url=qc_url)
        	flowcell_obj.save()
        	# redirect to a new URL:
        	return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = FlowcellSubmitForm()
    return render(request, 'main/projects_and_flowcells_submit.html', {'form': form})

def get_project(request):
    # if this is a POST request we need to process the form data
    SampleFormSet = formset_factory(SampleSubmitForm)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectSubmitForm(request.POST)
        sample_set = SampleFormSet(request.POST)
        # check whether it's valid:
        if form.is_valid() and sample_set.is_valid():
        	# process the data in form.cleaned_data as required
        	username = request.POST.get('username', "")
        	title = request.POST.get('title', "")
        	date = request.POST.get('date', "")
        	time = request.POST.get('time', "")
        	status = request.POST.get('status', "")
        	name = request.POST.get('name', "")
        	email = request.POST.get('email', "")
        	phone = request.POST.get('phone', "")
        	pi = request.POST.get('pi', "")
        	billing_account = request.POST.get('billing_account', "")
        	department = request.POST.get('department', "")
        	project_obj = project(username, title, date, time, status, name, email, phone, pi, billing_account, department)
        	project_obj.save() 
        	sample_set.save()
        	# redirect to a new URL:
        	return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectSubmitForm()
        sample_set = SampleFormSet()
    return render(request, 'main/projects.html', {'form': form, 'formset':sample_set})
    
                              

		
