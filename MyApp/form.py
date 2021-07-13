from django import forms
from MyApp.models import Review

class ReviewForm(forms.ModelForm):
    image = forms.ImageField(required = False)

    class Meta:
        model = Review
        fields = ["body", "image"]
        widgets = {"body" : forms.Textarea(attrs={"placeholder":"Write your reviews", "cols":70, "rows":7})}
    
    
    """body = forms.CharField(widget = forms.Textarea(attrs={"placeholder":"Write your reviews", "cols":"50px", "rows":"7px"}))
    image = forms.ImageField(required = False)"""