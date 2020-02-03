
# Create your models here.
from django.db import models
#from django.db.models import FloatField
from django.forms import ModelForm
from django import forms

class Input(models.Model):
    textA = '<[.1,.5],[.3,.4],[.2,.5]>  <[.3,.4],[.2,.6],[.2,.4]>\n<[.2,.3],[.1,.3],[.4,.7]>  <[.1,.7],[.3,.4],[.5,.6]>\n<[.4,.5],[.2,.3],[.1,.3]>  <[.5,.8],[.1,.2],[.4,.7]>\n<[.5,.6],[.3,.4],[.4,.5]>  <[.2,.5],[.4,.6],[.3,.8]>'
    textB = '<[.3,.4],[.2,.6],[.1,.3]>  <[.4,.6],[.3,.4],[.3,.5]>\n<[.4,.7],[.2,.6],[.4,.5]>  <[.2,.3],[.3,.4],[.4,.7]>\n<[.1,.3],[.2,.4],[.2,.3]>  <[.2,.6],[.3,.5],[.3,.6]>\n<[.3,.4],[.2,.3],[.3,.5]>  <[.1,.2],[.1,.4],[.2,.6]>'
    A = models.TextField(default=textA)
    B = models.TextField(default=textB)
    productScalar= models.FloatField(default=1)
    #dScalar= models.FloatField(default=1)

    #powerScalar = models.FloatField(default=1)


class InputForm(ModelForm):
    class Meta:
        model = Input
        fields = '__all__'
        widgets = {
            'A': forms.Textarea(attrs={'rows': 8, 'cols': 80}),
            'B': forms.Textarea(attrs={'rows': 8, 'cols': 80}),

        }

class InputNorm(models.Model):
    text = '<[.1,.5],[.3,.4],[.2,.5]>  <[.3,.4],[.2,.6],[.2,.4]>\n<[.2,.3],[.1,.3],[.4,.7]>  <[.1,.7],[.3,.4],[.5,.6]>\n<[.4,.5],[.2,.3],[.1,.3]>  <[.5,.8],[.1,.2],[.4,.7]>\n<[.5,.6],[.3,.4],[.4,.5]>  <[.2,.5],[.4,.6],[.3,.8]>'
    matrix = models.TextField(default=text)
    beneficial=models.BooleanField(default=True)

class InputNormForm(ModelForm):
    class Meta:
        model = InputNorm
        fields = '__all__'
        widgets = {
            'matrix': forms.Textarea(attrs={'rows': 8, 'cols': 120}),
        }

class InputAHP(models.Model):
    text = '<[.5,.5],[.5,.5],[.5,.5]>  <[.65,.75],[.2,.3],[.25,.35]>  <[.15,.25],[.1,.2],[.75,.85]>\n' \
           '<[.25,.35],[.2,.3],[.65,.75]>  <[.5,.5],[.5,.5],[.5,.5]>  <[0,.1],[0,0],[.95,1]>\n' \
           '<[.75,.85],[.1,.2],[.15,.25]>  <[.95,1],[0,0],[0,1]>  <[.5,.5],[.5,.5],[.5,.5]>' \

    matrix = models.TextField(default=text)


class InputAHPForm(ModelForm):
    class Meta:
        model = InputAHP
        fields = '__all__'
        widgets = {
            'matrix': forms.Textarea(attrs={'rows': 8, 'cols': 120}),
        }


class InputSimi(models.Model):
    text1 = '<[.1,.5],[.3,.4],[.2,.5]>\n' \
            '<[.3,.4],[.2,.6],[.2,.4]>\n' \
            '<[.2,.3],[.1,.3],[.4,.7]>\n' \
            '<[.1,.7],[.3,.4],[.5,.6]>'
    text2 = '<[.4,.5],[.2,.3],[.1,.3]>\n' \
            '<[.5,.8],[.1,.2],[.4,.7]>\n' \
            '<[.5,.6],[.3,.4],[.4,.5]>\n' \
            '<[.2,.5],[.4,.6],[.3,.8]>'

    num1 = models.TextField(default=text1)
    num2 = models.TextField(default=text2)

class InputSimiForm(ModelForm):
    class Meta:
        model = InputSimi
        fields = '__all__'
        widgets = {'num1': forms.Textarea(attrs={'rows': 8, 'cols': 80}),
                   'num2':forms.Textarea(attrs={'rows': 8, 'cols': 80})

                   }


