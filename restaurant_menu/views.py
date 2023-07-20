from django.shortcuts import render
from django.views import generic
from .models import item


class MenuList(generic.ListView):
    queryset = item.objects.order_by("-date_created")
    template_name = "index.html"

    def get_context_data(self):
        context = {'meals': ['Pizza', 'Burger'],
                   'ingredients': 'Butter'}
        return context


class MenuItemDetail(generic.DetailView):
    model = item
    template_name = "menu_item_detail.html"
