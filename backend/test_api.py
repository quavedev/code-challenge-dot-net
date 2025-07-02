#!/usr/bin/env python3
"""
Simple test script to verify API endpoints.
Run this after starting the server to test basic functionality.
"""

import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    """Test health endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_communities():
    """Test communities endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/api/communities/")
        print(f"Communities: {response.status_code} - Found {len(response.json())} communities")
        return response.status_code == 200
    except Exception as e:
        print(f"Communities test failed: {e}")
        return False

def test_people():
    """Test people endpoint"""
    try:
        response = requests.get(f"{BASE_URL}/api/people/")
        print(f"People: {response.status_code} - Found {len(response.json())} people")
        return response.status_code == 200
    except Exception as e:
        print(f"People test failed: {e}")
        return False

def main():
    print("Testing Quave Challenge API...")
    print(f"Base URL: {BASE_URL}")
    print("-" * 40)
    
    tests = [
        ("Health Check", test_health),
        ("Communities", test_communities),
        ("People", test_people),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\nRunning {test_name}...")
        if test_func():
            print(f"✅ {test_name} passed")
            passed += 1
        else:
            print(f"❌ {test_name} failed")
    
    print(f"\n{'-' * 40}")
    print(f"Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the server and database.")

if __name__ == "__main__":
    main()