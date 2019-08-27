import boto3

ec2 = boto3.resource('ec2')
volume = ec2.Volume('vol-0278446e7d9ecbdb6')

response = volume.attach_to_instance(Device='/dev/sdh', InstanceId='i-065d85664301b0c57',DryRun=True)
print(response)
