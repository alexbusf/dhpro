from .models import Category

"""categories for menu"""
def get_categories(request):
        context = {}
        context['categories'] = Category.objects.all()
        return context