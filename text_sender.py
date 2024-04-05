import boto3


class TextSender:

    @staticmethod
    def send_text(config):
        sns = boto3.client('sns',
                           region_name='eu-west-2',
                           aws_access_key_id=config['ACCESS_ID'],
                           aws_secret_access_key=config['ACCESS_KEY'])
        sns.publish(PhoneNumber=config['CONTACT_TEL'],
                    Message='example text message',
                    MessageAttributes={
                        'AWS.SNS.SMS.SenderID': {
                            'DataType': 'String',
                            'StringValue': 'GlastoAlert'
                        }}
                    )
