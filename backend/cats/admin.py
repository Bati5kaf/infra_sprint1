from django.contrib import admin

from models import Achievement, Cat, AchievementCat


admin.site.register(Achievement, AchievementCat, Cat)
