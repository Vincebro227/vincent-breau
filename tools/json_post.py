import json
import os
import re

class JsonPost:

    def __init__(self, filename, directory):
        self.filename = filename
        self.directory = directory
        self.title = None
        self.author = None
        self.date = None
        self.id = None
        self.status = None
        self.last_edited = None
        self.content = None

    def __str__(self):
        
        # Check if there is content to show and build a snippet if there is
        content_snippet = f"Here is a snippet of the content: {self.content[:100]}" if self.content else "No content available"

        # Build the string to return with all the information in it
        info = (
        f"This post is named {self.title}.\n"
        f"It was written by {self.author} on {self.date}.\n"
        f"Its status is {self.status} and was last edited on {self.last_edited}.\n"
        f"{content_snippet}"
        )
        
        return info

    def parsemd(self):

        with open(os.path.join(self.directory, self.filename), 'r') as file:
            # Read line by line
            lines = file.readlines()
            for line in lines:
                # Actual parsing
                # Title

                # Date

                # ID

                # Status

                # Last-edited

                # Content
                            
                pass

    def tojson(self):
        pass