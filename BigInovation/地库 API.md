# 地库 API

Tags: BigInovation

---

<!-- MDTOC maxdepth:6 firsth1:1 numbering:0 flatten:0 bullets:0 updateOnSave:1 -->

[地库 API](#地库-api)  
&emsp;[Global rules](#global-rules)  
&emsp;&emsp;[Request](#request)  
&emsp;&emsp;[Response](#response)  
&emsp;[Map APIs](#map-apis)  
&emsp;&emsp;[Create a new map ID](#create-a-new-map-id)  
&emsp;&emsp;[Update map info](#update-map-info)  
&emsp;&emsp;[Upload map GeoJSON](#upload-map-geojson)  
&emsp;&emsp;[Get map GeoJSON](#get-map-geojson)  
&emsp;&emsp;[Get nearest map ID](#get-nearest-map-id)  
&emsp;&emsp;[Delete map](#delete-map)  

<!-- /MDTOC -->

---

## Global rules

### Request

1. Requests are MOSTLY without body, just `METHOD /example`
2. Some request may need sending a JSON. The JSON MUST be put in HTTP body

### Response

1. All responses MUST be transported using JSON `object` as body
2. All responses MUST contain status as below

    > `"success"` MUST exists, type: `bool`
    >
    > if `"success" == false`, you CAN get error message via `"error_msg": "str" and "error_id": int`


3. The response content MUST be stored in the `result` element of `object` type


Example:

```
{
    "success": true,
    "result" : {
        ....
    }
}
```

```
{
    "success": false,
    "error_msg": "error description",
    "errro_id": 23333
}
```

## Map APIs

### Create a new map ID

Request:

`POST /map`

Response:

```json
{
   "id": 1212
}
```

### Update map info

Request:

`PATCH /map/<id>`

```json
{
	"desc": "str of description",
	"lon": 2.333333,
	"lat": -23.33333
}
```

Response: (empty JSON object)

```json
{
}
```

### Upload map GeoJSON

Request:

`PUT /map/<id>/geojson`

```
<GeoJSON content>
```

Response: (empty JSON object)

### Get map GeoJSON

Request:

`GET /map/<id>/geojson`

Response:

```
<GeoJSON content>
```

### Get nearest map ID

Request:

`GET /map/near/<lat>/<lon>`

Response:

```json
{
	"id": 233,
	"distance": 1212.2
}
```

> distance is the distance of your position and map by meters

### Delete map

Request:

`DELETE /map/<id>`

Response: (empty JSON object)
