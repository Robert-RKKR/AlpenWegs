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
