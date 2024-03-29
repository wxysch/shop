from tabnanny import verbose
from django.db import models
from apps.users.models import User
from apps.categories.models import Category
from django.db.models.signals import pre_save
from apps.posts.slug_generator import unique_slug_generators

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_user")
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="post_category", blank = True, null = True)
    price = models.PositiveBigIntegerField()
    post_image = models.ImageField(upload_to = "post_image/")
    CHOICE_CURRENCY = (
        ('KGZ', 'KGZ'),
        ('USD', 'USD'),
        ('EURO', 'EURO'),
        ('RUB', 'RUB'),
        ('Договорная', 'Договорная'),
    )
    currency = models.CharField(choices=CHOICE_CURRENCY, default='Договорная', max_length=100)
    phone = models.CharField(max_length=100, default="+99677777777")
    created = models.DateTimeField(auto_now_add=True)
    STATUS_POST = (
        ('Free', 'Free'),
        ('Pro', 'Pro'),
    )
    status = models.CharField(choices=STATUS_POST, max_length=10, default='Free')
    valid = models.BooleanField(default=True, verbose_name="Действительный пост")
    slug = models.SlugField(blank=True, null = True, unique = True, verbose_name="Человекопонятный URL (само генерация)")

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image_post")
    image = models.ImageField(upload_to = "second_post_image/")

    class Meta:
        verbose_name = "Дополнительная фотография"
        verbose_name_plural = "Дополнительные фотографии"

class FavoritePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favorite_user", verbose_name="Пользователь которому понравилось пост")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="favorite_post", verbose_name="Пост которому понравилось пост")

    def __str__(self):
        return f"{self.user.username} {self.post.title} {self.id}"

    class Meta:
        verbose_name = "Понравилось пост"
        verbose_name_plural = "Понравились посты"

def slag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generators(instance)


pre_save.connect(slag_pre_save_receiver, sender=Post)

class PostComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ('-created', )
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"