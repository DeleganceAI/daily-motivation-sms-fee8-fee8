# Infinifab MVP

A daily motivational quotes SMS service built with FastAPI, SQLite, and Twilio.

## Features

- User registration with phone number
- Daily SMS delivery at user-specified times
- Motivational quote database (20+ quotes)
- User preference management (timezone, preferred time)
- SMS delivery tracking
- RESTful API with automatic documentation

## Tech Stack

- **Backend**: Python 3.9+ with FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **SMS**: Twilio SMS API
- **Scheduler**: APScheduler for daily message delivery
- **Deployment**: Railway (recommended)

## Project Structure

```
infinifab/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── database.py          # Database setup
│   ├── models.py            # SQLAlchemy models
│   ├── schemas.py           # Pydantic schemas
│   ├── routes.py            # API endpoints
│   ├── sms_service.py       # Twilio SMS integration
│   ├── scheduler.py         # APScheduler for daily SMS
│   └── seed_data.py         # Initial quote data
├── docs/
│   ├── design.md
│   ├── tech-spec.md
│   └── implementation-guide.md
├── main.py                  # Application entry point
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── railway.toml            # Railway deployment config
└── README.md

```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd infinifab
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your Twilio credentials:

```env
TWILIO_ACCOUNT_SID=your_account_sid_here
TWILIO_AUTH_TOKEN=your_auth_token_here
TWILIO_PHONE_NUMBER=+1234567890
DATABASE_URL=sqlite:///./infinifab.db
API_HOST=0.0.0.0
API_PORT=8000
```

### 4. Run the Application

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### 5. Access API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Users

- `POST /api/users` - Register a new user
- `GET /api/users` - List all users
- `GET /api/users/{user_id}` - Get user details
- `PUT /api/users/{user_id}` - Update user preferences
- `DELETE /api/users/{user_id}` - Delete a user

### Quotes

- `GET /api/quotes` - List all quotes
- `GET /api/quotes/{quote_id}` - Get a specific quote

### Messages

- `GET /api/messages` - List message history
- `GET /api/messages?user_id={user_id}` - Filter messages by user

### System

- `GET /` - Root endpoint
- `GET /health` - Health check

## Usage Examples

### Register a User

```bash
curl -X POST "http://localhost:8000/api/users" \
  -H "Content-Type: application/json" \
  -d '{
    "phone": "+1234567890",
    "timezone": "America/New_York",
    "preferred_time": "09:00"
  }'
```

### Update User Preferences

```bash
curl -X PUT "http://localhost:8000/api/users/1" \
  -H "Content-Type: application/json" \
  -d '{
    "preferred_time": "08:00",
    "is_active": true
  }'
```

### List All Quotes

```bash
curl "http://localhost:8000/api/quotes"
```

## Daily SMS Scheduler

The application includes a background scheduler that sends daily motivational quotes:

- **Schedule**: Runs daily at 9:00 AM UTC (configurable in `app/scheduler.py`)
- **Process**:
  1. Fetches all active users
  2. Selects a random quote for each user
  3. Sends SMS via Twilio
  4. Records delivery status in database

## Deployment to Railway

### Prerequisites

- Railway account (https://railway.app)
- GitHub repository

### Steps

1. **Push code to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Create new Railway project**:
   - Go to Railway dashboard
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure environment variables**:
   - Add all variables from `.env` to Railway settings
   - Railway will automatically set `PORT` variable

4. **Deploy**:
   - Railway will automatically build and deploy
   - Your API will be available at the provided Railway URL

## Database

The application uses SQLite for simplicity. On first run, it will:
1. Create the database file (`infinifab.db`)
2. Create all tables (users, quotes, messages)
3. Seed 20 motivational quotes

## Twilio Setup

To use SMS functionality:

1. Create a Twilio account at https://www.twilio.com
2. Get a phone number from Twilio Console
3. Copy your Account SID and Auth Token
4. Add credentials to `.env` file

**Note**: Without Twilio credentials, the API will still work but SMS sending will be disabled (logged as warnings).

## Development

### Run in Development Mode

```bash
python main.py
```

The server will reload automatically on code changes.

### Run with Uvicorn Directly

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Testing

You can test the API using:
- The interactive Swagger UI at `/docs`
- curl commands (see examples above)
- API clients like Postman or Insomnia

## Troubleshooting

### SMS Not Sending

- Verify Twilio credentials in `.env`
- Check phone number format (must include country code, e.g., +1234567890)
- Review application logs for error messages

### Database Errors

- Delete `infinifab.db` and restart to reset database
- Check file permissions in the application directory

### Scheduler Not Running

- Check logs for scheduler startup messages
- Verify APScheduler is properly initialized in `app/main.py`

## MVP Scope

This MVP includes:
- ✅ User registration with phone number
- ✅ Daily SMS sending at user-specified times
- ✅ Motivational quote database
- ✅ User preference settings
- ✅ Basic authentication
- ✅ SMS delivery tracking

Out of scope for MVP:
- ❌ Mobile app
- ❌ Advanced analytics
- ❌ Premium quote categories
- ❌ Social features
- ❌ Payment processing

## Project Documentation

- [Design Document](docs/design.md) - Market research and business context
- [Technical Specification](docs/tech-spec.md) - MVP requirements and data models
- [Implementation Guide](docs/implementation-guide.md) - Libraries, patterns, and setup

---

*Built with [Infinifab](https://infinifab.com)*
