from django.db import models

from livefield import LiveField, LiveManager


class IntegerRangeField(models.IntegerField):
    def __init__(
            self,
            verbose_name=None,
            name=None,
            min_value=None,
            max_value=None,
            **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Persistable(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    live = LiveField()

    objects = LiveManager()
    all_objects = LiveManager(include_soft_deleted=True)

    def delete(self, **kwargs):
        self.live = False
        self.save()

    class Meta:
        abstract = True

    featured.boolean = True


class Addressable(Persistable):
    street = models.CharField(max_length=200)
    block = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=175)
    country = models.CharField(max_length=60)
    postal_code = models.CharField(max_length=10)

    class Meta:
        abstract = True


class Vet(Addressable):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Brand(Persistable):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name


class Food(Persistable):
    brand = models.ForeignKey(Brand)
    name = models.CharField(max_length=200)
    upc = models.CharField(max_length=12)

    def __str__(self):
        return self.name


class Breed(Persistable):
    name = models.CharField(max_length=200)
    url = models.URLField(max_length=200, blank=True)

    def wiki_link(self):
        return "http://www.wikipedia.com/wiki/{}".format(self.name)

    def __str__(self):
        return self.name


class Animal(Persistable):
    name = models.CharField(max_length=255)
    profile_img = models.ImageField(upload_to='media/upload', blank=True)
    breed = models.ForeignKey(Breed)
    birth_date = models.DateField('date of birth')
    microchip_id = models.CharField(max_length=255, blank=True)
    about = models.TextField()
    private = models.BooleanField(default=False)

    class Meta:
        get_latest_by = 'created'
        ordering = ('-created',)
        verbose_name_plural = 'animals'

    def __str__(self):
        return self.name


class Feeding(Persistable):
    HR = 'Hour'
    DY = 'Day'
    WK = 'Week'
    MO = 'Month'
    EA = 'Each'
    TSP = 'Tspn'
    TBS = 'Tblsp'
    CP = 'Cup'
    ML = 'Ml'
    GM = 'G'
    MG = 'MG'

    INTERVAL_CHOICES = (
        (HR, 'Hour'),
        (DY, 'Day'),
        (WK, 'Week'),
        (MO, 'Month'),
    )

    MEASUREMENT_CHOICES = (
        (EA, 'Each'),
        (TSP, 'Teaspoon'),
        (TBS, 'Tablespoon'),
        (CP, 'Cup'),
        (ML, 'Milliliter'),
        (GM, 'Gram'),
        (MG, 'Milligram'),
    )

    interval = models.CharField(
        max_length=5,
        choices=INTERVAL_CHOICES,
        default=DY
    )
    food = models.ForeignKey(Food)
    alt_food = models.CharField(max_length=255, blank=True)
    food_amount = models.DecimalField('amount', max_digits=3, decimal_places=2)
    food_measurement = models.CharField(
        'measurement',
        max_length=9,
        choices=MEASUREMENT_CHOICES,
        default=EA
    )
    animal = models.ForeignKey(Animal)
    occurrence = IntegerRangeField(min_value=0, max_value=60)
    note = models.TextField(blank=True)

    def __str__(self):
        return "{0} {1} times per {2}".format(
            self.food.name,
            self.occurrence,
            self.interval)
