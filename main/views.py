from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView,DetailView
from .models import Project, Blog, Contact, Category, HomeSlider
from django.views.decorators.http import require_POST
from django.utils.translation import gettext_lazy as _


class AboutPageView(TemplateView):
    template_name = 'pages/about.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()
        context['gallery'] = projects
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
        projects = Project.objects.all()
        context['projects'] = projects
        context['blogs'] = Blog.objects.select_related('category').order_by('-date')[:6]
        context["sliders"] = HomeSlider.objects.filter(is_active=True)
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
        errors["name"] =_( "الاسم مطلوب")
    if not email:
        errors["email"] = _("البريد الإلكتروني مطلوب")
    if not subject:
        errors["subject"] = _("الموضوع مطلوب")
    if not message:
        errors["message"] = _("الرسالة مطلوبة")

    if errors:
        return JsonResponse({"success": False, "errors": errors})

    Contact.objects.create(name=name, email=email, subject=subject, message=message)
    return JsonResponse({"success": True})

def project_list(request):
    projects = Project.objects.all().order_by('-created_at')
    return render(request, 'pages/project_list.html', {'projects': projects})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    images = project.images.all()
    return render(request, 'pages/project_detail.html', {'project': project, 'images': images})