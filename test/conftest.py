from marshmallow import Schema, fields
from marshmallow.class_registry import _registry

import pytest
from marshmallow_annotations.registry import DefaultTypeRegistry


# testing the converter means creating a scheme to test with it
# the behavior of marshmallow is to place a reference into
# a dict to do name based lookups for Nested (etc) however
# this can be irksome when creating multiple schema with the same name
@pytest.fixture(autouse=True)
def clear_registry():
    yield
    _registry.clear()


@pytest.fixture
def registry():
    yield DefaultTypeRegistry()


@pytest.fixture
def scheme():

    class ConverterTestScheme(Schema):
        id = fields.Integer()
        name = fields.String()

    yield ConverterTestScheme
