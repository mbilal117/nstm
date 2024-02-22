from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'nstm.apps.accounts'

    def ready(self):
        try:
            import nstm.apps.accounts.signals  # noqa F401
        except ImportError:
            pass
