from django import forms
from .models import customer_reg
from .models import staff_reg
from .models import stations
from .models import trains
from .models import routes
from .models import offers
from .models import parkings
from .models import complaints

class customers(forms.ModelForm):
    class Meta():
        model=customer_reg
        fields="__all__"

class staff(forms.ModelForm):
    class Meta():
        model=staff_reg
        fields="__all__"

class station(forms.ModelForm):
    class Meta():
        model=stations
        fields="__all__"

class train(forms.ModelForm):
    class Meta():
        model=trains
        fields="__all__"

class route(forms.ModelForm):
    class Meta():
        model=routes
        fields="__all__"

class offer(forms.ModelForm):
    class Meta():
        model=offers
        fields='__all__'

class parking(forms.ModelForm):
    class Meta():
        model=parkings
        fields="__all__"

class complaint(forms.ModelForm):
    class Meta():
        model=complaints
        fields="__all__"
