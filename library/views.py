from django.views.generic import ListView, DetailView

from .models import Piece

class PieceList(ListView):
    queryset = Piece.objects.all()
    context_object_name = 'piece_list'

class PieceDetail(DetailView):
    queryset = Piece.objects.all()
    context_object_name = 'piece'
