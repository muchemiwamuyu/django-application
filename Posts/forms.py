from django import forms
from .models import Blog, Author

class BlogForm(forms.ModelForm):

    author = forms.ModelChoiceField(queryset=Author.objects.all(), empty_label="Select Author")

    class Meta:
        model = Blog
        fields = ['title', 'image', 'author', 'content', 'published']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500'
            }),
            'content': forms.Textarea(attrs={
                'class': 'border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500'
            }),
            'author': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500'
            }),
            'published': forms.CheckboxInput(attrs={
                'class': 'h-5 w-5 text-pink-600 focus:ring-pink-500 border-gray-300 rounded'
            }),

            'image': forms.ClearableFileInput(attrs={
    'class': 'border border-gray-300 rounded-lg px-4 py-2 focus:outline-none focus:ring-2 focus:ring-pink-500 focus:border-pink-500'
}),

        }
    
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['author'].widget.attrs.update({'class': 'form-select'})
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data