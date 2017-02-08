from django.views import generic
from .models import Product
from taggit.models import Tag


class TopView(generic.TemplateView):
    template_name = "top.html"


class ProductView(generic.TemplateView):
    template_name = "product.html"

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        products = Product.objects.all()
        list_tags = []

        for product in products:
            temp = []
            for tag in product.tags.all():
                temp.append(tag.name)
            list_tags.append(temp)

        context["products"] = zip(Product.objects.all(), list_tags)
        return context
