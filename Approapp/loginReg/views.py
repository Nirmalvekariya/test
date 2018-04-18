from django.contrib.auth.forms import UserChangeForm
from django.shortcuts import redirect,render
from loginReg.forms import RegistrationForm
# Create your views here.

def home(request):
    return render(request,'loginReg/main_page.html')

#def login_redirect(request):
    #return redirect('loginReg/login')

def register(request):
    if request.method == 'POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/loginReg')
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'loginReg/reg_form.html',args)


def profile_view(request):
    args={'user':request.user}
    return render(request,'loginReg/profile.html',args)

def profile_edit(request):
    if request.method=='POST':
        form=UserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/loginReg/profile')
    else:
        form=UserChangeForm(instance=request.user)
        args={'form':form}
        return render(request,'loginReg/edit.html',args)
