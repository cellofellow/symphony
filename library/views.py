from django.views.generic import ListView, DetailView, TemplateView

from .models import Piece, Location, Performance


class SearchView(TemplateView):
    template_name = "library/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get("q")
        if query:
            context["query"] = query
            context["results"] = Piece.search(query)
        return context


class PieceDetail(DetailView):
    queryset = Piece.objects.all()
    context_object_name = 'piece'


class LocationView(DetailView):
    queryset = Location.objects.all()


class PerformanceList(ListView):
    queryset = (Performance.objects
                .prefetch_related('orchestra', 'piece')
                .order_by('-date'))
    context_object_name = 'performances'
