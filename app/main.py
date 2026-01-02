from fastapi import FastAPI
from contextlib import asynccontextmanager
import logging
from app.database import init_db, SessionLocal
from app.routes import router
from app.scheduler import start_scheduler, stop_scheduler
from app.seed_data import seed_quotes

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Global scheduler instance
scheduler = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    global scheduler

    # Startup
    logger.info("Starting Infinifab API...")
    init_db()
    logger.info("Database initialized")

    # Seed quotes
    db = SessionLocal()
    try:
        seed_quotes(db)
        logger.info("Quotes seeded")
    finally:
        db.close()

    # Start scheduler
    scheduler = start_scheduler()
    logger.info("Application started successfully")

    yield

    # Shutdown
    logger.info("Shutting down...")
    stop_scheduler(scheduler)


app = FastAPI(
    title="Infinifab API",
    description="Daily motivational quotes via SMS",
    version="1.0.0",
    lifespan=lifespan
)

# Include routes
app.include_router(router, prefix="/api", tags=["api"])


@app.get("/")
def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Infinifab API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}
