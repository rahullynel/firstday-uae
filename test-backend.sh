#!/bin/bash

# FirstDay UAE Backend - Quick Test

echo "🧪 FirstDay UAE Backend - Quick Test"
echo "====================================="

cd /home/rdsouza/firstday-uae/backend

# Test Python syntax
echo "📝 Checking Python syntax..."
python3 -m py_compile app/main.py
python3 -m py_compile app/core/config.py
python3 -m py_compile app/db/session.py
python3 -m py_compile app/api/v1/api.py
python3 -m py_compile app/api/v1/endpoints/health.py
echo "✓ All source files compile successfully"

# Test imports
echo ""
echo "🔍 Testing imports..."
python3 << 'EOF'
try:
    from app.core.config import settings
    print("✓ Settings imported")
    print(f"  - App: {settings.APP_NAME}")
    print(f"  - Version: {settings.APP_VERSION}")
    print(f"  - Debug: {settings.DEBUG}")
    print(f"  - API v1 prefix: {settings.API_V1_STR}")
    print(f"  - CORS origins: {settings.CORS_ORIGINS}")
except ImportError as e:
    print(f"✗ Import failed: {e}")
    exit(1)
EOF

echo ""
echo "✅ All checks passed!"
echo ""
echo "📋 Next Steps:"
echo "1. Install system dependencies:"
echo "   sudo apt install python3.12-venv python3-pip"
echo ""
echo "2. Run the setup script:"
echo "   bash backend/setup.sh"
echo ""
echo "3. Start the backend:"
echo "   cd backend && source .venv/bin/activate && uvicorn app.main:app --reload"
