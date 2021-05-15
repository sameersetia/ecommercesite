from django.contrib import admin
from .models import Products, Order

# Register your models here.

admin.site.site_header = "E-Commerce site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"

class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self,request,queryset):
        queryset.update(category="default")
    change_category_to_default.short_description ='DefaultCategory'
    list_display = ('title','price','discount_price','discount_price','category','description')
    search_fields = ('title',)
    actions = ('change_category_to_default',)
    list_editable = ('price',)

class OrderAdmin(admin.ModelAdmin):
    
    list_display = ('id','name','email','contact_no','address','total')
    search_fields = ('id',)



admin.site.register(Products,ProductAdmin)
admin.site.register(Order,OrderAdmin)