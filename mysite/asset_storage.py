from storages.backends.s3boto3 import S3Boto3Storage

# Image 저장 데이터 베이스로 AWS_S3 사용 
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False