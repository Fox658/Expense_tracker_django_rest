import os

# https://docs.djangoproject.com/en/6.0/topics/db/multi-db/
class ExpTrackerApiDbRouter:

    route_app_labels = {"expense_tracker_api"}

    def db_for_read(self, model, **hints):
        if os.getenv('EXP_TRACKER_ENV') == 'production':
            return 'postgres-prod'
        
        return 'postgres'
    
    def db_for_write(self, model, **hints):
        if os.getenv('EXP_TRACKER_ENV') == 'production':
            return 'postgres-prod'
        
        return 'postgres'

    def allow_relation(self, obj1, obj2, **hints):
        pass

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        pass

