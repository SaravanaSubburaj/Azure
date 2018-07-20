#!/usr/bin/env/python
"""vmss_private_ips.py : Returns private IPs from a Azure Scale Set"""

import json
import azurerm

resource_group = "xxxx"
scaleset = "xxxx"
tenant_id = 'xxxxxxxxxxxxxxxxxxxxx'
app_id = 'xxxxxxxxxxxxxxxx'
app_secret = 'xxxxxxxxxxxxxxxxxxxxx'
subscription_id = 'xxxxxxxxxxxxxxxxxxxxxx'
access_token = azurerm.get_access_token(tenant_id, app_id, app_secret)
response = azurerm.get_vmss_nics(access_token, subscription_id, resource_group, scaleset)

string = json.dumps(response)
data = json.loads(string)

instances = len(data["value"])
for i in range(instances):
	# print(type(data["value"][i]["properties"]["ipConfigurations"][0]["properties"]["privateIPAddress"]))
	print(data["value"][i]["properties"]["ipConfigurations"][0]["properties"]["privateIPAddress"])
