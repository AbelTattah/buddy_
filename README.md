# Flask Backend for Buddy
Current deployed on Render: https://buddy-zpdh.onrender.com
A new faster link will be posted very soon.

## Endpoint
1. /geturl
This endpoint recieves Book keywords an returns book Titles and their corresponding download links.

Request Body:
```
{
	"keywords":"My Book of Bible Stories"
}
```
Request Headers:
```
{
"content-Type":"application/json"
}
```

### Example Response
```
Response:200, OK
{
"titles":[
          "Bible Story1",
          "Bible Story2"
         ],
"links":[
         "https://librarylol.com/sdijfsodj",
         "https://librarylol..com/sodijjfiosdihf"
        ]
}
```

