from django import forms
from .models import Food

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields=['name','desc','category','servings','prep_time','ingredients','cook_time','difficulty','steps_to_follow','image']
        
        
class RecipeEditForm(forms.ModelForm):
    class Meta:
        model = Food
        fields=['name','desc','category','servings','prep_time','ingredients','cook_time','difficulty','steps_to_follow','image']


