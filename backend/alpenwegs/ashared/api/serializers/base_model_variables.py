# Base all model Representation Fields:
base_representation_fields = [
    'pk',
    'url',
]

# BaseModel serializer details:
base_model_read_only_fields = [
    'pk',
    'url',
]
base_model_fields = [
    'pk',
    'url',
]

# BaseIdentificationModel serializer details:
base_identification_read_only_fields = [
    'slug',
]
base_identification_fields = [
    'name',
    'slug',
    'snippet',
]

# BaseDescriptiveModel serializer details:
base_descriptive_read_only_fields = []
base_descriptive_fields = [
    'description',
]

# BaseCreatorModel serializer details:
base_creator_read_only_fields = [
    'creator',
]
base_creator_fields = [
    'is_public',
    'creator',
]

# BaseTimestampModel serializer details:
base_timestamp_read_only_fields = [
    'created',
    'updated',
]
base_timestamp_fields = [
    'created',
    'updated',
]

# BaseCharacteristicModel serializer details:
base_characteristic_fields = [
    'difficulty',
    'stamina_requirement',
    'experience_requirement',
    'potential_risk_requirement',
    'potential_risk_description',
    'family_friendly',
    'best_seasons',
    'best_months',
    'winter_season',
    'summer_season',
]
base_characteristic_read_only_fields = []

# BaseSportCategoryModel serializer details:
base_sport_category_fields = [
    'category',
    'category_specific_difficulty',
]
base_sport_category_read_only_fields = []

# BaseStatisticModel serializer details:
base_statistic_fields = [
    'comment_count',
    'visit_count',
    'download_count',
]
base_statistic_read_only_fields = [
    'comment_count',
    'visit_count',
    'download_count',
]

# BaseScoreModel serializer details:
base_score_fields = [
    'score',
]
base_score_read_only_fields = [
    'score',
]

# BaseObjectRepresentation serializer details:
base_object_representation_fields = [
    'app_name',
    'model_name',
    'object_id',
    'object_repr',
]
base_object_representation_read_only_fields = [
    'app_name',
    'model_name',
    'object_id',
    'object_repr',
]

# BaseGpx serializer details:
base_gpx_fields = [
    'geojson',
    'duration',
    'distance',
    'elevation_gain',
    'elevation_loss',
    'highest_elevation',
    'lowest_elevation',
    'average_grade',
    'highest_grade',
    'track_types',
    'elevation_graph',
]
base_gpx_read_only_fields = [
    'geojson',
    'duration',
    'distance',
    'elevation_gain',
    'elevation_loss',
    'highest_elevation',
    'lowest_elevation',
    'average_grade',
    'highest_grade',
    'track_types',
    'elevation_graph',
]
