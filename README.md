This Docker repository contains a simple Flask application designed to echo back all HTTP request headers and body content, irrespective of the HTTP method or URL path used. It's a valuable tool for debugging and testing client-server communications.

## Features
* Echoes back all request headers and body content.
* Accepts all HTTP methods: GET, POST, PUT, DELETE, and PATCH.
* Handles any URL path.
* Provides a JSON-formatted response for easy reading.
* Ready for immediate deployment for testing purposes.


## Real-time Support

### Server-Sent Events (SSE)
* Endpoint: `/stream`
* Returns a continuous stream of timestamps (every 1 second).
* Useful for testing SSE connectivity and load balancers.

### WebSockets
* Endpoint: `/ws`
* Echoes back any text message sent to it.
* Useful for testing full-duplex communication and WebSocket support in proxies/load balancers.

## Deployment
```bash
docker run -d --name headerrevealer -p 5000:5000 amdadulbari/headerrevealer
```
