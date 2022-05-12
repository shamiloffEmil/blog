from django import forms
from .models import Post, Dsc, Like, User, Profile ,Comment
class PostForm(forms.ModelForm):
	class Meta:
            model = Post
            fields = ('text',)

class DscForm(forms.ModelForm):
	class Meta:
		model = Dsc
		fields = ('name', 'fio', 'age', 'city', 'inter',)

class LikeForm(forms.ModelForm):
	class Meta:
			model = Like
			fields = ('like',)

class CommentForm(forms.ModelForm):
	class Meta:
			model = Comment
			fields = ('author', 'text',)

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('age', 'city', 'inter')

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)