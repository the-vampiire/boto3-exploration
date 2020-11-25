import boto3 as aws
from pprint import pprint as print
from pprint import pformat

ec2_manager = aws.client("ec2")

dry_run = False

# # create an instance
boto3_instance = ec2_manager.run_instances(
    ImageId="ami-04bf6dcdc9ab498ca",
    InstanceType="t1.micro",
    KeyName="todo-api-vamp-us-east-1",
    MaxCount=1,
    MinCount=1,
    Monitoring={"Enabled": True},
    Placement={
        "AvailabilityZone": "us-east-1a",
    },
    UserData="file://user-data.sh",
    DisableApiTermination=False,
    DryRun=dry_run,
    IamInstanceProfile={
        "Arn": "arn:aws:iam::355466282407:instance-profile/Demo-API-EC2-Service-Role"
    },
    InstanceInitiatedShutdownBehavior="terminate",
    NetworkInterfaces=[
        {
            "AssociatePublicIpAddress": True,
            "DeviceIndex": 0,
            "SubnetId": "subnet-0280696e7c72f30c1",
            "Groups": ["sg-0be537cbaf957ff53", "sg-05d3eb671c166922b"],
        },
    ],
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": "boto3-instance"}],
        }
    ],
    # LaunchTemplate={
    #     "LaunchTemplateId": "string",
    #     "LaunchTemplateName": "string",
    #     "Version": "string",
    # },
)


boto3_instance_id = boto3_instance["Instances"][0]["InstanceId"]

while True:
    boto3_instance = aws.resource("ec2").Instance(boto3_instance_id)
    public_ip = boto3_instance.public_ip_address
    if public_ip:
        print(public_ip)
        break
