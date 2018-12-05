from __future__ import unicode_literals

from django.db import models
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime
from django.utils import timezone
import datetime
# from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField, get_thumbnail
from phonenumber_field.modelfields import PhoneNumberField
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField

from bs4 import BeautifulSoup

# class User(AbstractUser):
# 	avatar= models.ImageField(blank=True, null=True, upload_to='users')
# 	email = models.EmailField(unique=True, null=True)

class Guru(models.Model):
	id_guru= models.AutoField(primary_key=True)
	name= models.CharField(max_length=500, null=False, default=None)
	phone_number = PhoneNumberField()
	email= models.EmailField(max_length=500, null=False, default=None)
	twitter= models.CharField(max_length=500, null=False, default=None)
	facebook= models.CharField(max_length=500, null=False, default=None)
	description= models.CharField(max_length=500, null=False, default=None)
	# picture= models.ImageField(blank=True, null=True, upload_to='guru')
	picture= ResizedImageField(size=[206, 206], crop=['middle', 'center'], upload_to='guru')
	st= (
		(0, 'Deactive'),
		(1, 'Active'),
	)
	status= models.IntegerField(choices=st, null=False, default=1)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.name


class Category(models.Model):
	id_category= models.AutoField(primary_key=True)
	# sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	category= models.CharField(max_length=100, null=False, default=None)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category

class Post(models.Model):
	id_post= models.AutoField(primary_key=True)
	title= models.CharField(max_length=500, null=False, default=None)
	content = RichTextField()
	image= ResizedImageField(size=[900, 400], crop=['middle', 'center'], upload_to='post')
	category= models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
	author= models.CharField(max_length=500, null=False, default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.title

	def plaintext(self):
		soup = BeautifulSoup(self.content, 'html.parser')
		return soup.text

class Testimonial(models.Model):
	id_testimonial= models.AutoField(primary_key=True)
	name= models.CharField(max_length=100, null=False, default=None)
	testimonial= models.CharField(max_length=500, null=False, default=None)
	picture=  ResizedImageField(size=[206, 206], crop=['middle', 'center'], upload_to='testimonial')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	st= (
		(0, 'Deactive'),
		(1, 'Active'),
	)
	status= models.IntegerField(choices=st, null=False, default=1)
	def __str__(self):
		return self.testimonial

class Picture_category(models.Model):
	id_picture_category= models.AutoField(primary_key=True)
	# sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	picture_category= models.CharField(max_length=100, null=False, default=None)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.picture_category

class Picture(models.Model):
	id_picture= models.AutoField(primary_key=True)
	picture= models.ImageField(blank=True, null=True, upload_to='picture')
	description= models.CharField(max_length=500, null=False, default=None)
	picture_category= models.ForeignKey(Picture_category, on_delete=models.SET_NULL,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.description



class Download(models.Model):
	id_download= models.AutoField(primary_key=True)
	file= models.FileField(blank=True, null=True, upload_to='downloads')
	description= models.CharField(max_length=500, null=False, default=None)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.description

class Static(models.Model):
	id_static= models.AutoField(primary_key=True)
	# sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	static= models.CharField(max_length=100, null=False, default=None, unique=True)
	value= models.CharField(max_length=500, null=True, default=None)
	image= models.ImageField(blank=True, null=True, upload_to='statis')
	def __str__(self):
		return self.static
