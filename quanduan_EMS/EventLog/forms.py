from django.forms import Form, ModelForm
import models

class HardwareEventModelForm(ModelForm):
    class Meta:
        model = models.Hardware_Event
        exclude = ()
        
    def __init__(self, *args, **kwargs):
        super(HardwareEventModelForm, self).__init__(*args, **kwargs)

        for field_name in self.base_fields:
            field = self.base_fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})