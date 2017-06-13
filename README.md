# SYS-IDMAPPING SERVICE
Microservice for ID mapping management in the BIBBOX framework. 

## Docker Images Used
 * phyton server running flask

## INSTALL
#### run install.sh 

## Mounted Volumes

## APIs

### THINGS

* SUBJECT
* SAMPLE
* DATA


### GET /BIBBOXDocker-portlet.get-id-mapping-info
`http://demo.bibbox.org/api/jsonws/BIBBOXDocker-portlet.get-id-mapping-info?instanceId=pt13rc1`

with the credentials: 
    username:   userapi 
    password:   changepassword

```json
{
  "mappings": {
    "SUBJECT": {
      "get_all": [
        "var appID = &&aid;",
        "var result  = 'https://' + appID + '/rest/patients';",
        "println(result);"
      ],
      "human_readable": [
        "var appID = &&aid;",
        "var localId1      = &&id1;",
        "var result        = 'https://' + appID + '/bin/ + localId1;",
        "println(result);"
      ],
      "get_info": [
        "var appID = &&aid;",
        "var localId1      = &&id1;",
        "var result        = 'https://' + appID + '/rest/patients/' + localId1;",
        "println(result);"
      ]
    }
  },
  "documentation": [
    "https://phenotips.org/DevGuide/RESTfulAPI"
  ]
}
```

### GET / info
```json
`http://demo.bibbox.org/idmapping/idmapping/api/v1.0/info/SUBJECT@pt13rc1.demo.bibbox.org::P0000012`
{
    "resolved-mappings": {
        "id": "pt13rc1.demo.bibbox.org::P0000012",
        "mappings": {
            "url": "http://pt13rc1.demo.bibbox.org/rest/patients/P0000012",
            "human-readable": "http://pt13rc1.demo.bibbox.org/bin/P0000012"
        }
    },
    "documentation": [
        "https://phenotips.org/DevGuide/RESTfulAPI"
    ],
    "mappings": {
        "SUBJECT": {
            "get_info": [
                "(",
                "function() {",
                "var appID = '&&aid';",
                "var localId1      = '&&id1';",
                "var result        = 'http://' + appID + '/rest/patients/' + localId1;",
                "return result;",
                "}",
                ")()"
            ],
            "human_readable": [
                "(",
                "function() {",
                "var appID = '&&aid';",
                "var localId1      = '&&id1';",
                "var result        = 'http://' + appID + '/bin/' + localId1;",
                "return result;",
                "}",
                ")()"
            ],
            "get_all": [
                "(",
                "function() {",
                "var appID = '&&aid';",
                "var result  = 'http://' + appID + '/rest/patients';",
                "return result;",
                "}",
                ")()"
            ]
        }
    }
}
```