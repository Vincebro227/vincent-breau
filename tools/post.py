import json
import os
import re

class Post:

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
            lines = file.readlines()
            
            # Define regex patterns
            author_pattern = re.compile(r'^##\s*Author:\s*(.*)')
            title_pattern = re.compile(r'^##\s*Title:\s*(.*)')
            date_pattern = re.compile(r'^##\s*Date-of-Creation:\s*(.*)')
            id_pattern = re.compile(r'^##\s*ID:\s*(.*)')
            status_pattern = re.compile(r'^##\s*Status:\s*(.*)')
            last_edited_pattern = re.compile(r'^##\s*Last-Edited:\s*(.*)')
            content_pattern = re.compile(r'^##\s*Content:\s*(.*)', re.DOTALL)
            
            content_lines = []
            content_started = False
            
            for line in lines:
                # Author
                author_match = author_pattern.match(line)
                if author_match:
                    self.author = author_match.group(1).strip()
                    continue
                
                # Title
                title_match = title_pattern.match(line)
                if title_match:
                    self.title = title_match.group(1).strip()
                    continue
                
                # Date
                date_match = date_pattern.match(line)
                if date_match:
                    self.date = date_match.group(1).strip()
                    continue
                
                # ID
                id_match = id_pattern.match(line)
                if id_match:
                    self.id = id_match.group(1).strip()
                    continue
                
                # Status
                status_match = status_pattern.match(line)
                if status_match:
                    self.status = status_match.group(1).strip()
                    continue
                
                # Last-edited
                last_edited_match = last_edited_pattern.match(line)
                if last_edited_match:
                    self.last_edited = last_edited_match.group(1).strip()
                    continue
                
                # Content
                if content_started:
                    content_lines.append(line)
                # If pattern is found, content has started and will be found below
                elif content_pattern.match(line):
                    content_started = True
            
            self.content = ''.join(content_lines).strip()

    def tojson(self, database):

        # Check if the database file exists
        if os.path.exists(database):
            with open(database, 'r') as file:
                # Check if the file is empty
                if os.stat(database).st_size == 0:
                    data = {}
                else:
                    data = json.load(file)
        else:
            data = {}

        # Check if the post is already in the database
        if self.id in data:
            # Check if the last edited date is newer than the one in the database
            if self.last_edited > data[self.id]['last_edited']:
                data[self.id] = {
                    'title': self.title,
                    'author': self.author,
                    'date': self.date,
                    'id': self.id,
                    'status': self.status,
                    'last_edited': self.last_edited,
                    'content': self.content
                }
        else:
            data[self.id] = {
                'title': self.title,
                'author': self.author,
                'date': self.date,
                'id': self.id,
                'status': self.status,
                'last_edited': self.last_edited,
                'content': self.content
            }

        # If database file does not exist, create it
        if not os.path.exists(database):
            with open(database, 'w') as file:
                json.dump(data, file, indent=4)
        else: # If it does exist, write to it
            with open(database, 'w') as file:
                json.dump(data, file, indent=4)

        pass