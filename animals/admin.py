from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from animals.models import Animal, Brand, Feeding, Food, Breed, Vet

class FeedingInline(admin.StackedInline):
    model = Feeding
    fieldsets = [
        ('Feed',               {'fields': ['food_amount', 'food_measurement', 'food', 'occurrence', 'interval']}),
        ('Notes', {'fields': ['note'], 'classes': ['collapse']}),
    ]
    extra = 1

class AnimalAdmin(admin.ModelAdmin):
    fields = ['name', 'birth_date', 'breed', 'microchip_id', 'about', 'private']
    inlines = [FeedingInline]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        obj.save()

class FoodInline(admin.TabularInline):
    fields = ('name', 'upc', 'featured')
    model = Food
    extra = 3

class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'featured')
    fields = ['name', 'url', 'featured']
    inlines = [FoodInline]

# class ProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'profile'

# class UserAdmin(UserAdmin):
#     inlines = (ProfileInline,)

admin.site.unregister(User)

admin.site.register(Animal, AnimalAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Breed)
admin.site.register(User, UserAdmin)
admin.site.register(Vet)

