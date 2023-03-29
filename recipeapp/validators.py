from django.core.exceptions import ValidationError
from django.utils.html import strip_tags


def textfield_not_empty(textfield):
    """
    Strips white space from Summernote fields and raise an error
    if the field is empty
    Code source: https://code-institute-room.slack.com/archives/CGWQJQKC5/
    p1659026298076079?thread_ts=1659005118.161939&cid=CGWQJQKC5
    """
    cleaned_data = strip_tags(textfield).replace("&nbsp;", "").strip()
    if cleaned_data == "":
        raise ValidationError("Please fill in this field.")
