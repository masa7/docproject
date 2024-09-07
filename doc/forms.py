from django.forms import ModelForm
from .models import PhotoData

class PhotoDataForm(ModelForm):
    '''ModelFormのサブクラス
    '''
    class Meta:
        '''ModelFormのインナークラス
        
        Attributes:
          model: モデルのクラス
          fields: フォームで使用するモデルのフィールドを指定
        '''
        model = PhotoData
        fields = ['category', 'title', 'comment', 'image1', 'image2']
