# Dovecs Property Marketing Solution

This project is developed by Group 8 as part of the 2023-2024 hackathon in TRNC Famagusta. It features an AI-driven chatbot integrated with Dovecs' website to enhance customer interactions and improve property marketing strategies.

## Team Members
- Berkay Pehlivan
- Kaan Acar
- Oktar Onder

## Introduction
The solution focuses on leveraging automation, data analysis, and personalized communication to address the marketing challenges faced by Dovecs. It utilizes technologies like web scraping, MongoDB, and SMS notifications to provide real-time updates and efficiently manage customer data.

## Features
- **AI Chatbot**: Engages with customers directly on the Dovecs website, providing tailored interactions.
- **Web Scraping**: Uses BeautifulSoup to scrape real-time house details directly from web sources.
- **Database Management**: Utilizes MongoDB for efficient data storage and retrieval.
- **SMS Notifications**: Sends targeted property details to potential customers via SMS, expanding the marketing reach.

## Implementation

### Web Scraping
- Libraries used: `json`, `requests`, `BeautifulSoup`
- Connects to MongoDB and retrieves house information from specified URLs.

### SMS Notifications
- MongoDB setup to retrieve and manage customer and property data.
- Integration with Twilio API to send SMS messages based on user preferences and inquiries.

### AI Chatbot
- Developed using Flask for backend.
- Utilizes language processing to interact and respond to user queries effectively.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-github-username/dovecs-property-marketing.git
