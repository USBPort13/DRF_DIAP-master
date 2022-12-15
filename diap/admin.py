from django.contrib import admin, messages
from django.utils.translation import ngettext

from .models.choices import PersonTypeSocialNetworkChoices
from .models.person import Person, PersonImage, PersonText, PersonPlaceWhereHeWas, PersonSocialNetwork


class PersonSocialNetworkAdmin(admin.ModelAdmin):
    title = 'SocialNetwork'


class PersonSocialNetworkInline(admin.StackedInline):
    model = PersonSocialNetwork
    max_num = 10
    extra = 0


class PersonPlaceWhereHeWasAdmin(admin.ModelAdmin):
    pass


class PersonPlaceWhereHeWasInline(admin.StackedInline):
    model = PersonPlaceWhereHeWas
    max_num = 10
    extra = 0


class PersonTextAdmin(admin.ModelAdmin):
    pass


class PersonTextInline(admin.StackedInline):
    model = PersonText
    max_num = 10
    extra = 0


class PersonImageAdmin(admin.ModelAdmin):
    pass


class PersonImageInline(admin.StackedInline):
    model = PersonImage
    max_num = 10
    extra = 0


class PersonAdmin(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'middle_name')
    list_display = ['first_name', 'time_create', 'time_update', 'post_status']
    ordering = ['time_update']
    inlines = [PersonImageInline, PersonSocialNetworkInline, PersonTextInline, PersonPlaceWhereHeWasInline]
    actions = ['make_published_person', 'make_unpublished_person', 'make_deleted_person']

    @admin.action(description='Mark selected person as published')
    def make_published_person(self, request, queryset):
        updated = queryset.update(post_status='PUBLISHED')
        self.message_user(request, ngettext(
            '%d Person was successfully marked as published.',
            '%d Persons were successfully marked as published.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected person as unpublished')
    def make_processing_person(self, request, queryset):
        updated = queryset.update(post_status='PROCESSING')
        self.message_user(request, ngettext(
            '%d Person was successfully marked as processing.',
            '%d Persons were successfully marked as processing.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Mark selected person as deleted')
    def make_deleted_person(self, request, queryset):
        updated = queryset.update(post_status='DELETED')
        self.message_user(request, ngettext(
            '%d Person was successfully marked as deleted.',
            '%d Persons were successfully marked as deleted.',
            updated,
        ) % updated, messages.SUCCESS)


class PersonTypeSocialNetworkAdmin(admin.ModelAdmin):
    list_display = ['type', 'time_create']
    ordering = ['type']


# -- Admin add models -- #
admin.site.register(Person, PersonAdmin)
admin.site.register(PersonTypeSocialNetworkChoices, PersonTypeSocialNetworkAdmin)
