from django.shortcuts import render
from .models import Person

# Create your views here.
def show(request):
        persons = Person.objects.all()
        print('Person id',persons[0].name)
        return render(request, 'index.html',{'persons':persons})


class Registration():

    def create(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass

    