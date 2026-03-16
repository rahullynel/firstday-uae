#!/usr/bin/env python3
"""
Simple API test client - tests backend without installing anything
Run this after backend is running on localhost:8000
"""

import json
import urllib.request
import urllib.error
import sys
from typing import Optional, Any

def make_request(url: str, method: str = "GET") -> Optional[dict[str, Any]]:
    """Make HTTP request without external dependencies."""
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            return json.loads(data)
    except urllib.error.URLError as e:
        print(f"❌ Connection error: {e}")
        print(f"   Is the backend running on http://localhost:8000?")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON response: {e}")
        return None

def test_api():
    """Test API endpoints."""
    base_url = "http://localhost:8000"
    
    print("🧪 FirstDay UAE API - Simple Test")
    print("=" * 50)
    
    endpoints = [
        ("/", "Root endpoint"),
        ("/api/v1/health", "Health check"),
        ("/api/v1/health/ready", "Readiness probe"),
    ]
    
    for endpoint, description in endpoints:
        url = f"{base_url}{endpoint}"
        print(f"\n📍 Testing: {description}")
        print(f"   URL: {url}")
        
        response = make_request(url)
        
        if response is None:
            return 1
        
        print(f"   ✓ Status: OK")
        print(f"   Response: {json.dumps(response, indent=6)}")
    
    print("\n" + "=" * 50)
    print("✅ All tests passed!")
    print(f"\n📖 Interactive API docs:")
    print(f"   Open in browser: http://localhost:8000/docs")
    
    return 0

if __name__ == "__main__":
    sys.exit(test_api())
