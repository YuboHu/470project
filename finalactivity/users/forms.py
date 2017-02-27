from users.models import UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	confirm_password = forms.CharField(widget=forms.PasswordInput())
	
	def clean(self):

         cleaned_data = super(UserForm, self).clean()

         password1 = cleaned_data.get("password")

         email = cleaned_data.get("email")

         password2 = cleaned_data.get("confirm_password")

         if password1 and password2:

            if email=="":

                 msg = u"email is null"

                 self._errors["email"] = self.error_class([msg])

            if password1!=password2:

                 msg = u"passwords are not same"

                 self._errors["password"] = self.error_class([msg])

         return cleaned_data

	class Meta:
		model = User
		fields = ('username', 'email', 'password','confirm_password')
	




class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('birthday','make_public_your_user_name')



class Advan_UserForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('street_number', 'street_name', 'city_name', 'province_name', 'postal_code', 'country_name', 'latitude', 'longitude', 'isMusic', 'isSports', 'isFood_Drink', 'isParties', 'isArts', 'isBusiness', 'phonenumber', 'isMale', 'isFemale')
