#!/bin/bash

# Update Frontend with Production Backend URL
# Usage: ./update_api_url.sh https://your-backend.onrender.com

if [ -z "$1" ]; then
    echo "❌ Error: Please provide your backend URL"
    echo ""
    echo "Usage: ./update_api_url.sh https://your-backend.onrender.com"
    echo ""
    echo "Example:"
    echo "  ./update_api_url.sh https://college-chatbot.onrender.com"
    exit 1
fi

BACKEND_URL=$1
FRONTEND_FILE="static-frontend/index.html"

# Check if file exists
if [ ! -f "$FRONTEND_FILE" ]; then
    echo "❌ Error: $FRONTEND_FILE not found"
    exit 1
fi

# Create backup
cp "$FRONTEND_FILE" "${FRONTEND_FILE}.backup"
echo "✅ Created backup: ${FRONTEND_FILE}.backup"

# Update the API URL
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s|const API_URL = window.location.origin;|const API_URL = '$BACKEND_URL';|g" "$FRONTEND_FILE"
else
    # Linux
    sed -i "s|const API_URL = window.location.origin;|const API_URL = '$BACKEND_URL';|g" "$FRONTEND_FILE"
fi

echo "✅ Updated API URL to: $BACKEND_URL"
echo ""
echo "📝 Next steps:"
echo "1. Review changes: git diff $FRONTEND_FILE"
echo "2. Commit: git add $FRONTEND_FILE"
echo "3. Push: git commit -m 'Update production API URL' && git push"
echo ""
echo "🚀 Then deploy to Netlify!"
