from flask.views import MethodView
from . import mixins


class CreateAPIView(mixins.CreateMixin, MethodView):
    """
    Concrete view for creating a model instance.
    """
    methods = ['POST']

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)


class ListAPIView(mixins.ListMixin, MethodView):
    """
    Concrete view for listing a queryset.
    """
    methods = ['GET']

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)


class RetrieveAPIView(mixins.RetrieveMixin, MethodView):
    """
    Concrete view for retrieving a model instance.
    """
    methods = ['GET']

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)


class DestroyAPIView(mixins.DeleteMinxin, MethodView):
    """
    Concrete view for deleting a model instance.
    """
    methods = ['DELETE']

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)


class UpdateAPIView(mixins.UpdateMixin, MethodView):
    """
    Concrete view for updating a model instance.
    """
    methods = ['PUT', 'PATCH']

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.partial_update(*args, **kwargs)


class OptionsAPIView(mixins.OptionsMixin, MethodView):
    """
    Concrete view for updating a model instance.
    """
    methods = ['OPTIONS']

    def options(self, *args, **kwargs):
        return self.cors_preflight(*args, **kwargs)


class ListCreateAPIView(mixins.ListMixin, mixins.CreateMixin, mixins.OptionsMixin, MethodView):
    """
    Concrete view for listing a queryset or creating a model instance.
    """
    methods = ['GET', 'POST', 'OPTIONS']

    def get(self, *args, **kwargs):
        return self.list(*args, **kwargs)

    def post(self, *args, **kwargs):
        return self.create(*args, **kwargs)

    def options(self, *args, **kwargs):
        return self.cors_preflight(*args, **kwargs)


class RetrieveUpdateAPIView(mixins.RetrieveMixin, mixins.UpdateMixin, mixins.OptionsMixin, MethodView):
    """
    Concrete view for retrieving, updating a model instance.
    """
    methods = ['GET', 'PUT', 'PATCH', 'OPTIONS']

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.partial_update(*args, **kwargs)

    def options(self, *args, **kwargs):
        return self.cors_preflight(*args, **kwargs)


class RetrieveDestroyAPIView(mixins.RetrieveMixin, mixins.DeleteMinxin, mixins.OptionsMixin, MethodView):
    """
    Concrete view for retrieving or deleting a model instance.
    """
    methods = ['GET', 'DELETE', 'OPTIONS']

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)

    def options(self, *args, **kwargs):
        return self.cors_preflight(*args, **kwargs)


class RetrieveUpdateDestroyAPIView(mixins.RetrieveMixin, mixins.UpdateMixin, mixins.DeleteMinxin, mixins.OptionsMixin, MethodView):
    """
    Concrete view for retrieving, updating or deleting a model instance.
    """
    methods = ['GET', 'PUT', 'PATCH', 'DELETE', 'OPTIONS']

    def get(self, *args, **kwargs):
        return self.retrieve(*args, **kwargs)

    def put(self, *args, **kwargs):
        return self.update(*args, **kwargs)

    def patch(self, *args, **kwargs):
        return self.partial_update(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.destroy(*args, **kwargs)

    def options(self, *args, **kwargs):
        return self.cors_preflight(*args, **kwargs)
