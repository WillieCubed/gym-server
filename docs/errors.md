# Request Error Codes
*Universal request error codes for Gym Server*

These error codes only come when requesting `Experiment` resources through
HTTP REST or WebSocket endpoints.

Resource endpoints use mostly standard convention for response status codes:
 - 101 Switching Protocols: The request is being upgraded to a WebSocket
   connection.
 - 200 OK: Your request was handled successfully.
 - 202 Created: A new resource has been created (POST requests only).
 - 400 Bad Request: The server could not interpret your request body.
 - 401 Unauthorized: The request required authentication, but none was provided.
 - 403 Forbidden: The request does not have proper access permissions for the
   requested resource. 
 - 404 Not Found: The requested resource does not exist on the server.
 - 500 Internal server error: Something went wrong, but you don't need to worry.

Errors for requests to resource endpoints follow this format:
```json
{
  "errorCode": 100,
  "message": "Unknown server error. Try again later." 
}
```

TODO: Centralize API documentation for endpoints

### experiment
*Error code 1*

Returned when an experiment encounters an unrecoverable error.

### experimentUnknown
*Error code 10*

Returned when the given `experiment_id` for an operation does not exist.

### unknown
*Error code 100*

Returned when the server does not know went wrong.