from aws_cdk import (
    # Duration,
    aws_ec2 as ec2, Stage,
)
from constructs import Construct

from deploygre.deploygre_stack import ServiceStack


class ServiceStage(Stage):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        serviceStack = ServiceStack(self, "ServiceStack")
