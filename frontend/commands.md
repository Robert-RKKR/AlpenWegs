# React + NPM Project Commands

## Table of Contents

1. [Project Setup](#project-setup)  
   1.1 [Create new project with Vite](#create-new-project-with-vite)  
   1.2 [Navigate to project folder](#navigate-to-project-folder)  
   1.3 [Install dependencies](#install-dependencies)  
2. [NPM Basics](#npm-basics)  
   2.1 [Install package](#install-package)  
   2.2 [Install dev dependency](#install-dev-dependency)  
   2.3 [Uninstall package](#uninstall-package)  
   2.4 [Update package](#update-package)  
   2.5 [Run audit](#run-audit)  
3. [React Scripts](#react-scripts)  
   3.1 [Start development server](#start-development-server)  
   3.2 [Build project](#build-project)  
   3.3 [Preview production build](#preview-production-build)  

## Project Setup

### Create new project with Vite

```bash
npm create vite@latest my-app   # Create new Vite + React project
```

### Navigate to project folder

```bash
cd my-app
```

### Install dependencies

```bash
npm install   # Install all dependencies from package.json
```

## NPM Basics

### Install package

```bash
npm install <package-name>   # Install a dependency
```

### Install dev dependency

```bash
npm install -D <package-name>   # Install a dev-only dependency
```

### Uninstall package

```bash
npm uninstall <package-name>   # Remove a package
```

### Update package

```bash
npm update <package-name>   # Update a dependency
```

### Run audit

```bash
npm audit fix   # Fix security issues automatically
```

## React Scripts

### Start development server

```bash
npm run dev -- --host 0.0.0.0   # Run project in development mode
```

### Build project

```bash
npm run build   # Create production build
```

### Preview production build

```bash
npm run preview   # Preview production build locally
```
