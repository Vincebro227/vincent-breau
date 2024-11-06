import json
import argparse
import os
import post

'''
Plan:
1. Read all markdown files in the directory
2. If there is a json database file, read it and store it in a dictionary
    2.1 Before appending markdown file information to the json database, check if the markdown file is already in the database and check last modified date
3. If there is no json database file, create a new dictionary
    3.1 Append all markdown file information to the dictionary
4. Write the dictionary to the json database file
'''

def markdown_to_json(directory, database):

    # Read all markdown files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename != "template.md":
            tmp_post = post.Post(filename, directory)
            tmp_post.parsemd()
            tmp_post.tojson(database)
            #print(post.author)
            #print(post.date)
            #print(post.title)
            #print(post.status)
            #print(post.last_edited)
            #print(post.content)

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="markdown_to_json",
        description="Convert markdown files to json"
    )
    parser.add_argument("-d", "--directory", help="input markdown directory", required=True)
    parser.add_argument("-db", "--database", help="json database file", required=True)
    args = parser.parse_args()

    # Convert markdown files to json
    markdown_to_json(args.directory, args.database)


if __name__ == '__main__':
    main()