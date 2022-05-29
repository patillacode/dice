from django.contrib import admin

from .models import Die, Game, Player, Score

admin.site.register(Die)
admin.site.register(Player)
# admin.site.register(Game)
admin.site.register(Score)


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'duration', 'start_at', 'finish_at']
