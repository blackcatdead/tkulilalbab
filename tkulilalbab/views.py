# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from tkulilalbab.models import Static, Testimonial, Post, Category, Guru, Picture, Picture_category, Download
from django.core.paginator import Paginator

def home(request):
	template = loader.get_template('v_home.html')
	context = {
		'page': 'Home',
		'slider_1': Static.objects.get(static='slider_1'),
		'slider_2': Static.objects.get(static='slider_2'),
		'slider_3': Static.objects.get(static='slider_3'),
		'slider_4': Static.objects.get(static='slider_4'),
		'slider_5': Static.objects.get(static='slider_5'),
		'testimonials': Testimonial.objects.all()
		# 'dataresponden': Responden.objects.get(id_responden=request.session['id_responden']),
    }

	return HttpResponse(template.render(context, request))

def blog(request, page=1):
	template = loader.get_template('v_blog.html')
	posts = Post.objects.all().order_by('-id_post')
	paginator = Paginator(posts, 5)
	context = {
		'page': 'Blog',
		'posts': paginator.page(page),
		'categories': Category.objects.all(),
    }

	return HttpResponse(template.render(context, request))

def artikel(request, judul, id):
	template = loader.get_template('v_blog.html')
	artikel = get_object_or_404(Post, id_post=id)
	context = {
		'page': 'Artikel',
		'artikel': artikel,
		'categories': Category.objects.all(),
    }

	return HttpResponse(template.render(context, request))



def pengurusyayasan(request):
	template = loader.get_template('v_pengurus_yayasan.html')
	gurus = Guru.objects.all()
	context = {
		'page': 'Pengurus Yayasan',
		'gurus': gurus,
    }

	return HttpResponse(template.render(context, request))

def gallery(request):
	template = loader.get_template('v_gallery.html')
	pictures = Picture.objects.all()
	context = {
		'page': 'Gallery',
		'pictures': pictures,
		'picture_categorys': Picture_category.objects.all()
    }

	return HttpResponse(template.render(context, request))

def download(request):
	template = loader.get_template('v_download.html')
	downloads = Download.objects.all()
	context = {
		'page': 'Download',
		'downloads': downloads,
    }

	return HttpResponse(template.render(context, request))