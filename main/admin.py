from django.contrib import admin
from django.http.request import HttpRequest
from .models import (
    Events,
    Subscribers,
    SubscribeToEvent,
    Testimonies,
    OurImages,
    MahnazImages,
    Post,
    FrequentQuestions,
    MahnazContacts,
)


# Register your models here.

admin.site.register(Subscribers)
admin.site.register(SubscribeToEvent)
admin.site.register(Testimonies)
admin.site.register(OurImages)
admin.site.register(MahnazImages)

admin.site.register(FrequentQuestions)


class EventsAdmin(admin.ModelAdmin):
    if Events.online_status == 0:
        exclude = "online_venu"
    if Events.online_status == 1:
        exclude = "venue"

    exclude = ("event_email", "event_status_to_come")


admin.site.register(Events, EventsAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "status",
    )
    list_filter = ("status",)
    search_fields = (
        "title",
        "content",
    )


admin.site.register(Post, PostAdmin)


class MahnazContactAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if MahnazContacts.objects.exists():
            return False
        return super().has_add_permission(request)


admin.site.register(MahnazContacts, MahnazContactAdmin)
