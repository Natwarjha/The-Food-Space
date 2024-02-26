from django.contrib import admin
from users.models import Profile, Itempictures, CusOrders,CusRatingFeedback 

# Register your models here.

admin.site.register(Profile)
admin.site.register(Itempictures)
admin.site.register(CusOrders)
admin.site.register(CusRatingFeedback)




