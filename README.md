# 🎬 Instagram Reel Downloader Telegram Bot

A Telegram bot that downloads Instagram reels, posts, and videos directly. Send a link, get your media!

## ✨ Features

- ✅ Download Instagram reels, posts, and IGTV
- ✅ No login required (works on public content)
- ✅ Fast & reliable (uses yt-dlp)
- ✅ Direct video sending via Telegram
- ✅ Simple one-click usage
- ✅ Works 24/7 on cloud servers

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/instagram-reel-bot.git
cd instagram-reel-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Get Your Telegram Bot Token

1. Open Telegram and search for **@BotFather**
2. Send `/start` command
3. Send `/newbot` to create a new bot
4. Follow the prompts (give it a name)
5. Copy the **API Token** (example: `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11`)

### 4. Setup Environment

```bash
# Copy the example env file
cp .env.example .env

# Edit .env and add your Telegram token
nano .env
```

Add this line:
```
TELEGRAM_BOT_TOKEN=YOUR_TOKEN_HERE
```

### 5. Run the Bot

```bash
python instagram_reel_bot.py
```

You should see:
```
✓ Bot started! Polling for messages...
```

## 🎯 How to Use

### In Telegram:

1. **Search for your bot** by its name
2. **Send any Instagram link:**
   ```
   instagram.com/reel/ABC123...
   instagram.com/p/XYZ789...
   ```
3. **Wait 5-30 seconds** for download
4. **Get your video!** Download directly

### Supported Links

| Type | Example | Support |
|------|---------|---------|
| Reels | `instagram.com/reel/ABC123...` | ✅ Full |
| Posts | `instagram.com/p/XYZ789...` | ✅ Full |
| IGTV | `instagram.com/tv/ABC123...` | ✅ Full |
| Stories | `instagram.com/stories/...` | ⚠️ Limited |

## 🌐 Deploy on Cloud (Free Options)

### Option 1: Heroku (Free - Limited)
Heroku free tier is ending. Consider alternatives.

### Option 2: Render (Recommended)

1. **Push to GitHub**
2. **Go to [render.com](https://render.com)**
3. **Create new Web Service**
4. **Connect your GitHub repo**
5. **Set Environment Variables** (your .env contents)
6. **Deploy!**

Free tier includes:
- Always running services
- No card needed
- Good uptime

### Option 3: Railway.app

1. Push to GitHub
2. Go to [railway.app](https://railway.app)
3. New Project → GitHub Repo
4. Add environment variables
5. Deploy!

### Option 4: PythonAnywhere (Cheap)

1. Upload files to PythonAnywhere
2. Create a console
3. Run Python script
4. Keep console running (free account limitation)

### Option 5: AWS Lambda + API Gateway (Advanced)

For serverless deployment, see `deploy/lambda-deployment.md`

## 📁 Project Structure

```
instagram-reel-bot/
├── instagram_reel_bot.py      # Main bot code
├── requirements.txt            # Python dependencies
├── .env.example               # Environment variables template
├── .env                       # Your credentials (git-ignored)
├── .gitignore                 # Ignore sensitive files
├── README.md                  # This file
└── deploy/
    └── docker-compose.yml     # Optional: Docker setup
```

## 🔧 Configuration Options

### Advanced Setup (Optional)

```python
# In instagram_reel_bot.py, modify:
DOWNLOAD_TIMEOUT = 30      # Increase for slow connections
MAX_VIDEO_SIZE = 50 * 1024 * 1024  # 50MB limit
```

## 🐛 Troubleshooting

### ❌ "Invalid URL" Error

```
Solution: Make sure the Instagram link is complete
❌ Wrong: instagram.com/reel
✅ Right: instagram.com/reel/ABC123XYZ
```

### ❌ "Download Failed" Error

```
Common causes:
1. Private account → Add Instagram credentials to .env
2. Deleted post → Link no longer exists
3. Rate limited → Wait 30 minutes before retrying
4. Network issue → Check your internet
```

### ❌ Bot not responding

```bash
# Check if bot is running
ps aux | grep instagram_reel_bot.py

# Check for errors in console
# Make sure TELEGRAM_BOT_TOKEN is set correctly
echo $TELEGRAM_BOT_TOKEN
```

### ❌ "yt-dlp not installed"

```bash
pip install --upgrade yt-dlp
```

## 📊 How It Works

```
User sends link
    ↓
Bot validates URL
    ↓
yt-dlp downloads from Instagram
    ↓
Bot sends video to Telegram
    ↓
User downloads from Telegram
```

## ⚡ Performance Tips

1. **Use yt-dlp** (included) - Most reliable
2. **Run on VPS** - Faster than laptop
3. **Check rate limits** - Instagram has limits
4. **Parallel requests** - Bot handles multiple users

## 🔐 Security & Privacy

- ✅ No data stored on server
- ✅ No login information stored
- ✅ Works only on public content
- ✅ Each download is independent
- ✅ Tokens stored in .env (git-ignored)

### Best Practices:

```bash
# Always add to .gitignore
echo ".env" >> .gitignore

# Never commit credentials
git add .
git commit -m "Initial commit"

# Use environment variables
export TELEGRAM_BOT_TOKEN="your_token"
```

## 📝 Environment Variables Reference

| Variable | Required | Example |
|----------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Yes | `123456:ABC-DEF...` |
| `INSTAGRAM_USERNAME` | No | `your_instagram_handle` |
| `INSTAGRAM_PASSWORD` | No | `your_password` |

## 🚀 Advanced Usage

### Custom Download Path

```python
# Modify instagram_reel_bot.py
DOWNLOAD_PATH = "/tmp/downloads"
```

### Add Webhooks (Instead of Polling)

Replace polling with webhooks for better performance. See `advanced/webhook-setup.md`

### Database Integration

Store download history:

```python
import sqlite3
db = sqlite3.connect('downloads.db')
# Log each download with timestamp
```

## 📦 Docker Deployment

```bash
docker build -t insta-bot .
docker run -e TELEGRAM_BOT_TOKEN=your_token insta-bot
```

See `deploy/Dockerfile` for details.

## 🤝 Contributing

Pull requests welcome! Areas for improvement:

- [ ] Audio extraction (MP3 from reels)
- [ ] Batch downloads
- [ ] Download history
- [ ] Statistics dashboard
- [ ] Rate limit handling
- [ ] Queue system for large files

## 📄 License

MIT License - see LICENSE file

## ⚠️ Disclaimer

- This tool is for **personal use only**
- Respect Instagram's Terms of Service
- Don't download copyrighted content without permission
- Use responsibly

## 🎓 Learning Resources

- [Telegram Bot API Docs](https://core.telegram.org/bots/api)
- [python-telegram-bot Docs](https://python-telegram-bot.readthedocs.io/)
- [yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp)
- [Instagram API Limitations](https://help.instagram.com/instagram-api)

## 📧 Support

- Open an **Issue** on GitHub
- Check **Discussions** for common problems
- Read the **Wiki** for advanced topics

## 🌟 If You Like This

Give it a star! ⭐

Follow for more projects on GitHub

---

**Happy downloading!** 🎉

Made with ❤️ by the community
