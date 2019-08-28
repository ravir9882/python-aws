## This script will invoke create_vpc.yaml cloudformation template and creates vpc

import boto3
client = boto3.client('cloudformation')

response = client.create_stack(
        StackName='MyVPC',
        TemplateURL='https://raviicloudformation.s3.amazonaws.com/vpc.yaml',
        Parameters=[
            {
                'ParameterKey': 'EnvironmentName',
                'ParameterValue': 'Development_Ravi',
                'UsePreviousValue': True
            }
        ],
        DisableRollback=False
)
print(response)

