from rest_framework.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    '''
    Build path to file : (media)/avatar/user_id/photo.jpg
    '''
    return f'avatar/{instance.id}/{file}'


def validate_size_image(file_obj):
    '''
    Check size image
    '''
    max_size = 2  #2 megabytes

    if file_obj.size > max_size * 1024 * 1024:
        raise ValidationError(f'Max Size is {max_size} megabytes')