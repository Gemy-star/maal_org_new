from django.views.generic import TemplateView,DetailView
from .models import Projects ,Blog , Contact , Category , Gallery
from django.views.decorators.http import require_POST


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        gallery = Gallery.objects.all()
        context['gallery'] = gallery
        return context

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'

class BlogDetailPageView(DetailView):
    template_name = 'pages/blog_detail.html'
    context_object_name = 'blog'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Projects.objects.all()
        context['projects'] = projects
        context['blogs'] = Blog.objects.select_related('category').order_by('-date')[:6]
        return context

class BlogsPageView(TemplateView):
    template_name = 'pages/blogs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories

        cat_id = self.request.GET.get('category')
        blogs = Blog.objects.select_related('category').order_by('-date')

        if cat_id and cat_id.isdigit():
            blogs = blogs.filter(category_id=cat_id)

        context['blogs'] = blogs
        return context


@require_POST
def submit_contact(request):
    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "").strip()
    message = request.POST.get("message", "").strip()

    errors = {}

    if not name:
        errors["name"] = "الاسم مطلوب"
    if not email:
        errors["email"] = "البريد الإلكتروني مطلوب"
    if not subject:
        errors["subject"] = "الموضوع مطلوب"
    if not message:
        errors["message"] = "الرسالة مطلوبة"

    if errors:
        return JsonResponse({"success": False, "errors": errors})

    Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return JsonResponse({"success": True})