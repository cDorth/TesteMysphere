# MySphere - Django Project

## Overview
MySphere is a Django-based web application that appears to be a multi-tenant social platform with features for user management, posts, comments, and reactions.

## Project Structure
- **accounts/** - User authentication and account management
- **tenants/** - Multi-tenant functionality
- **feed/** - Social feed with posts, comments, and reactions
- **chat/** - Chat functionality (not yet implemented)
- **MySphere/** - Main Django project configuration

## Recent Changes (October 4, 2025)
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

## User Preferences
None documented yet.

## Technology Stack
- Django 5.2.6
- Python 3.11
- SQLite (development)
- Pillow for image handling
- django-environ for environment configuration
