from django.contrib import admin
from main.models import Opportunity, Province


class OpportunityAdmin(admin.ModelAdmin):
    list_display = (
        "last_name",
        "first_name",
        "address1",
        "address2",
        "city",
        "province",
        "postal_code",
        "phone_number1",
        "phone_number2",
        "email",
        "sin",
        "dob",
    )


admin.site.register(Province)
admin.site.register(Opportunity, OpportunityAdmin)

