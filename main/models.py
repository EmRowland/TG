from tabnanny import verbose
from django.db import models
from accounts.models import CustomUser
from autoslug import AutoSlugField

# Create your models here.


EVENT_STATUS = ((0, "Physical"), (1, "Online"))


class Events(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    event_image = models.ImageField(
        blank=False, null=False, upload_to="events", default="default.webp"
    )
    updated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    event_description = models.TextField(null=False, blank=False)

    event_name = models.CharField(null=False, blank=False, max_length=500)
    time_when = models.DateTimeField(blank=False, null=False)
    event_status_to_come = models.BooleanField(default=True)
    event_email = models.BooleanField(default=True)
    online_status = models.IntegerField(
        choices=EVENT_STATUS, default=0, verbose_name="Location"
    )
    venue = models.CharField(
        null=False, blank=True, max_length=1000, verbose_name="Physical Location"
    )
    online_venu = models.URLField(
        null=True,
        blank=True,
        verbose_name="Link To Webinar",
        help_text="Link To Webinar",
    )

    class Meta:
        verbose_name = "Add Event"

    def __str__(self):
        return self.event_name


class Subscribers(models.Model):
    user_email = models.EmailField(null=True, blank=True, unique=True)
    sub_time = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        verbose_name = "See Subscribed User"

    def __str__(self):
        return self.user_email


class SubscribeToEvent(models.Model):
    event = models.ManyToManyField(Events)
    subscribed_user_email = models.EmailField(null=False, blank=False, unique=True)
    status = models.BooleanField(default=False, null=False)

    class Meta:
        verbose_name = " See Event Subscription"

    def __str__(self):
        return self.subscribed_user_email


class Testimonies(models.Model):
    testimony = models.TextField(null=False, blank=False)
    username = models.CharField(null=False, blank=False, max_length=200)
    work = models.CharField(null=False, blank=False, max_length=200)
    image = models.ImageField(default="default.png", upload_to="testimonies/")

    class Meta:
        verbose_name = "Add Testimonie"

    def __str__(self):
        return self.username


class OurImages(models.Model):
    uploaded_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(null=False, blank=False, upload_to="Our_works")
    img_name = models.CharField(null=False, blank=False, max_length=20)

    class Meta:
        verbose_name = "Add Art Image"

    def __str__(self):
        return self.img_name


class MahnazImages(models.Model):
    image = models.ImageField(null=False, blank=False, upload_to="Mahnaz")
    image_name = models.CharField(null=False, blank=False, max_length=20)

    class Meta:
        verbose_name = "Add Images Of Mahnaz"

    def __str__(self):
        return self.image_name


STATUS = ((0, "Draft"), (1, "Publish"))


class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = AutoSlugField(populate_from="title", unique=True)
    category_blog = models.CharField(max_length=300, default="Art")
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    image_blog = models.ImageField(upload_to="blog", default="default.png")
    status = models.IntegerField(choices=STATUS, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Add Blog Post"

    def __str__(self):
        return self.title


class FrequentQuestions(models.Model):
    faq_question = models.CharField(blank=False, null=False, max_length=1000)
    faq_answer = models.CharField(blank=False, null=False, max_length=1000)
    faq_title = models.CharField(blank=False, null=False, max_length=30)

    class Meta:
        verbose_name = "Add faq"

    def __str__(self):
        return self.faq_title


class MahnazContacts(models.Model):
    facebook = models.URLField(
        blank=True, null=True, verbose_name="facebook Profile Link"
    )
    twitter = models.URLField(
        blank=True, null=True, verbose_name="Twitter Profile Link"
    )
    instagram = models.URLField(
        blank=True, null=True, verbose_name="Instagram Profile Link"
    )
    skype = models.URLField(blank=True, null=True, verbose_name="Skype Profile Link")
    linkedin = models.URLField(
        blank=True, null=True, verbose_name="LinkedIn Profile Link"
    )
    tiktok = models.URLField(blank=True, null=True, verbose_name="Tiktok Profile Link")
    phone = models.IntegerField(
        blank=True, null=True, verbose_name="Phone Number", help_text="Add country Code"
    )
    email = models.EmailField(blank=True, null=False, verbose_name="Email Address")
    state = models.CharField(
        blank=True, null=True, verbose_name="Add state", max_length=100
    )
    street = models.CharField(
        blank=True, null=True, verbose_name="Add street", max_length=100
    )
    country = models.CharField(
        blank=True,
        null=True,
        verbose_name="Add country",
        max_length=100,
        default="Canada",
    )

    class Meta:
        verbose_name = "Add Contact Info"

    def __str__(self):
        return "Mahnaz Contact Info's"
