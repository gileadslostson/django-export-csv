from django_export_csv import QueryCsvMixin
from django_export_csv import render_csv_response
from django.views.generic.list import ListView

from .data_init import create_student_and_get_queryset, create_college_and_get_queryset


def boolean_serializer(value):
    if value:
        return 'Y'
    else:
        return 'N'


def college_serializer(obj):
    return obj.college.name


class StudentListView(QueryCsvMixin, ListView):
    filename = 'export_student_list'
    add_datestamp = True
    use_verbose_names = True
    exclude = ['id']
    field_order = ['name', 'is_graduated']
    field_header_map = {'is_graduated': 'Graduated'}
    field_serializer_map = {'is_graduated': boolean_serializer, 'college': college_serializer}
    extra_field = ['college']
    queryset = create_student_and_get_queryset()

    def get(self, *args, **kwargs):
        return self.render_csv_response(self.get_queryset())


class CollegeListView(QueryCsvMixin, ListView):
    filename = 'export_college_list'
    add_datestamp = True
    use_verbose_names = True
    queryset = create_college_and_get_queryset()

    def get(self, *args, **kwargs):
        return self.render_csv_response(self.get_queryset())


def student_list_view(request):
    filename = 'export_student_list'
    add_datestamp = True
    use_verbose_names = True
    exclude = ['id']
    field_order = ['name', 'is_graduated']
    field_header_map = {'is_graduated': 'Graduated'}
    field_serializer_map = {'is_graduated': boolean_serializer, 'college': college_serializer}
    extra_field = ['college']

    if request.method == 'GET':
        queryset = create_student_and_get_queryset()
        return render_csv_response(
            queryset, filename=filename, add_datestamp=add_datestamp, use_verbose_names=use_verbose_names,
            exclude_field=exclude, field_order=field_order, field_header_map=field_header_map,
            field_serializer_map=field_serializer_map, extra_field=extra_field
        )