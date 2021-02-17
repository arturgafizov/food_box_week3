from django.apps import AppConfig


class ItemsConfig(AppConfig):
    name = 'items'

    def ready(self):
        import food_box.items.signals.handlers # noqa
