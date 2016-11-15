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
'http://development.bibbox.org/api/jsonws/BIBBOXDocker-portlet.get-id-mapping-info?instanceId=pt99'

'''json
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
'''

### GET / info
'http://idmapping.development.bibbox.org/idmapping/api/v1.0/info?id=SUBJECT@pt99.development.bibbox.org::P0000002'

### GET /generate
'http://idmapping.development.bibbox.org/idmapping/api/v1.0/generate?id=SUBJECT@pt99.development.bibbox.org::P0000002?type=HR'