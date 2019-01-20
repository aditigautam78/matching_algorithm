from utils import NumberValidator, FloatValidator

REQUIREMENT_QUE = [
    {
        'type': 'input',
        'name': 'min_price',
        'message': 'Minimum Price',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'max_price',
        'message': 'Maximum Price',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'min_number_of_bedrooms',
        'message': 'Minimum Number of Bedrooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'max_number_of_bedrooms',
        'message': 'Maximum Number of Bedrooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'min_number_of_bathrooms',
        'message': 'Minimum Number of Bathrooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'max_number_of_bathrooms',
        'message': 'Maximum Number of Bathrooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'latitude',
        'message': 'latitude',
        'validate': FloatValidator,
        'filter': lambda val: float(val)
    },
    {
        'type': 'input',
        'name': 'longitude',
        'message': 'longitude',
        'validate': FloatValidator,
        'filter': lambda val: float(val)
    }
]

PROPERTY_QUE = [
    {
        'type': 'input',
        'name': 'price',
        'message': 'price',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'number_of_bedrooms',
        'message': 'Number of Bedrooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'number_of_bathrooms',
        'message': 'Number of Bathrooms',
        'validate': NumberValidator,
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'latitude',
        'message': 'latitude',
        'validate': FloatValidator,
        'filter': lambda val: float(val)
    },
    {
        'type': 'input',
        'name': 'longitude',
        'message': 'longitude',
        'validate': FloatValidator,
        'filter': lambda val: float(val)
    }
]

PROPERTY_DATA = {
    'VALUES': [
        (41.0473099, 41.0473112, 1000, 1, 1),
        (12.9127356, 77.6380054, 100, 2, 2),
        (44.968046, -94.420307, 101, 3, 1),
        (44.33328, -89.132008, 20, 5, 1),
        (33.755787, -116.359998, 2000, 2, 1),
        (33.844843, -116.54911, 3000, 1, 1),
        (44.92057, -93.44786, 5000, 1, 1)
    ],
    'COLUMN_NAMES': [
        'latitude',
        'longitude',
        'price',
        'number_of_bedrooms',
        'number_of_bathrooms',
    ],
    'table_name': 'Property'
}

REQUIREMENT_DATA = {
    'VALUES': [
        (41.0473099, 41.0473112, 0, 1000, 1, 4, 1, 2),
        (44.240309, -91.493619, 0, 1000, 2, 4, 1, 2),
        (44.968041, -94.419696, 0, 1000, 3, 5, 3, 4),
    ],
    'COLUMN_NAMES': [
        'latitude',
        'longitude',
        'min_price',
        'max_price',
        'min_number_of_bedrooms',
        'max_number_of_bedrooms',
        'min_number_of_bathrooms',
        'max_number_of_bathrooms',
    ],
    'table_name': 'UserRequirement'
}
