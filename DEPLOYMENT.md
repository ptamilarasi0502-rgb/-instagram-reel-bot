# 🌐 Cloud Deployment Guide

## Deployment Options Comparison

| Platform | Cost | Ease | Always Running |
|----------|------|------|-----------------|
| Render | Free | ⭐⭐⭐⭐⭐ | ✅ |
| Railway | $5/mo | ⭐⭐⭐⭐ | ✅ |
| Replit | Free (limited) | ⭐⭐⭐⭐⭐ | ❌ |
| PythonAnywhere | Free | ⭐⭐⭐ | ❌ |
| DigitalOcean | $5/mo | ⭐⭐⭐ | ✅ |
| AWS Lambda | Free tier | ⭐⭐ | ⚠️ |

---

## 🎯 Recommended: Render.com (Free & Reliable)

### Step 1: Prepare Your GitHub Repo

```bash
# Initialize git if needed
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Create repo on GitHub
# Then push:
git remote add origin https://github.com/yourusername/instagram-reel-bot.git
git branch -M main
git push -u origin main
```

### Step 2: Create Render Account

1. Go to [render.com](https://render.com)
2. Sign up with GitHub (easiest)
3. Grant permissions

### Step 3: Create New Web Service

1. Click "New +" → "Web Service"
2. Connect your GitHub repo
3. Select the `instagram-reel-bot` repository

### Step 4: Configure Settings

| Setting | Value |
|---------|-------|
| **Name** | instagram-reel-bot |
| **Environment** | Python 3 |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `python instagram_reel_bot.py` |
| **Region** | Choose closest to you |
| **Instance Type** | Free |

### Step 5: Add Environment Variables

1. Scroll down to "Environment"
2. Click "Add Environment Variable"
3. Add these:

```
TELEGRAM_BOT_TOKEN = your_bot_token_here
INSTAGRAM_USERNAME = (optional)
INSTAGRAM_PASSWORD = (optional)
```

### Step 6: Deploy!

1. Click "Create Web Service"
2. Wait for deployment (2-3 minutes)
3. Check logs for "Bot started! Polling for messages..."

✅ **Your bot is now running 24/7!**

---

## 🚂 Alternative: Railway.app

### Step 1-2: Same as Render (GitHub setup)

### Step 3: Create New Project

1. Go to [railway.app](https://railway.app)
2. New Project → GitHub Repo
3. Select your repository

### Step 4: Add Variables

In the "Variables" tab:
```
TELEGRAM_BOT_TOKEN=your_token
```

### Step 5: Deploy

Deploy button → Wait for deployment

**Cost:** ~$5-10/month after free credits

---

## 💻 DIY: DigitalOcean Droplet ($5/month)

### Step 1: Create Droplet

1. Go to [digitalocean.com](https://digitalocean.com)
2. Create Droplet → Ubuntu 22.04
3. $5/month plan
4. Choose region nearest to you

### Step 2: SSH into Droplet

```bash
ssh root@your_droplet_ip
```

### Step 3: Install Dependencies

```bash
apt update
apt install -y python3-pip python3-venv git ffmpeg

# Clone your repo
git clone https://github.com/yourusername/instagram-reel-bot.git
cd instagram-reel-bot

# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 4: Setup Environment

```bash
nano .env
# Add your TELEGRAM_BOT_TOKEN

# Make script executable
chmod +x setup.sh
```

### Step 5: Run with Systemd (Auto-restart)

Create `/etc/systemd/system/instagram-bot.service`:

```ini
[Unit]
Description=Instagram Reel Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/instagram-reel-bot
Environment="PATH=/root/instagram-reel-bot/venv/bin"
ExecStart=/root/instagram-reel-bot/venv/bin/python instagram_reel_bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
systemctl daemon-reload
systemctl enable instagram-bot
systemctl start instagram-bot

# Check status
systemctl status instagram-bot

# View logs
journalctl -u instagram-bot -f
```

---

## 🎮 Free but Limited: Replit

### Step 1: Import Repo

1. Go to [replit.com](https://replit.com)
2. "Import from GitHub" → Your repo

### Step 2: Add Secrets

1. Click "Secrets" (lock icon)
2. Add `TELEGRAM_BOT_TOKEN`

### Step 3: Run

Click "Run" button

⚠️ **Limitation:** Replit keeps free apps sleeping after 5 minutes of inactivity. Use paid tier ($7/month) for always-running

---

## 🔄 Keeping Everything Updated

### Auto-update from GitHub

Create `auto-update.sh`:

```bash
#!/bin/bash
cd /root/instagram-reel-bot
git pull origin main
systemctl restart instagram-bot
```

Schedule with cron:
```bash
# Every day at 2 AM
0 2 * * * /root/instagram-reel-bot/auto-update.sh
```

---

## 📊 Monitoring & Logs

### On Render
- Logs tab shows real-time output
- Notifications for crashes

### On DigitalOcean
```bash
journalctl -u instagram-bot -f --lines=50
```

### On Railway
- Logs tab in dashboard
- Error alerts

---

## 🔍 Troubleshooting Deployments

### Bot not responding?

```bash
# Check if running
systemctl status instagram-bot

# Restart
systemctl restart instagram-bot

# View errors
journalctl -u instagram-bot -n 50
```

### Token issues?

```bash
# Verify token is set
echo $TELEGRAM_BOT_TOKEN

# Should NOT be empty
```

### Out of memory?

Use lighter library (already using yt-dlp which is efficient)

---

## 💰 Cost Summary

| Platform | Monthly Cost | Setup Time |
|----------|--------------|-----------|
| Render | $0 | 10 min |
| Railway | $5 | 10 min |
| DigitalOcean | $5 | 20 min |
| Replit Pro | $7 | 5 min |

**Recommendation:** Start with Render (free), upgrade to Railway/DigitalOcean if needed.

---

## 🆘 Getting Help

1. Check logs first
2. Verify token is correct
3. Test locally with `python instagram_reel_bot.py`
4. Open GitHub issue with error message

Good luck! 🚀
