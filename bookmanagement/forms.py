from django import forms

class BookSearchForm(forms.Form):
    bookname = forms.CharField(max_length=200, label='Book Title')
