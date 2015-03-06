from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from forms import MyRegistrationForm
from django.shortcuts import render_to_response
from django.template import RequestContext

def register_user(request):
    print "here"
    context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        print request.POST.get('first_name')
        print request.POST.get('username')
        print request.POST.get('lastname')
        user_form = MyRegistrationForm(data=request.POST)
        if user_form.is_valid():
            print "re"
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/')
        else:
            print "error"
            print user_form.errors

    else:
        user_form = MyRegistrationForm()

    return render(request,
            'gbs/register.html',
            {'user_form': user_form, 'registered': registered})

#def register(request):
#    print "here"
#    context = RequestContext(request)
#    registered = False
#    if request.method == 'POST':
#
#        user_form = MyRegistrationForm(data=request.POST)
#        if user_form.is_valid():
#
#            user = user_form.save()
#            user.set_password(user.password)
#            user.save()
#            registered = True
#            return HttpResponseRedirect('/')
#        else:
#            print user_form.errors
#
#    else:
#        user_form = MyRegistrationForm()
#
#    return render_to_response(
#            'gbs/register.html',
#            {'user_form': user_form, 'registered': registered},
#            context)
