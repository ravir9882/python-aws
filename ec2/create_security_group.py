# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the 'License').
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an 'AS IS' BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License. 


import boto3
from botocore.exceptions import ClientError

def get_vpc_id():
    ec2 = boto3.client('ec2')
    response = ec2.describe_vpcs()
    vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')
    return vpc_id

def create_sec_group(GroupName, Description, vpc_id):
    try:
        ec2 = boto3.client('ec2')
        response = ec2.create_security_group(GroupName=GroupName,
                                         Description=Description,
                                         VpcId=vpc_id)
        security_group_id = response['GroupId']
        print('Security Group Created %s in vpc %s.' % (security_group_id, vpc_id))
    
        data = ec2.authorize_security_group_ingress(
            GroupId=security_group_id,
            IpPermissions=[
                {'IpProtocol': 'tcp',
                'FromPort': 80,
                'ToPort': 80,
                'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
                {'IpProtocol': 'tcp',
                'FromPort': 22,
                'ToPort': 22,
                'IpRanges': [{'CidrIp': '183.82.21.100/32'}]}
            ])
        print('Ingress Successfully Set %s' % data)
    except ClientError as e:
        print(e)
 
 
def main():
    ##Assign the values here
    GroupName = "my_ec2_admin_group"
    Description = "Used for admin activities"
    vpc_id = get_vpc_id()
    create_sec_group(GroupName, Description, vpc_id)
    return GroupName

if __name__ == '__main__':
    main()

