# 🚀 QUICK DEPLOYMENT GUIDE

## ✅ Step 1: GitHub (COMPLETED!)
Your code is now at: https://github.com/Anurag02012004/College-ChatBot

---

## 🖥️ Step 2: Deploy Backend to Render (FREE)

### Why Render?
- ✅ Free tier available
- ✅ Auto-deploys from GitHub
- ✅ Supports Python/Flask
- ✅ Easy setup with `render.yaml`

### Steps:

1. **Go to Render**
   - Visit: https://render.com
   - Click "Get Started" or "Sign In"
   - Sign in with your GitHub account

2. **Create New Web Service**
   - Click "New +" button (top right)
   - Select "Web Service"

3. **Connect Repository**
   - Click "Connect account" for GitHub
   - Search for `College-ChatBot`
   - Click "Connect"

4. **Configure Service** (Render auto-detects from render.yaml)
   - Name: `college-chatbot` (or your choice)
   - Region: `Oregon` (or nearest)
   - Branch: `main`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: `Free`

5. **Deploy!**
   - Click "Create Web Service"
   - Wait 5-10 minutes for first deployment
   - You'll get a URL like: `https://college-chatbot.onrender.com`

6. **Test Your Backend**
   ```bash
   curl https://your-app-name.onrender.com/api/health
   ```

---

## 🌐 Step 3: Deploy Frontend to Netlify (FREE)

### Why Netlify?
- ✅ Free tier with unlimited bandwidth
- ✅ Perfect for static sites
- ✅ Global CDN
- ✅ Auto-deploys from GitHub

### Steps:

1. **Update Frontend with Backend URL**
   - Edit: `static-frontend/index.html`
   - Find line: `const API_URL = window.location.origin;`
   - Change to: `const API_URL = 'https://YOUR-RENDER-URL.onrender.com';`
   - Example: `const API_URL = 'https://college-chatbot.onrender.com';`

2. **Commit & Push Changes**
   ```bash
   cd /Users/anurag/Desktop/college-chat-bot
   git add static-frontend/index.html
   git commit -m "Update API URL for production"
   git push origin main
   ```

3. **Go to Netlify**
   - Visit: https://app.netlify.com
   - Sign in with GitHub

4. **Create New Site**
   - Click "Add new site"
   - Select "Import an existing project"
   - Choose "Deploy with GitHub"
   - Select `College-ChatBot` repository

5. **Configure Build Settings**
   - Base directory: `static-frontend`
   - Build command: (leave empty)
   - Publish directory: `.` (or leave as default)
   - Click "Deploy site"

6. **Update Site Name (Optional)**
   - Go to Site settings → Change site name
   - Choose something like: `iiit-kalyani-chatbot`
   - Your URL: `https://iiit-kalyani-chatbot.netlify.app`

---

## ⚡ Alternative: Deploy Both on Render

If you prefer one platform:

1. **Deploy Backend** (as above)
2. **Serve Frontend from Flask**
   - No need for Netlify
   - Your Flask app already serves the frontend
   - Just use: `https://your-app.onrender.com`

---

## 🧪 Testing Your Deployment

### Test Backend (Render)
```bash
# Health check
curl https://your-app.onrender.com/api/health

# Test chat
curl -X POST https://your-app.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me about Dr. Anirban Lakshman"}'
```

### Test Frontend (Netlify or Render)
1. Open your URL in browser
2. Try these queries:
   - "Tell me about Dr. Anirban Lakshman"
   - "Who is the director?"
   - "Show me CSE faculty"
   - "What are the placement records?"

---

## 🔧 Troubleshooting

### Backend Issues

**Problem**: "Application failed to start"
- Check Render logs for errors
- Verify `requirements.txt` has all dependencies
- Ensure Python version matches (3.11)

**Problem**: "Module not found"
- Render might be missing dependencies
- Check build logs and add missing packages to `requirements.txt`

**Problem**: "Cold start - slow first request"
- Free tier Render sleeps after 15min inactivity
- First request wakes it up (takes 30-60s)
- Normal behavior for free tier

### Frontend Issues

**Problem**: "Cannot connect to server"
- Verify backend URL in `static-frontend/index.html`
- Check CORS is enabled in Flask (already done in `app.py`)
- Test backend URL directly

**Problem**: "Netlify build fails"
- Ensure base directory is `static-frontend`
- No build command needed for static HTML

---

## 💰 Cost Breakdown

### Free Forever:
- ✅ GitHub: Unlimited public repos
- ✅ Render: 750 hours/month free
- ✅ Netlify: 100GB bandwidth/month free

### Limitations:
- ⚠️ Render free tier: Sleeps after 15min inactivity
- ⚠️ First request after sleep: 30-60s delay
- ✅ No credit card required!

---

## 🎯 Next Steps

1. **Monitor your deployments**
   - Render dashboard: https://dashboard.render.com
   - Netlify dashboard: https://app.netlify.com

2. **Set up custom domain** (optional)
   - Buy domain from Namecheap/GoDaddy
   - Connect to Netlify (free SSL included!)

3. **Enable continuous deployment**
   - Already set up! Push to GitHub = auto-deploy

4. **Share your chatbot**
   - Update README.md with live URLs
   - Share with friends and faculty!

---

## 📞 Need Help?

- **Render Docs**: https://render.com/docs
- **Netlify Docs**: https://docs.netlify.com
- **Flask Deployment**: https://flask.palletsprojects.com/en/stable/deploying/

---

**Pro Tip**: For production, consider upgrading to paid tiers to eliminate cold starts and get better performance!
