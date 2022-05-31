from django.contrib import admin

from .models import Game, Player, Score

# admin.site.register(Die)
admin.site.register(Player)
# admin.site.register(Game)
admin.site.register(Score)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'started_at', 'finished_at']
    readonly_fields = ('started_at',)
