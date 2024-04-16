import glob
import boto3
import json
region_name = 'us-west-2'

client = boto3.client('rekognition', region_name=region_name)
combined = []
for filename in glob.glob('public/photos/*.jpeg'):
    with open(filename, 'rb') as fd:
        response = client.detect_labels(Image={'Bytes': fd.read()})
        entry = {  "Filename": filename.replace("public/", "") }
        #####
        # Replace this code to populate the Labels key with the response from the service
        #####

        # print(f" photo details : {response['Labels']}")
        entry['Labels'] = response['Labels']
        # entry["Labels"] =  [
        #     {
        #         "Name": "Label-ReplaceThis",
        #         "Confidence": 95.63501739501953,
        #         "Parents": []
        #     },
        #     {
        #         "Name": "Label-ReplaceThis",
        #         "Confidence": 89.634765625,
        #         "Parents": [{"Name": "Parent-ReplaceThis"}
        #         ]
        #     }
        # ]
        combined.append(entry)

print(json.dumps(combined, indent=2))
