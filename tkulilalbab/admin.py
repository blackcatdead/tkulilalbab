# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from tkulilalbab.models import Guru, Post, Picture, Category, Static, Testimonial, Picture_category, Download
# Register your models here.

# admin.site.register(User)
admin.site.register(Guru)
admin.site.register(Post)
admin.site.register(Picture)
admin.site.register(Category)
admin.site.register(Static)
admin.site.register(Testimonial)
admin.site.register(Picture_category)
admin.site.register(Download)