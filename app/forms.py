from django import forms

def check_n(value):
    if value[0]=="N":
        raise forms.ValidationError('it cant start with N ')

def max_lenth(value):
    if len(value)<=5:
        raise forms.ValidationError('it will be take only more then length of 5')


class NameForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_n,])
    father_name=forms.CharField(max_length=100,validators=[max_lenth,])
    email=forms.EmailField()
    reemail=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    
    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reemail']
        if e!=r:
            raise forms.ValidationError('emails are not matched')
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)<=5:
            raise forms.ValidationError('it hieden data')