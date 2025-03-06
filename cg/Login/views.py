from django.shortcuts import render,redirect
from django.http import HttpResponse
from Register.models import rDetails
from django.contrib.auth.hashers import check_password



def log(request):
    if request.method == 'POST':
        email = request.POST.get('Lemail')
        password = request.POST.get('Lpassword')
        request.session['user_email'] = email


        if email == 'Sreeson@gmail.com' and password == 'Sreeson':
            return redirect('/admin/')

        try:
            rdetails = rDetails.objects.get(REmail=email)
            if rdetails.is_approved and check_password(password, rdetails.RPassword):
                request.session['user_id'] = rdetails.id
                details = {
                    'Id': rdetails.id,
                    'name': rdetails.RName,
                    'email': rdetails.REmail,
                    'password':rdetails.RPassword,
                }

                return render(request, 'View/viewmain.html', {'details': details})
            else:
                return HttpResponse("Not Approved")
        except rDetails.DoesNotExist:
            return HttpResponse("User Dose Not Exist")
    return render(request, 'Login\login.html')


