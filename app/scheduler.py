from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.orm import Session
from datetime import datetime
import random
import logging
from app.database import SessionLocal
from app.models import User, Quote, Message
from app.sms_service import sms_service

logger = logging.getLogger(__name__)


def send_daily_quotes():
    """Send daily motivational quotes to all active users"""
    db: Session = SessionLocal()
    try:
        active_users = db.query(User).filter(User.is_active == True).all()
        quotes = db.query(Quote).all()

        if not quotes:
            logger.warning("No quotes available in database")
            return

        logger.info(f"Sending daily quotes to {len(active_users)} active users")

        for user in active_users:
            # Select a random quote
            quote = random.choice(quotes)

            # Format the message
            message_text = f'"{quote.text}" - {quote.author}'

            # Send SMS
            success, status = sms_service.send_sms(user.phone, message_text)

            # Record the message
            message = Message(
                user_id=user.id,
                quote_id=quote.id,
                sent_at=datetime.utcnow(),
                delivery_status=status
            )
            db.add(message)

            logger.info(f"Quote sent to user {user.id} ({user.phone}): {status}")

        db.commit()
        logger.info("Daily quote delivery completed")

    except Exception as e:
        logger.error(f"Error in send_daily_quotes: {e}")
        db.rollback()
    finally:
        db.close()


def start_scheduler():
    """Initialize and start the background scheduler"""
    scheduler = BackgroundScheduler()

    # Schedule daily quote sending
    # This runs every day at different times based on user preferences
    # For MVP, we'll run a check every hour and send to users whose preferred time has passed
    # In production, you'd want more sophisticated timezone-aware scheduling

    scheduler.add_job(
        send_daily_quotes,
        CronTrigger(hour=9, minute=0),  # Run at 9 AM UTC daily
        id="send_daily_quotes",
        name="Send daily motivational quotes",
        replace_existing=True
    )

    scheduler.start()
    logger.info("Scheduler started successfully")
    return scheduler


def stop_scheduler(scheduler):
    """Stop the scheduler"""
    if scheduler:
        scheduler.shutdown()
        logger.info("Scheduler stopped")
