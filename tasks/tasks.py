from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


@shared_task
def send_email_task(subject, message, email):
    logger.info(f"Enviando correo a {email}...")
    try:
        send_mail(
            subject,
            message,
            "jesusroblesduana@gmail.com",
            [email],
            fail_silently=False,
        )
        logger.info(f"Correo enviado a {email} exitosamente.")
    except Exception as e:
        logger.error("Exception: ", e)
