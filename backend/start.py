#!/usr/bin/env python3
"""
Simple startup script for the FastAPI application.
This can be used as an alternative to the uvicorn command.
"""

import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )