from django import forms
from house.models import Member, Notice

class MemberForm(forms.ModelForm):
    class Meta:
        # form based on fields of Member class
        model = Member
        fields = "__all__"

class NoticeForm(forms.ModelForm):
    class Meta:
        # form based on fields of Notice model
        model = Notice
        fields = "__all__"
        widgets = {
            'title':forms.TextInput(),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
