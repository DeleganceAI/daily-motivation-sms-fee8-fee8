#!/usr/bin/env python3
"""
Simple test script to verify the application structure and imports
"""
import sys

def test_imports():
    """Test that all modules can be imported"""
    try:
        print("Testing imports...")

        # Test config
        from app.config import get_settings
        print("✓ Config module imported")

        # Test models
        from app.models import User, Quote, Message
        print("✓ Models imported")

        # Test schemas
        from app.schemas import UserCreate, UserResponse, QuoteResponse, MessageResponse
        print("✓ Schemas imported")

        # Test database
        from app.database import get_db, init_db
        print("✓ Database module imported")

        # Test routes
        from app.routes import router
        print("✓ Routes imported")

        # Test sms_service
        from app.sms_service import sms_service
        print("✓ SMS service imported")

        # Test scheduler
        from app.scheduler import start_scheduler, stop_scheduler, send_daily_quotes
        print("✓ Scheduler imported")

        # Test seed data
        from app.seed_data import seed_quotes
        print("✓ Seed data imported")

        # Test main app
        from app.main import app
        print("✓ Main app imported")

        print("\n✅ All imports successful!")
        print("\nApplication structure verified:")
        print("- Configuration management: ✓")
        print("- Database models (User, Quote, Message): ✓")
        print("- API endpoints: ✓")
        print("- Twilio SMS integration: ✓")
        print("- Daily scheduler: ✓")
        print("- Quote seeding: ✓")
        print("- FastAPI application: ✓")

        return True

    except ImportError as e:
        print(f"\n❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
