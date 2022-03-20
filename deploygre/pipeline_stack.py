import logging

import boto3
from aws_cdk import (
    # Duration,
    Stack, )
from aws_cdk.pipelines import CodePipeline, ShellStep, CodePipelineSource
from constructs import Construct

from sandbox.service_stage import ServiceStage

secretsmanager = boto3.client('secretsmanager')


class PipelineStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, connection_arn: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        logger = logging.getLogger()

        github_source = CodePipelineSource.connection(
            "roliverbond/TechChallengeApp", "master",
            connection_arn=connection_arn,
        )

        pipeline = CodePipeline(self, "MyPipe",
                                pipeline_name="MyPipe",
                                cross_account_keys=True,
                                synth=ShellStep("Synth",
                                                input=github_source,
                                                commands=["npm install -g aws-cdk",
                                                          "python -m pip install -r requirements.txt",
                                                          "cdk synth"]
                                                )
                                )

        service = ServiceStage(self, 'ServiceStage')
        pipeline.add_stage(service)
