# 3-Level Authentication System

This is a 3-level authentication system that ensures enhanced security by combining image selection, pattern selection, and pixel selection, in addition to the traditional username and password authentication.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)

## Introduction

The 3-Level Authentication System provides an advanced security mechanism by using a combination of the following, beyond the traditional username and password:

- **Image Selection**: The first additional level where users select a pre-defined image.
- **Pattern Selection**: The second additional level where users select a pre-defined pattern from a set of patterns.
- **Pixel Selection**: The third additional level where users select specific pixels in an image.

This multi-layered approach ensures that even if one additional level is compromised, the subsequent levels provide additional security.

## Features

- **Multi-factor authentication**: Combines traditional and advanced methods for enhanced security.
- **Customizable**: Easily configure the images, patterns, and pixels.
- **User-friendly**: Simple and intuitive interface for easy use.
- **Secure**: Protects against common attacks like brute force, phishing, and more.

## Installation

### Prerequisites

- Python 3.x
- Flask
- pymongo
- pycryptodome
- MongoDB

### Steps

1. **Clone the repository**
    ```bash
    cd C:\Users\sweta\Desktop\new 3levelAuth final project\new 3levelAuth\3levelauthentication
    ```

2. **Install dependencies**
    ```bash
    pip install Flask pymongo pycryptodome
    ```

3. **Set up the database**
    Ensure MongoDB is installed and running on your machine. You can start the MongoDB service using the following command:
    ```bash
    mongod
    ```

4. **Run the application**
    ```bash
    python app.py
    ```

## Usage

### Register

1. Navigate to the registration page.
2. Enter your desired username and password.
3. Select your authentication image, select a pattern, and select specific pixels in the image.
4. Submit the form to register.

### Login

1. Navigate to the login page.
2. Enter your username and password.
3. Select the correct authentication image.
4. Select the correct pattern.
5. Select the correct pixels in the image.
6. Submit the form to login.
