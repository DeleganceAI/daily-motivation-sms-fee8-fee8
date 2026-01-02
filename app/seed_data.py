from sqlalchemy.orm import Session
from app.models import Quote


def seed_quotes(db: Session):
    """Seed the database with initial motivational quotes"""
    existing = db.query(Quote).first()
    if existing:
        return  # Already seeded

    quotes = [
        {
            "text": "The only way to do great work is to love what you do.",
            "author": "Steve Jobs",
            "category": "motivation"
        },
        {
            "text": "Believe you can and you're halfway there.",
            "author": "Theodore Roosevelt",
            "category": "motivation"
        },
        {
            "text": "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "author": "Winston Churchill",
            "category": "perseverance"
        },
        {
            "text": "The future belongs to those who believe in the beauty of their dreams.",
            "author": "Eleanor Roosevelt",
            "category": "inspiration"
        },
        {
            "text": "It does not matter how slowly you go as long as you do not stop.",
            "author": "Confucius",
            "category": "perseverance"
        },
        {
            "text": "Everything you've ever wanted is on the other side of fear.",
            "author": "George Addair",
            "category": "courage"
        },
        {
            "text": "Believe in yourself. You are braver than you think, more talented than you know, and capable of more than you imagine.",
            "author": "Roy T. Bennett",
            "category": "self-belief"
        },
        {
            "text": "I learned that courage was not the absence of fear, but the triumph over it.",
            "author": "Nelson Mandela",
            "category": "courage"
        },
        {
            "text": "The only impossible journey is the one you never begin.",
            "author": "Tony Robbins",
            "category": "motivation"
        },
        {
            "text": "Your limitation—it's only your imagination.",
            "author": "Unknown",
            "category": "inspiration"
        },
        {
            "text": "Great things never come from comfort zones.",
            "author": "Unknown",
            "category": "growth"
        },
        {
            "text": "Dream it. Wish it. Do it.",
            "author": "Unknown",
            "category": "motivation"
        },
        {
            "text": "Success doesn't just find you. You have to go out and get it.",
            "author": "Unknown",
            "category": "motivation"
        },
        {
            "text": "The harder you work for something, the greater you'll feel when you achieve it.",
            "author": "Unknown",
            "category": "perseverance"
        },
        {
            "text": "Don't stop when you're tired. Stop when you're done.",
            "author": "Unknown",
            "category": "perseverance"
        },
        {
            "text": "Wake up with determination. Go to bed with satisfaction.",
            "author": "Unknown",
            "category": "motivation"
        },
        {
            "text": "Do something today that your future self will thank you for.",
            "author": "Unknown",
            "category": "inspiration"
        },
        {
            "text": "Little things make big days.",
            "author": "Unknown",
            "category": "inspiration"
        },
        {
            "text": "It's going to be hard, but hard does not mean impossible.",
            "author": "Unknown",
            "category": "perseverance"
        },
        {
            "text": "Don't wait for opportunity. Create it.",
            "author": "Unknown",
            "category": "motivation"
        }
    ]

    for quote_data in quotes:
        quote = Quote(**quote_data)
        db.add(quote)

    db.commit()
