# API

## What is an API?

API (Application Programming Interface) is a set of rules, protocols, and definitions that allows one software application to communicate with with another.
It defines how requests should be made, which data can be requested, and how responses are returned without exposing the internal implementation of the system.

## What an API consists of

- Endpoints - URIs that represent resources
- Methods - actions to be performed (GET, POST, PUT, DELETE)
- Request - data sent by the client
- Response - data returned by the server
- Status Codes - indicate success or failure
---

# API Methods (HTTPs Methods)

API methods, also called as HTTP methods, define the type of action a client want to perform on a resource through an API.
They specify what operation should be executed on the server when an API endpoint is accessed.

## Common API Methods Used in REST APIs

### 1. GET

- Used to retrieve data from the server
- Does not modify server data
- Should be safe and idempotent

**Example**
```
GET /users
```
Purpose:
- Fetch a list of users
- Fetch a single resource


### 2. POST

- Used to create new data
- Sends data in the request body
- Modifies server state

**Example**
```
POST /users
```
Purpose:
- Creates a new user
- Submit form data


### 3. PUT

- Used to update an existing resource completely
- Replaces the entire resource

**Example**
```
PUT /users/1
```
Purpose:
- Update all fields of a user


### 4. PATCH

- Used to partially update a resource
- Updates only specified fields

**Example**
```
PATCH /users/1
```
Purpose:
- Update a single field like email or name


### 5. DELETE

- Used to remove a resource
- Permanently deletes data

**Example**
```
DELETE /users/1
```
Purpose:
- Delete a user
---
# REST API

## Definition of REST API

REST (Representational State Transfer) is an architectural style for designing an networked applications.
A REST API is an API that follows REST principles to enable stateless, resource-based communication between a client and a server using standard HTTP methods.

## REST API - Important Rules

1. **Resource-Based URLs**
   - Everything is treated as a resource
   - Use nouns, not verbs  
   - Example: `/users`, `/orders/5`

2. **Use Standard HTTP Methods**
   - GET → Read data
   - POST → Create data
   - PUT → Update entire resource
   - DELETE → Remove resource

3. **Client–Server Separation**
   - Client handles UI and user interaction
   - Server handles business logic and data

4. **Use Proper HTTP Status Codes**
   - 200 → Success
   - 201 → Created
   - 400 → Bad Request
   - 404 → Not Found
   - 500 → Server Error

5. **Standard Data Format**
   - JSON is commonly used for request and response bodies

---

# FastAPI

## What is FastAPI?

FastAPI is a mordern Python web framework used to build APIs, especially REST APIs, quickly and efficiently. 

It is designed to:
- Be fast
- Be easy to write
- Be easy to understand
- Automatically validate data

## What FastAPI is mainly used for
- Building backend APIs
- Creating CRUD applications
- Serving JSON responses
- Acting as the backend for:
    - Web apps
    - Mobile apps
    - ML / AI models
