from django.core.files.uploadhandler import MemoryFileUploadHandler, TemporaryFileUploadHandler
from django.core.files.uploadedfile import UploadedFile


class CustomFileUploadHandler(MemoryFileUploadHandler, TemporaryFileUploadHandler):
    """
    Custom file upload handler that allows SVG files to be uploaded in the Django admin site.
    """
    def file_complete(self, file_size):
        """
        Called by Django when a file upload is complete.

        If the uploaded file is an SVG file, set its content type to "image/svg+xml" to allow it to be displayed in the
        admin site. Otherwise, use the default behavior.
        """
        # Call the parent class's file_complete() method to get a handle to the uploaded file
        file_obj = super().file_complete(file_size)

        # If the uploaded file is an SVG file, set its content type to "image/svg+xml"
        if isinstance(file_obj, UploadedFile) and file_obj.content_type == 'image/svg+xml':
            file_obj.content_type = 'image/svg+xml'

        # Return the updated file object
        return file_obj
