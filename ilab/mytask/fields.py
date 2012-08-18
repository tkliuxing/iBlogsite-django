#-*- coding: utf-8 -*-
from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import simplejson as json
from south.modelsinspector import add_introspection_rules


class JSONField(models.TextField):
    """JSONField is a generic textfield that neatly serializes/unserializes
    JSON objects seamlessly"""

    __metaclass__ = models.SubfieldBase

    def to_python(self, value):
        """Convert our string value to JSON after we load it from the DB"""
        if value == "":
            return None
        try:
            if isinstance(value, basestring):
                return json.loads(value, cls=DjangoJSONDecoder)
        except ValueError:
            pass
        return value

    def get_db_prep_save(self, value, connection=None):
        """Convert our JSON object to a string before we save"""
        if value == "":
            return None
        if isinstance(value, dict):
            value = json.dumps(value, cls=DjangoJSONEncoder)
        return super(JSONField, self).get_db_prep_save(value, connection=connection)

add_introspection_rules([([JSONField], [], {},), ], ["^ilab\.mytask\.fields\.JSONField"])
