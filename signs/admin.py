from django.contrib import admin
from .models import Image, ImageQueue, Newsitem, NewsitemQueue, Ticker, TickerQueue, Screen

class ScreenAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Image)
admin.site.register(ImageQueue)
admin.site.register(Newsitem)
admin.site.register(NewsitemQueue)
admin.site.register(Ticker)
admin.site.register(TickerQueue)
admin.site.register(Screen, ScreenAdmin)
