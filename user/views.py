from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# do this after making profile func
from django.contrib.auth.decorators import login_required
#4th step
from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm

def register(request):
    #1st step do this 
    #form = UserCreationForm()
    #return render(request,"register.html",{'form':form})

    #2nd step do this 
    #if request.method == 'POST':
    #    form = UserCreationForm(request.POST)
    #    if form.is_valid():
    #        #3rd step add this 
    #        form.save()
    #        #3rd step add this
    #        username = form.cleaned_data.get('username')
    #        messages.success(request,f'Account created for {username}!')
    #        return redirect('index')
    #else:
    #    form = UserCreationForm()
    #return render(request,'register.html',{'form':form})   

    #4th step is to create forms.py file and import form from there to here
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #3rd step add this 
            form.save()
            #3rd step add this
            username = form.cleaned_data.get('username')
            # messages.success(request,f'Account created for {username}!')
            # 5th do this when u make login page
            messages.success(request,f'Your account has been created you are now anle to login')
            # return redirect('index')
            #5th do this when u make login page
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'register.html',{'form':form})   

#after making logout page do this or add links to basehtm


@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST,instance=request.user)
		p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request,f'Your account has been updated!')
			return redirect('profile')
	else:
		u_form = UserUpdateForm()
		p_form = ProfileUpdateForm()	

	context = {
	     'u_form':u_form,
	     'p_form':p_form
	}
	return render(request,'profile.html',context)