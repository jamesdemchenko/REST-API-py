#Device Registry Service

## Usage

All responses will have the form

```json
{
	"data": "Mixed type holding the content of the response",
	"message": "Description of what happened"

}
```

Subsequent response definitions will only detail the expected value of the 'data field'

### List all devices
**Definitions**

`GET /devices`

**Response**
- '200 OK' on success

```json
[
	{ "identifier":"lamp_style1",
		"name": "Cozy Lamp",
		"device type":"switch",
		"controller_gateway": "192.1.68.0.2"
	},
	{"identifier":"bench_style3",
		"name": "Australian Oak Bench",
		"device type":"bench",
		"controller_gateway": "192.1.68.0.2"
	}
]
```
### Registering a new device

**Definition**

`POST /device`

**Arguments**

- `"identifier": string` a globally unique identifier for this device
- `"name":string` a friendly name for this device
- `"device_type": string` the type of the device as understood by the client
- `"controller_gateway": string` the IP address of the device's controller

If a device with the given identifier already exists, the existing device will be overwritten.

**Response**
- `201 Created` on success
```json
{ "identifier":"lamp_style1",
		"name": "Cozy Lamp",
		"device type":"switch",
		"controller_gateway": "192.1.68.0.2"
}
```

## Lookup device details 
 `Get/ device/<identifier>`

 	**Response**
- `404 Not Found` if the device does not exist
- `200 OK` on success
```json
{ "identifier":"lamp_style1",
		"name": "Cozy Lamp",
		"device type":"switch",
		"controller_gateway": "192.1.68.0.2"
}
```
`DELETE / device/ <identifiers>`

**Response**
- `404 Not Found` if the device does not exist
- `204 No Content` deleted content
