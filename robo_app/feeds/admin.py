from django.contrib import admin

from robo_app.models import News
from robo_app.models import NewsGroup
# Register your models here.

admin.site.register(News)
admin.site.register(NewsGroup)

