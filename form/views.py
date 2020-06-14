from django.shortcuts import render
from form.models import Form

# Create your views here.



def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        zipcode = request.POST['zip']
        comment = request.POST['comment']
        print(name, address, phone, city, state, zipcode, comment)
        print(Form)
        a = Form.objects.create(name=name, address=address, phone=phone, city=city, state=state, zipcode=zipcode, comment=comment)
        a.save()
        return render(request, 'index.html')
    else:
        return render(request, 'index.html')
