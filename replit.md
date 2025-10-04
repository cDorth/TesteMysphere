# MySphere - Django Project

## Overview
MySphere is a Django-based web application - a multi-tenant social platform with features for user management, posts, comments, reactions, and a complete social feed system.

## Project Structure
- **accounts/** - User authentication and account management
- **tenants/** - Multi-tenant functionality
- **feed/** - Social feed with posts, comments, likes, shares and reactions
- **chat/** - Chat functionality (not yet implemented)
- **MySphere/** - Main Django project configuration

## Recent Changes (October 4, 2025)

### Initial Setup
- Imported project from GitHub to Replit
- Installed Python 3.11 and all required dependencies
- Fixed app naming issue: Changed 'fead' to 'feed' throughout the codebase
- Configured Django settings for Replit environment:
  - Set ALLOWED_HOSTS to ['*']
  - Added CSRF_TRUSTED_ORIGINS for Replit domains
  - Configured database to use SQLite with fallback
  - Added STATIC_ROOT for static files
- Fixed migration references from 'fead' to 'feed'
- Successfully ran all database migrations
- Configured workflow to run Django development server on port 5000
- Added media URL configuration for development

### Feed System Implementation
- Enhanced Feed models with Like and Share functionality
- Added video upload support to posts
- Created complete feed view with 3-column layout
- Implemented AJAX interactions for likes, comments, and shares
- Designed responsive UI matching provided mockups
- Features implemented:
  - **Feed**: Main feed with post creation, viewing posts with media support
  - **Profile Sidebar**: User stats (posts, followers, following), navigation menu
  - **Messages/Events Sidebar**: Event listings and message requests
  - **Post Interactions**: Like, Comment, Share buttons with real-time counters
  - **Post Creation**: Support for text, images, and videos

## Feed Features
- ✅ Create posts with text, images, or videos
- ✅ Like/unlike posts with visual feedback
- ✅ Comment on posts with real-time updates
- ✅ Share posts
- ✅ View post statistics (likes, comments, shares)
- ✅ 3-column responsive layout
- ✅ Profile sidebar with user information
- ✅ Events and messages sidebar
- ❌ Stories (not implemented as requested)
- ❌ Direct messaging (not implemented as requested)
- ❌ Gamification (not implemented as requested)

## Test Credentials
- **Username**: testuser
- **Password**: test123

## Setup Instructions
1. Dependencies are managed via requirements.txt
2. Database: SQLite (db.sqlite3) - auto-created on first migration
3. Run migrations: `python manage.py migrate`
4. Start server: `python manage.py runserver 0.0.0.0:5000`

## Environment Configuration
- **Development Server**: Runs on 0.0.0.0:5000
- **Database**: SQLite (development), can be configured for PostgreSQL via .env
- **Static Files**: Collected to /staticfiles/
- **Media Files**: Uploaded to /media/

## URLs
- **Feed**: `/` (requires login)
- **Login**: `/user/login/`
- **Admin**: `/admin/`

## Technology Stack
- Django 5.2.6
- Python 3.11
- SQLite (development)
- Pillow for image handling
- django-environ for environment configuration
- Gunicorn for production deployment
