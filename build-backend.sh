#!/bin/bash

# Build and run backend in Docker

set -e

cd /home/rdsouza/firstday-uae

echo "🐳 Building FirstDay UAE Backend Docker Image..."

docker build -t firstday-uae-backend:latest ./backend

echo "✅ Build successful!"
echo ""
echo "To run the backend:"
echo "  docker run -p 8000:8000 -e DATABASE_URL=postgresql://postgres:postgres@localhost:5432/firstday_uae firstday-uae-backend:latest"
echo ""
echo "Or use Docker Compose:"
echo "  docker-compose up backend"
