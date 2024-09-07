# import UserCreationForm class
from django.contrib.auth.forms import UserCreationForm
# import Custom User Model defined in models.py
from .models import CustomUser
class CustomUserCreationForm(UserCreationForm):
    '''
    sub class of UserCreationForm
    '''
    class Meta:
        '''
        inner class of UserCreationForm
        Attibutes:
            model: linked User Model
            fields: fields used in Form 
        '''
        # set linked User Model
        model = CustomUser
        # set fields used in From 
        fields = ('username', 'email', 'password1', 'password2')