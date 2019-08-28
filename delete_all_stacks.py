## list stacks

import boto3

client = boto3.resource('cloudformation')

def delete_stack(stack_name):
    response = client.delete_stack(
            StackName=stack_name
        )
    print(response)

for stack in client.stacks.all():
    print(stack)
    delete_stack('MyVPC')
