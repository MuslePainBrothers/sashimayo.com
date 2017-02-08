from django.views import generic


class TopView(generic.TemplateView):
    template_name = "top.html"


class ProductView(generic.TemplateView):
    template_name = "product.html"
