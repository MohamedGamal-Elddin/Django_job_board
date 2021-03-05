import django_filters
from .models import Job

class job_Filter(django_filters.FilterSet):
    # title = django_filters.CharFilter(lookup_expr='iexact')
    title = django_filters.CharFilter(lookup_expr='icontains')


    class Meta:
        model = Job
        fields = '__all__'
        exclude=('owner','published_at','image','slug','vacancy')
        