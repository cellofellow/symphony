from django.views.generic import ListView, DetailView, TemplateView

from .models import Piece

class SearchView(TemplateView):
    template_name = "library/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            context["query"] = query
            context["results"] = Piece.search(query)
        return context

class PieceList(ListView):
    queryset = Piece.objects.all()
    context_object_name = 'piece_list'

class PieceDetail(DetailView):
    queryset = Piece.objects.all()
    context_object_name = 'piece'
