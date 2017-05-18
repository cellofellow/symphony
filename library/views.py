from django.views.generic import ListView

from .models import Piece

class PieceList(ListView):
    model = Piece
    context_object_name = 'piece_list'
