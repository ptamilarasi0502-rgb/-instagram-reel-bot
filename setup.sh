#!/bin/bash

echo "🎬 Instagram Reel Downloader Bot - Setup Script"
echo "=============================================="
echo ""

# Check Python version
python_version=$(python3 --version 2>&1)
echo "✓ Python found: $python_version"

# Create virtual environment
echo ""
echo "📦 Creating virtual environment..."
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Create .env file
if [ ! -f .env ]; then
    echo ""
    echo "🔐 Setting up environment variables..."
    cp .env.example .env
    
    echo ""
    echo "❗ IMPORTANT:"
    echo "1. Get your bot token from @BotFather on Telegram"
    echo "2. Edit the .env file and add: TELEGRAM_BOT_TOKEN=your_token_here"
    echo ""
    echo "   nano .env"
    echo ""
else
    echo "✓ .env file already exists"
fi

echo ""
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit .env file: nano .env"
echo "2. Add your TELEGRAM_BOT_TOKEN"
echo "3. Run the bot: python instagram_reel_bot.py"
echo ""
echo "To activate venv in future:"
echo "   source venv/bin/activate"
echo ""
