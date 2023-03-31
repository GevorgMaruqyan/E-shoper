from django.db import models

# Create your models here.

class G_Logo(models.Model):
    logo = models.ImageField('site logo', upload_to='images')
    
    class Meta():
        verbose_name = 'Global logo'
        verbose_name_plural = 'Global logo'
# ---------------------------------------------------------------------
class Contact(models.Model):
    name = models.CharField('Contact name', max_length=50)
    email = models.EmailField('Contact email')
    subject = models.CharField('Contact subject', max_length=200)
    message = models.TextField('Contact message')

    def __str__(self):
        return self.name

class Soc(models.Model):
    name1 = models.CharField('name1',max_length=50, blank=True)
    company = models.CharField('company', max_length=50, blank=True)
    adress = models.CharField('adress', max_length=100, blank=True)
    country = models.CharField('country', max_length=50, blank=True)
    mobile = models.CharField('mobile', max_length=30, blank=True)
    fax = models.CharField('fax', max_length=50, blank=True)
    email = models.CharField('email',max_length=100, blank=True)
    name2 = models.CharField('name2',max_length=100, blank=True)
    link1 = models.URLField('link1', blank=True)
    name_link1 = models.CharField('name link1',max_length=100, blank=True)
    link2 = models.URLField('link2', blank=True)
    name_link2 = models.CharField('name link2',max_length=100, blank=True)
    link3 = models.URLField('link3', blank=True)
    name_link3 = models.CharField('name link3',max_length=100, blank=True)
    link4 = models.URLField('link4', blank=True)
    name_link4 = models.CharField('name link4',max_length=100, blank=True)

    def __str__(self):
        return self.name1
# -------------------------------------------------------------------------------    
class HomeSliderActive(models.Model):

    name1 = models.CharField('HomeSliderActive name1', max_length=60)
    name2 = models.CharField('HomeSliderActive name2', max_length=60)
    text = models.TextField('HomeSliderActive text')
    img = models.ImageField('HomeSlider image', upload_to='images')
    logo = models.ImageField('HomeSlider logo', upload_to='images')

    def __str__(self):
        return self.name1
    
class HomeSlider(models.Model):

    name1 = models.CharField('HomeSlider name1', max_length=60)
    name2 = models.CharField('HomeSlider name2', max_length=60)
    text = models.TextField('HomeSlider text')
    img = models.ImageField('HomeSlider image', upload_to='images')
    logo = models.ImageField('HomeSlider logo', upload_to='images')

    def __str__(self):
        return self.name1
# -----------------------------------------------------------------------------   
class Category(models.Model):
    name = models.CharField('Category name', max_length=100, blank=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='categ', blank=True)
    name = models.CharField('SubCategory nem',max_length=50, blank=True)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField('Brand', max_length=50, blank=True)

    def __str__(self):
        return self.name
    
class Features_Item(models.Model):
    name = models.CharField('Item name', max_length=50, blank=True)
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='subcat',blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cat', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brend_i', blank=True)
    price = models.PositiveBigIntegerField('price item', blank=True)
    img = models.ImageField('Item image', upload_to='images',blank=True)
    slug = models.SlugField('Item slug', unique=True, blank=True)

    def __str__(self):
        return self.name
    