# from django import forms
# # from django.contrib.auth.models import User
# from .models import UserProfile
# from .models import Profile

# # class UserForm(forms.ModelForm):
# #     class Meta:
# #         model = User
# #         fields = ['first_name', 'last_name', 'email']

# # class ProfileForm(forms.ModelForm):
# #     class Meta:
# #         model = UserProfile
# #         fields = ('description', 'picture')

# # class UploadAvatar(forms.Form):
# #     docfile = forms.FileField(label='Select an image ')


# class UserProfileForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ['description', 'picture']
# 		exclude = ('user',)

# 	# user.first_name = models.OneToOneField(User, related_name='profile')
# 	# user.last_name = 
# 	# user.email = 
	# description = models.TextField(max_length=500, default='', null=True)
	# picture = models.ImageField(upload_to='files', null=True)


# class MyUserProfileForm():