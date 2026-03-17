import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import instagrapi
import requests
from io import BytesIO

# Get credentials from environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD", "")

class InstagramDownloader:
    def __init__(self):
        """Initialize Instagram client"""
        self.client = instagrapi.Client()
        if INSTAGRAM_USERNAME and INSTAGRAM_PASSWORD:
            try:
                self.client.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
                print("✓ Instagram login successful")
            except Exception as e:
                print(f"⚠ Instagram login failed: {e}")
    
    def extract_reel_id(self, url):
        """Extract reel/post ID from Instagram URL"""
        patterns = [
            r'instagram\.com/reel/([a-zA-Z0-9_-]+)',
            r'instagram\.com/p/([a-zA-Z0-9_-]+)',
            r'instagram\.com/tv/([a-zA-Z0-9_-]+)',
        ]
        
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None
    
    def download_media(self, url):
        """Download Instagram media - works without login for most public content"""
        try:
            media_id = self.extract_reel_id(url)
            if not media_id:
                return None, "Invalid Instagram URL format"
            
            # Try with yt-dlp (most reliable, doesn't require login)
            return self._download_with_ytdlp(url)
        
        except Exception as e:
            return None, f"Error: {str(e)}"
    
    def _download_with_ytdlp(self, url):
        """Download using yt-dlp (no Instagram login needed)"""
        try:
            import yt_dlp
            
            ydl_opts = {
                'format': 'best',
                'quiet': True,
                'no_warnings': True,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                video_url = info['url']
                title = info.get('title', 'reel')
                
                # Download the media
                response = requests.get(video_url, timeout=30)
                if response.status_code == 200:
                    return BytesIO(response.content), title
                else:
                    return None, "Failed to download media"
        
        except ImportError:
            return None, "yt-dlp not installed. Install with: pip install yt-dlp"
        except Exception as e:
            return None, f"Download failed: {str(e)}"


# Initialize downloader
downloader = InstagramDownloader()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send welcome message"""
    welcome_text = """
🎬 **Instagram Reel Downloader Bot**

Simply send me an Instagram reel link and I'll download it for you!

**Supported links:**
- instagram.com/reel/...
- instagram.com/p/... (posts)
- instagram.com/tv/... (IGTV)

**Features:**
✓ Works without login
✓ Fast downloads
✓ Direct download links

**How to use:**
1. Copy an Instagram link
2. Send it to me
3. Get your video! 📥

**Commands:**
/start - Show this menu
/help - Get help
/status - Check bot status

Made with ❤️
    """
    await update.message.reply_text(welcome_text, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send help message"""
    help_text = """
📖 **Help Guide**

**How to use:**
1. Get a link to an Instagram reel/post
2. Send the link to this bot
3. Wait for processing (usually 5-30 seconds)
4. Download the media sent back

**Supported content:**
- Reels (short videos)
- Posts (images/videos)
- IGTV/Stories (some limitations)

**File types returned:**
- MP4 videos (most common)
- MP3 audio (if you need just audio)

**Troubleshooting:**
❌ "Invalid URL" - Make sure it's a valid Instagram link
❌ "Download failed" - Try a public account's post
❌ Slow response - Try again, servers might be busy

**Privacy:**
This bot only downloads public content. No data is stored.
    """
    await update.message.reply_text(help_text, parse_mode="Markdown")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Check bot status"""
    await update.message.reply_text("✅ Bot is online and ready!", parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle incoming messages with Instagram URLs"""
    url = update.message.text.strip()
    
    # Check if it's an Instagram URL
    if "instagram.com" not in url:
        await update.message.reply_text(
            "❌ Please send a valid Instagram link\n\nExamples:\n"
            "- instagram.com/reel/...\n"
            "- instagram.com/p/...",
            parse_mode="Markdown"
        )
        return
    
    # Send processing message
    processing_msg = await update.message.reply_text("⏳ Processing your request...")
    
    try:
        # Download the media
        media_data, title = downloader.download_media(url)
        
        if media_data is None:
            await processing_msg.edit_text(f"❌ {title}")
            return
        
        # Send the downloaded media
        await update.message.reply_video(
            video=media_data,
            caption=f"📥 Downloaded: {title}",
            parse_mode="Markdown"
        )
        
        await processing_msg.delete()
    
    except Exception as e:
        await processing_msg.edit_text(f"❌ Error: {str(e)[:100]}")


async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle errors"""
    print(f"Error: {context.error}")


def main():
    """Start the bot"""
    if not TELEGRAM_TOKEN:
        print("❌ TELEGRAM_BOT_TOKEN environment variable not set!")
        return
    
    # Create application
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("status", status))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)
    
    # Start the bot
    print("🚀 Bot started! Polling for messages...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
