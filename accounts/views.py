from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy

# Create your views here.
class SignUpView(CreateView):
    ''' Sign up page view
    '''
    # form class defined in form.py
    form_class = CustomUserCreationForm
    # rendering template
    template_name = "signup.html"
    # URL pattern for redirect link after sign up completion
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        ''' override form_valid() in CreateView class
            this function is call after form validation process
            register form data
            parameters:
                form(django.formms.From):
                form_class in CustomUserCreationForm object
            return:
                HttpResponseRedirect Object:
                    return form_valid()
                    redirect to URL defined by success_url
        '''
        # save field in Form Object into database
        user = form.save()
        self.object = user
        # return from_valid() (HttpResponseREdirect)
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    ''' Singup completion page view
    '''    
    # rendering template
    template_name = "signup_success.html"
      