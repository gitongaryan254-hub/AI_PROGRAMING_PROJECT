# cipherschool Chat Bot - Deployment Options
# This file contains instructions for deploying your bot with a clean branded web interface

## 🌐 FREE DEPLOYMENT OPTIONS WITH CUSTOM DOMAINS

### Option 1: Render.com (FREE with custom domain)
# 1. Go to https://render.com
# 2. Sign up for free account
# 3. Create new "Web Service"
# 4. Connect your GitHub repository
# 5. Set build command: pip install -r requirements.txt
# 6. Set start command: python fly_app.py
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
gunicorn
"""

## 🔧 MANUAL DEPLOYMENT STEPS

### Step 1: Create requirements.txt
echo "flask" > requirements.txt
echo "gunicorn" >> requirements.txt

### Step 2: Test locally
python fly_app.py

### Step 3: Deploy to chosen platform
# Follow platform-specific instructions above

### Step 4: Add custom domain (optional)
# Purchase domain from Namecheap/GoDaddy (~$10/year)
# Point DNS to your hosting provider

## 📞 SUPPORT
# If you need help with any deployment option, let me know!

## ✅ QUICK NO-CARD DEPLOY (RENDER)

1. Push this project to GitHub (main branch).
2. Go to https://render.com and sign in with GitHub.
3. Click New + -> Blueprint.
4. Select your repository.
5. Render will detect `render.yaml` automatically.
6. Click Apply to create and deploy the free web service.
7. Open the generated URL: `https://<your-service-name>.onrender.com`

### If deploy fails
- Confirm `requirements.txt` contains:
	- flask
	- gunicorn
- Confirm start command in Render service is: `gunicorn fly_app:app`