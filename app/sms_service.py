from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from app.config import get_settings
import logging

logger = logging.getLogger(__name__)
settings = get_settings()


class SMSService:
    def __init__(self):
        self.client = None
        if settings.twilio_account_sid and settings.twilio_auth_token:
            try:
                self.client = Client(
                    settings.twilio_account_sid,
                    settings.twilio_auth_token
                )
            except Exception as e:
                logger.error(f"Failed to initialize Twilio client: {e}")

    def send_sms(self, to_phone: str, message: str) -> tuple[bool, str]:
        """
        Send SMS via Twilio
        Returns: (success: bool, status: str)
        """
        if not self.client:
            logger.warning("Twilio client not initialized. SMS not sent.")
            return False, "failed"

        try:
            message_obj = self.client.messages.create(
                body=message,
                from_=settings.twilio_phone_number,
                to=to_phone
            )
            logger.info(f"SMS sent to {to_phone}, SID: {message_obj.sid}")
            return True, "sent"
        except TwilioRestException as e:
            logger.error(f"Failed to send SMS to {to_phone}: {e}")
            return False, "failed"
        except Exception as e:
            logger.error(f"Unexpected error sending SMS to {to_phone}: {e}")
            return False, "failed"


# Singleton instance
sms_service = SMSService()
