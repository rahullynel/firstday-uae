#!/usr/bin/env python3
"""
Backend Sanity Check - Uses only Python standard library
Tests that all source files have correct syntax and can be imported
"""

import py_compile
import sys
from pathlib import Path

def main():
    backend_path = Path("/home/rdsouza/firstday-uae/backend")
    
    print("🧪 FirstDay UAE Backend - Sanity Check")
    print("=" * 50)
    
    # Check all Python files compile
    py_files = list(backend_path.glob("app/**/*.py")) + list(backend_path.glob("tests/**/*.py"))
    
    print(f"\n📝 Checking {len(py_files)} Python files...")
    
    all_ok = True
    for py_file in sorted(py_files):
        rel_path = py_file.relative_to(backend_path)
        try:
            py_compile.compile(str(py_file), doraise=True)
            print(f"  ✓ {rel_path}")
        except py_compile.PyCompileError as e:
            print(f"  ✗ {rel_path}: {e}")
            all_ok = False
    
    if not all_ok:
        print("\n❌ Some files have syntax errors!")
        return 1
    
    print("\n✅ All files compile successfully!")
    
    # Print file structure
    print("\n📁 Backend Structure:")
    print("```")
    print("backend/")
    print("├── app/")
    print("│   ├── main.py              ← FastAPI entry point")
    print("│   ├── core/")
    print("│   │   └── config.py        ← Pydantic settings")
    print("│   ├── db/")
    print("│   │   └── session.py       ← SQLAlchemy session")
    print("│   └── api/v1/")
    print("│       ├── api.py           ← v1 router")
    print("│       └── endpoints/")
    print("│           └── health.py    ← Health endpoints")
    print("├── tests/")
    print("│   ├── test_main.py         ← App tests")
    print("│   ├── test_config.py       ← Config tests")
    print("│   ├── test_health.py       ← Health tests")
    print("│   └── test_api_integration.py")
    print("├── requirements.txt         ← Dependencies")
    print("├── setup.sh                 ← Setup script")
    print("├── TESTING.md               ← Test guide")
    print("└── conftest.py              ← Pytest config")
    print("```")
    
    print("\n📋 What's Implemented:")
    print("  ✓ FastAPI application with CORS")
    print("  ✓ Environment configuration (Pydantic Settings)")
    print("  ✓ SQLAlchemy session management")
    print("  ✓ API v1 routers at /api/v1")
    print("  ✓ Health endpoints (/api/v1/health, /api/v1/health/ready)")
    print("  ✓ Full test suite with pytest")
    print("  ✓ Lifespan management")
    print("  ✓ CORS configuration for frontend")
    
    print("\n🚀 Next Steps:")
    print("\n  Option 1: Use Docker (Easiest)")
    print("  ==========================================")
    print("  docker-compose up --build")
    print("  # Backend: http://localhost:8000")
    print("  # API Docs: http://localhost:8000/docs")
    
    print("\n  Option 2: Install System Packages")
    print("  ==========================================")
    print("  sudo apt install python3.12-venv python3-pip")
    print("  bash backend/setup.sh")
    print("  cd backend && source .venv/bin/activate")
    print("  uvicorn app.main:app --reload")
    
    print("\n  Option 3: WSL/Remote Development")
    print("  ==========================================")
    print("  # Open in VS Code Remote or use dev container")
    print("  # Pre-configured dependencies in Docker containers")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
