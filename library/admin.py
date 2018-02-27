from django.contrib import admin

from .models import (Artist, Piece, ScoreType, CabinetGroup,
                     Cabinet, Drawer, Orchestra, Performance)

admin.site.register(Artist)
admin.site.register(Piece)
admin.site.register(ScoreType)
admin.site.register(CabinetGroup)
admin.site.register(Cabinet)
admin.site.register(Drawer)
admin.site.register(Orchestra)
admin.site.register(Performance)
