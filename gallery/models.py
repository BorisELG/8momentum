from django import forms
from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


class GalleryPageTag(TaggedItemBase):
    content_object = ParentalKey(
        "GalleryPage", related_name="tagged_items", on_delete=models.CASCADE
    )


class GalleryTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get("tag")
        gallerypages = GalleryPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context["gallerypages"] = gallerypages
        return context


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255)
    author_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("author_image"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Authors"


class GalleryIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        gallerypages = self.get_children().live().order_by("-first_published_at")
        context["gallerypages"] = gallerypages
        return context

    content_panels = Page.content_panels + [FieldPanel("intro")]


class GalleryPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    authors = ParentalManyToManyField("gallery.Author", blank=True)

    tags = ClusterTaggableManager(through=GalleryPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("date"),
                FieldPanel("authors", widget=forms.CheckboxSelectMultiple),
                FieldPanel("tags"),
            ],
            heading="Gallery information",
        ),
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel("gallery_images", label="Gallery images"),
    ]


class GalleryPageGalleryImage(Orderable):
    page = ParentalKey(
        GalleryPage, on_delete=models.CASCADE, related_name="gallery_images"
    )
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        FieldPanel("image"),
        FieldPanel("caption"),
    ]

    def is_portrait(self):
        return self.image.height > self.image.width

    def is_landscape(self):
        return self.image.width > self.image.height
