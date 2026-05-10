# Deployment Guide

## Environment
- Python 3.14
- Virtual Environment
- OpenAI API
- ChromaDB

## Setup

### Create Virtual Environment

python3 -m venv venv

### Activate

source venv/bin/activate

### Install Dependencies

pip install -r requirements.txt

## Run Application

python3 -m app.main

## Health Check

python3 deployment/health_check.py

## Assumptions
- OpenAI API key configured
- ChromaDB available locally
- Internet connectivity required

## Limitations
- No real banking integration
- No transactional support
- Non-production authentication