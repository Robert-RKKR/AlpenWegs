from django.contrib import admin

from .models.section_model import SectionModel
from .models.route_model import RouteModel
from .models.trip_model import TripModel

admin.site.register(SectionModel)
admin.site.register(RouteModel)
admin.site.register(TripModel)
