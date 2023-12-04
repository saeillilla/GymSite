from django.contrib import admin
from .models import BMIData,Trainer,personToTrainer,personToSubsc,Subscription

admin.site.register(BMIData)
admin.site.register(Trainer)
admin.site.register(personToSubsc)
admin.site.register(personToTrainer)
admin.site.register(Subscription)