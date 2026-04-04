# C!pher School Bot - Deployment Options
# This file contains instructions for deploying your bot with custom names

## 🌐 FREE DEPLOYMENT OPTIONS WITH CUSTOM DOMAINS

### Option 1: Render.com (FREE with custom domain)
# 1. Go to https://render.com
# 2. Sign up for free account
# 3. Create new "Web Service"
# 4. Connect your GitHub repository
# 5. Set build command: pip install -r requirements.txt
# 6. Set start command: python public_bot.py
# 7. Deploy!
# 8. Add custom domain: cipherschoolbot.com (purchase domain separately)

### Option 2: Railway.app (FREE tier)
# 1. Go to https://railway.app
# 2. Connect GitHub
# 3. Deploy automatically
# 4. Get free railway.app subdomain
# 5. Add custom domain in settings

### Option 3: Fly.io (FREE tier)
# 1. Install flyctl: iwr https://fly.io/install.ps1 -useb | iex
# 2. fly launch
# 3. fly deploy
# 4. Get free fly.dev subdomain

### Option 4: Vercel (FREE)
# 1. Go to https://vercel.com
# 2. Import GitHub repo
# 3. Set build command for Python
# 4. Deploy with vercel.app subdomain

## 📋 REQUIREMENTS.TXT for deployment
"""
flask
pyngrok
"""

## 🚀 QUICK START WITH NGRok (Free)
# Run: python public_bot.py
# Get a temporary public URL instantly

## 💎 PAID OPTIONS FOR CUSTOM SUBDOMAIN
# 1. Ngrok Paid Plan ($5/month): cipherschoolbot.ngrok.io
# 2. Custom domain ($10-15/year): cipherschoolbot.com
# 3. Cloudflare Pages + Functions (Free tier)

## 🔧 MANUAL DEPLOYMENT STEPS

### Step 1: Create requirements.txt
echo "flask" > requirements.txt
echo "pyngrok" >> requirements.txt

### Step 2: Test locally
python public_bot.py

### Step 3: Deploy to chosen platform
# Follow platform-specific instructions above

### Step 4: Add custom domain (optional)
# Purchase domain from Namecheap/GoDaddy (~$10/year)
# Point DNS to your hosting provider

## 📞 SUPPORT
# If you need help with any deployment option, let me know!