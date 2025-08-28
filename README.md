# AIHumanizer API Client

## Overview

This project implements a Python client that interacts with AIHumanizer.io's internal API endpoints by reverse-engineering the requests sent from their web frontend to the backend. The service is designed to humanize AI-generated text content, and this client replicates the browser's communication with their servers to provide the same functionality through a command-line interface. The client utilizes Server-Sent Events (SSE) to provide real-time streaming of the humanization process, allowing users to observe the text transformation as it occurs.

## Project Structure

```
AIHumanizer.ioAPi/
├── main.py              # Primary implementation with environment variable support
├── .env                 # Environment variables (not included in repository)
```

## Features

- **Real-time Streaming**: Implements Server-Sent Events (SSE) to display text humanization in real-time
- **Environment Configuration**: Supports loading credentials from environment variables
- **Error Handling**: Includes comprehensive error handling for network requests and API responses
- **Multiple Implementations**: Three different versions demonstrating various approaches to the same functionality

## Technical Implementation

### Core Dependencies

- `http.client`: Built-in Python library for HTTP connections
- `sseclient`: Third-party library for handling Server-Sent Events
- `python-dotenv`: Environment variable management
- `json`: JSON data parsing and manipulation

### API Integration

The client communicates with AIHumanizer.io's internal backend API by replicating the requests made by their web frontend:
- **URL**: `https://aihumanize.io/dev/outstream`
- **Method**: POST
- **Content-Type**: application/json

**Note**: This endpoint is not publicly documented as it's part of the internal communication between the website's frontend and backend. The implementation was achieved through network traffic analysis of the web application.

### Authentication

The application requires authentication tokens that are typically handled by the web browser when using the official website:
1. **Token**: User authentication token obtained from browser session or provided via input

These tokens must be manually extracted from browser developer tools when using the official AIHumanizer.io website.

## Installation and Setup

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation Steps

1. Clone or download the project files
2. Install required dependencies:
   ```bash
   pip install sseclient-py python-dotenv
   ```

3. Create a `.env` file in the project root with the following structure:
   ```
   TOKEN=your_authentication_token_here
   ```

## Usage

### Basic Usage (main.py)

```bash
python main.py
```

This version automatically loads credentials from the `.env` file or prompts for manual input if the file is not found.



## Code Structure Analysis

### Request Payload

The API expects a JSON payload with the following structure:
```json
{
  "prompt": "text_to_humanize",
  "token": "jwt_authentication_token",
  "auto": 0,
  "cjtype": 0,
  "model": 0
}
```

### Response Handling

The API returns Server-Sent Events with different event types:
- `success`: Contains humanized text chunks
- `final_words`: Reports the final word count
- `language`: Indicates the detected language
- `final_ai_score`: Provides the AI detection score

### Streaming Implementation

The streaming functionality is achieved through:
1. Establishing an HTTPS connection to the API
2. Sending a POST request with appropriate headers
3. Using `sseclient.SSEClient` to parse Server-Sent Events
4. Processing each event and displaying content in real-time

## Learning Outcomes

This project demonstrates several important programming and reverse engineering concepts:

- **HTTP Client Programming**: Understanding how to make HTTP requests and handle responses
- **Server-Sent Events**: Implementation of real-time data streaming
- **Web API Reverse Engineering**: Analyzing network traffic to understand internal API structures
- **Browser Session Replication**: Mimicking browser behavior in a programmatic client
- **Environment Management**: Secure handling of extracted credentials
- **Error Handling**: Proper exception management and user feedback

## Potential Improvements

- Implement retry logic for failed requests
- Add configuration file support for different API endpoints
- Implement logging for debugging purposes
- Add unit tests for core functionality
- Create a command-line interface with argument parsing

## Security Considerations

- Credentials are extracted from browser sessions and stored in environment variables to avoid hardcoding
- The `.env` file should be included in `.gitignore` to prevent accidental commits
- Authentication tokens expire and must be refreshed periodically from the browser
- This implementation relies on reverse-engineered endpoints that may change without notice
- Use responsibly and in accordance with the website's terms of service

## Legal and Ethical Considerations

This project is for educational purposes, demonstrating API reverse engineering and HTTP client implementation. Users should:
- Respect the website's terms of service
- Use the service responsibly and avoid excessive requests
- Understand that internal APIs may change without notice
- Consider the ethical implications of automating web services

## Conclusion

This project serves as a practical example of web API reverse engineering, real-time data streaming, and HTTP client implementation. It demonstrates how to analyze and replicate browser-server communication while maintaining good coding practices and security standards. The implementation showcases the technical skills required to understand and interact with internal web APIs through network traffic analysis.
