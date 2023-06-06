from django_filters import  rest_framework as filters

from catalog.models import Author


class CharFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class AuthorFilters(filters.FilterSet):
    surname = CharFilter(field_name='surname', lookup_expr='in')
    birthday = filters.RangeFilter()
    class Meta:
        model = Author
        fields = ['birthday','surname']