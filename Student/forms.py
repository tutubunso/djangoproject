from django import forms
from .models import *

class SchoolForm(forms.ModelForm):
	name= forms.CharField(
		label='SCHOOl',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'saisir ecole',
    			'class':'form-control'} ) )

	class Meta:
		model = School
		fields = '__all__'


class ClasseForm(forms.ModelForm):
	name= forms.CharField(
		label='classe',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'saisir classe',
    			'class':'form-control'} ) )

	school= forms.ModelChoiceField(
		queryset=School.objects.all(),
		label='ecole',
		widget=forms.Select(
    		attrs={
    			'placeholder':'saisir ecole',
    			'class':'form-control'} ) )

	class Meta:
		model = Classe
		fields = '__all__'
		


class RegisterStudentForm(forms.ModelForm):
	nom = forms.CharField(
		label='NOM',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'saisir votre nom',
    			'class':'form-control'} ) )

	prenom = forms.CharField(
		label='PRENOM',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'saisir votre prenom',
    			'class':'form-control'} ) )

	age = forms.IntegerField(
		label='AGE',
		widget=forms.NumberInput(
			attrs={
    			'placeholder':'votre age',
    			'class':'form-control'} ))

	classe = forms.ModelChoiceField(
		queryset=Classe.objects.all(),
		label='CLASSE',
		widget=forms.Select(
    		attrs={
    			'placeholder':'saisir votre ecole',
    			'class':'form-control'} ) )

	picture = forms.ImageField(
		label='PHOTOS',
		widget=forms.FileInput(
			attrs={
    			
    			'class':'form-control-file',
    			} ))


	
	class Meta:
		model = RegisterStudent
		fields = '__all__'

		
class ProfileForm(forms.Form):

	#------------CAMPS POUR USER-----------------
	username = forms.CharField(
		required=False,
		label='USERNAME',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'username',
    			'class':'form-control'} ) )

	password = forms.CharField(
		required=False,
		label='PASSWORD',
		widget=forms.PasswordInput(
    		attrs={
    			'placeholder':'Password1',
    			'type':'password',
    			'class':'form-control'}) )

	password1 = forms.CharField(
		required=False,
		label='PASSWORD',
		widget=forms.PasswordInput(
    		attrs={
    			'placeholder':'Password2',
    			'type':'password',
    			'class':'form-control'}) )

	nom = forms.CharField(
		required=False,
		label='NOM',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'votre nom',
    			'class':'form-control'} ) )

	prenom = forms.CharField(
		required=False,
		label='PRENOM',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'votre prenom',
    			'class':'form-control'} ) )

	#------------CHAMPS POUR PROFILS--------------------
	age = forms.IntegerField(
		required=False,
		label='AGE',
		widget=forms.NumberInput(
			attrs={
    			'placeholder':'votre age',
    			'class':'form-control'} ))
		

	matricule = forms.CharField(
		required=False,
		label='MATRICULE',
		widget=forms.TextInput(
    		attrs={
    			'placeholder':'votre matricule',
    			'class':'form-control'} ) )

	picture = forms.ImageField(
		required=False,
		label='PHOTOS',
		widget=forms.FileInput(
			attrs={
    			
    			'class':'form-control',
    			} ))

class ConnexionForm(forms.Form):
    username = forms.CharField(
    	widget=forms.TextInput(
    		attrs={
    			'placeholder':'username',
    			'class':'form-control'} ) )

    password = forms.CharField(
    	widget=forms.PasswordInput(
    		attrs={
    			'placeholder':'Password',
    			'type':'password',
    			'class':'form-control'}) )
