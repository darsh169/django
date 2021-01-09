from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from Home.models import Entry
# Create your views here.
def home(request):
	return render(request,"home.html")

def show(request):
	data=Entry.objects.all()

	return render(request,"show.html",{'data':data})

def send(request):
	if request.method=='POST':
		ID=request.POST['id']
		data1=request.POST['data1']
		data2=request.POST['data2']
		Entry(ID=ID,data1=data1,data2=data2).save()
		msg="data Stored Successfully"

		# return HttpResponseRedirect("")
		return render(request,"home.html",{'msg':msg})

	else:
		return HttpResponse("<h1>404--Not Found</h1>")


def delete(request):
	ID=request.GET['id']
	Entry.objects.filter(ID=ID).delete()
	return HttpResponseRedirect("show")

def edit(request):
	Id=request.GET['id']
	data1=data2="not available"
	for data in Entry.objects.filter(ID=Id):
		data.data1=data1
		data.data2=data2

	context={
	'ID':Id,
	'data1':data.data1,
	'data2':data.data2
	}

	return render(request,"edit.html",context)

def RecordEdited(request):
    if request.method == 'POST':
        ID = request.POST['id']
        data1 = request.POST['data1']
        data2 = request.POST['data2']
        Entry.objects.filter(ID=ID).update(data1=data1,data2=data2)
        return HttpResponseRedirect("show")
    else:
        return HttpResponse("<h1>404 - Not Found</h1>")