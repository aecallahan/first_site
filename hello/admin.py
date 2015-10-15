from django.contrib import admin

from hello.models import Attempt


class AttemptAdmin(admin.ModelAdmin):
    # Set fields that appear in the Attempts admin interface
    list_display = ('player_name', 'score', 'last_guess', 'last_poke_id', 'guessed_pokes')
    # Set fields that appear when an Attempt is edited in the admin interface
    fields = list_display


admin.site.register(Attempt, AttemptAdmin)
