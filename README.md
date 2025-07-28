# Calculator Server - REST API

This is a simple REST API built using **Flask** that performs basic arithmetic operations such as addition, subtraction, multiplication, and division.

**Live URL**:  
[API](https://calc-server-rest-api.onrender.com/)

---

## Features

- Basic arithmetic operations
- JSON-based API input and output
- Easy to test with Postman

---

## API Endpoints

### GET `/`

Returns a basic welcome message in HTML.

#### Example usage:

## POST `/`

Accepts a JSON payload to perform the requested operation.

### Supported Operations

- `add` - addition  
- `sub` - subtraction  
- `mul` - multiplication  
- `div` - division  

---

### Sample Request

```json
{
  "op": "add",
  "first": 10,
  "second": 5
}
```
### Sample Response
```json
{
  "result": 15
}
```
