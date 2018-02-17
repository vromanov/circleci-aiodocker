import aiodocker
import asyncio
import pytest


class TestAlertModel:

    @pytest.mark.asyncio
    async def test_aiodocker(self):
        env = [
            'AWS_ACCESS_KEY_ID=key',
            'AWS_SECRET_ACCESS_KEY=secret'
        ]
        config = {
            'Image': 'instructure/dynamo-local-admin',
            'AttachStdout': False,
            'AttachStderr': False,
            'Env': env,
            'HostConfig': {
                'PortBindings': {
                    '8000/tcp': [
                        {
                            'HostIp': '',
                            'HostPort': '8000'
                        }
                    ]
                }
            }
        }
        docker = aiodocker.Docker()
        container = await docker.containers.create_or_replace(
            name='dynamodb', config=config)
        await container.start()
        await asyncio.sleep(3)
        host = (await container.show())['NetworkSettings']['IPAddress']
        print(host)
        # await container.kill()
        # await container.delete(force=True)
