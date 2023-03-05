from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager


class Post(models.Model):
    def get_absolute_url(self):
        return reverse('polls:post_detail',
                       args=[self.publish.year,
                             self.publish.strftime('%m'),
                             self.publish.strftime('%d'),
                             self.slug])
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Pub')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)


class ingredientItem(models.Model):
    productName = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    size = models.CharField(max_length=20, null='small')
    unitPrice = models.DecimalField(max_digits=19, decimal_places=2)
    img_url = models.TextField()

    def __str__(self):
        return str(self.productName)


class Recipe(models.Model):
    def get_absolute_url(self):
        return reverse('polls:recipes-detail',
                       args=[self.id, self.title])
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img_url = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    def get_absolute_url(self):
        return reverse('polls:product_list_by_category',
                       args=[self.slug])
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    def get_absolute_url(self):
        return reverse('polls:product_detail',
                       args=[self.id, self.slug])
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Visual(models.Model):
    class Meta:
        db_table = 'app_ideator_visuals'
    img = models.CharField(max_length=120, verbose_name='Файл картинки')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Описание')
    alt = models.TextField(verbose_name='Подсказка')
    index = models.IntegerField(verbose_name='Индекс')

    def __unicode__(self):
        return self.title


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.ForeignKey(Product, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)


class PredResult(models.Model):
    category = models.CharField(max_length=30)
    price = models.FloatField()
    popular = models.CharField(max_length=20)

    def __str__(self):
        return self.popular