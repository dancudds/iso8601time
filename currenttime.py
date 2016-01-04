from __future__ import print_function

from time import strftime
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    print('Checking ios time at {}...'.format( event['time']))
    currenttime=(strftime("%Y%m%d")+'T'+strftime("%H%M%S")+'Z')
    print(currenttime)
    s3.Object(bucketname, 'currenttime.txt').put(ACL='public-read',Body=(currenttime),CacheControl="max-age=1",ContentType="text/plain")
