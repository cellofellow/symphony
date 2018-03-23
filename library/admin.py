from django.contrib import admin

from .models import Artist, Piece, Location, Orchestra, Performance

admin.site.register(Artist)
admin.site.register(Piece)
admin.site.register(Location)
admin.site.register(Orchestra)
admin.site.register(Performance)
