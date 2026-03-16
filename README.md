# FirstDay UAE

A relocation intelligence platform helping newcomers move to the UAE with confidence.

## Platform Features

- **Neighborhood Discovery**: Find neighborhoods near work locations
- **Cost of Living Estimation**: Understand living expenses in different areas
- **Bank Comparison**: Compare banking options and services
- **Amenities Exploration**: Discover nearby amenities and services
- **Commute Estimates**: Calculate travel times to key locations
- **First-Week Checklist**: Follow a structured relocation checklist

## Abu Dhabi First MVP

This initial release focuses on Abu Dhabi as the primary market, with plans for expansion to other UAE emirates.

## Tech Stack

### Backend
- **Framework**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Language**: Python 3.11+

### Frontend
- **Framework**: Next.js 14
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Node**: 18+

### Infrastructure
- **Local Development**: Docker Compose
- **Deployment**: (TBD)

## Project Structure

```
firstday-uae/
├── frontend/          # Next.js application
├── backend/           # FastAPI application
└── docs/              # Documentation
```

## Getting Started

### Prerequisites
- Docker & Docker Compose
- (or) Node.js 18+ and Python 3.11+ for local development

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/rahullynel/firstday-uae.git
   cd firstday-uae
   ```

2. **Set up environment variables**
   ```bash
   cp backend/.env.example backend/.env
   cp frontend/.env.example frontend/.env.local
   ```

3. **Start with Docker Compose**
   ```bash
   docker-compose up
   ```

   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

### Local Development (without Docker)

**Backend Setup**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend Setup**
```bash
cd frontend
npm install
npm run dev
```

## Development Workflow

### Making Changes
1. Backend changes are auto-reloaded with Uvicorn
2. Frontend changes are hot-reloaded with Next.js
3. Database migrations handled via SQLAlchemy

### Database Migrations
(To be configured with Alembic)

### Testing
(Test suites to be added)

## API Documentation

When the backend is running, visit `/docs` for interactive Swagger UI documentation.

## Contributing

(Contribution guidelines to be added)

## License

(License to be determined)

## Contact

For more information about FirstDay UAE, visit our repository or contact the team.
