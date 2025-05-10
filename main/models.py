from django.db import models
from django.utils.translation import gettext_lazy as _
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class HomeSlider(models.Model):
    image = models.ImageField(upload_to='slider/', verbose_name=_("Slider Image"))
    # Processed image (1920x600)
    image_resized = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1920, 600)],
        format='JPEG',
        options={'quality': 85}
    )

    alt_text = models.CharField(max_length=255, verbose_name=_("Alt Text"))
    heading = models.CharField(max_length=255, verbose_name=_("Heading"))
    subheading = models.TextField(verbose_name=_("Subheading"))
    button_text = models.CharField(max_length=100, verbose_name=_("Button Text"))
    button_url_name = models.CharField(
        max_length=100,
        verbose_name=_("Django URL Name"),
        help_text=_("Enter the Django URL name (e.g. 'about_page', 'blogs_page').")
    )
    order = models.PositiveIntegerField(default=0, verbose_name=_("Display Order"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    class Meta:
        ordering = ['order']
        verbose_name = _("Home Slider")
        verbose_name_plural = _("Home Sliders")

    def __str__(self):
        return self.heading

    def get_button_url(self):
        from django.urls import reverse
        try:
            return reverse(self.button_url_name)
        except:
            return "#"
class Announcement(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))

    class Meta:
        verbose_name = _("Announcement")
        verbose_name_plural = _("Announcements")

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=250, verbose_name=_("Title"))
    content = models.TextField(verbose_name=_("Content"))
    date = models.DateTimeField(auto_now_add=True, verbose_name=_("Date"))
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True,
        verbose_name=_("Category")
    )

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name='images', on_delete=models.CASCADE,
        verbose_name=_("Project")
    )
    image = models.ImageField(upload_to='project_images/', verbose_name=_("Image"))
    # Processed image (1920x600)
    image_resized = ImageSpecField(
        source='image',
        processors=[ResizeToFill(1920, 600)],
        format='JPEG',
        options={'quality': 85}
    )


    class Meta:
        verbose_name = _("Project Image")
        verbose_name_plural = _("Project Images")

    def __str__(self):
        return f"{self.project.title} - {self.image.name}"


class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Name"))
    email = models.EmailField(max_length=254, verbose_name=_("Email"))
    subject = models.CharField(max_length=100, verbose_name=_("Subject"))
    message = models.TextField(verbose_name=_("Message"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    class Meta:
        verbose_name = _("Contact Message")
        verbose_name_plural = _("Contact Messages")

    def __str__(self):
        return self.name
