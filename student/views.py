from django.shortcuts import render
from django.http import HttpResponse
from student.models import member
from django.template import loader
# Create your views here.
def sayHello(request):
    return HttpResponse("Hello how are you")


def getAllMembers(request):
    allMembers=member.objects.all()
    template=loader.get_template("studentdetails.html")
    return HttpResponse(template.render({"allMembers":allMembers}))