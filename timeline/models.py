from django.db import models
from django.db.models import permalink

# Create your models here.

class Base(models.Model):
    """Class contains useful default fields.
    """
    name = models.CharField(max_length = 150)
    slug = models.SlugField(max_length = 50)
    description = models.TextField()

    def __unicode__(self):
        return '%s' % self.title

class Category(Base):
    """Case category (Religious Freedom, Civil Procedure, etc).
    Inherits Base, does not add any additional fields.
    """

    @permalink
    def get_absolute_url(self):
        return ('case_category', None, {'slug':self.slug})

class Justice(Base):
    """Information about the Justice.
    """
#    born = models.DateField()
    appointed_by = models.CharField(max_length = 50)
#    pres_party = models.CharField(max_length = 50)
#    joined = models.DateField()
#    cj = models.DateField(null = True, blank = True)
#    ideology = models.IntegerField()
#    left = models.DateField()
#    died = models.DateField()
#    picture = models.ImageField()
 
    @permalink
    def get_absolute_url(self):
        return ('justice', None, {'slug':self.slug})

class Case(Base):
    """The case.
    """
#    handed_down = models.DateField()
#    citations = models.IntegerField()
    category = models.ManyToManyField(Category)

    @permalink
    def get_absolute_url(self):
        return '%s' % self.title

#class Opinion(Base):
    # i.e. dissent, concurrence in part to sections I and IV, etc
#    opinion_type = CharField(max_length = 50)
#    written_by = ManyToManyField(Justice)
#    link = URLField()
    
#    @permalink
#    def get_absolute_url(self):
#        return ('opinion', None, {'slug':self.slug})
