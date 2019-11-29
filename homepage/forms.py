from django import forms

from .models import Bookinfo,Writer,Liuyan

class BookForm(forms.ModelForm):
    class Meta:
        model = Bookinfo
        fields = ['name','writer','jianjie',]
        labels={'name':'书名','writer':'作者','jianjie':'简介'}
        
        
class WriterForm(forms.ModelForm):
    class Meta:
        model = Writer
        fields = ['name',]
        labels={'name':'',}
        

class LiuyanForm(forms.ModelForm):
    class Meta:
        model = Liuyan
        fields = ['neirong',]
        labels={'neirong':'',}