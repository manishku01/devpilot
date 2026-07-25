# DevPilot Architecture

## Goal

Build a self-service deployment platform where developers can deploy applications without directly accessing Jenkins.

## Components

- React Frontend
- FastAPI Backend
- PostgreSQL Database
- Jenkins
- GitHub
- Docker

## Workflow

Developer
↓
React UI
↓
FastAPI
↓
Jenkins API
↓
Build
↓
Deploy
↓
Return Status