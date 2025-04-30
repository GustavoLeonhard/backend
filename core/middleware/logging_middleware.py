import logging
from django.utils import timezone
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Log the request
        logger.info(
            f"Request: {request.method} {request.path} - "
            f"User: {request.user.username if request.user.is_authenticated else 'Anonymous'} - "
            f"IP: {request.META.get('REMOTE_ADDR')} - "
            f"Time: {timezone.now()}"
        )

        response = self.get_response(request)

        # Log the response
        logger.info(
            f"Response: {request.method} {request.path} - "
            f"Status: {response.status_code} - "
            f"Time: {timezone.now()}"
        )

        return response

@receiver(post_save)
def log_model_save(sender, instance, created, **kwargs):
    if sender.__module__ == 'core.models':
        action = "created" if created else "updated"
        logger.info(
            f"Model {action}: {sender.__name__} - "
            f"ID: {instance.id} - "
            f"User: {instance._current_user.username if hasattr(instance, '_current_user') else 'Unknown'} - "
            f"Time: {timezone.now()}"
        )

@receiver(post_delete)
def log_model_delete(sender, instance, **kwargs):
    if sender.__module__ == 'core.models':
        logger.info(
            f"Model deleted: {sender.__name__} - "
            f"ID: {instance.id} - "
            f"User: {instance._current_user.username if hasattr(instance, '_current_user') else 'Unknown'} - "
            f"Time: {timezone.now()}"
        ) 