from django import forms
from app_billsent.models import Billsent

class ArticleForm(ModelForm):
    class Meta:
        model = Billsent
        fields = ['pub_date', 'headline', 'content', 'reporter']