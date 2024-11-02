import json
import markdown
import argparse
import os
import json_post

'''
Plan:
1. Read all markdown files in the directory
2. If there is a json database file, read it and store it in a dictionary
    2.1 Before appending markdown file information to the json database, check if the markdown file is already in the database and check last modified date
3. If there is no json database file, create a new dictionary
    3.1 Append all markdown file information to the dictionary
4. Write the dictionary to the json database file
'''

def markdown_to_json(directory):

    # Read all markdown files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".md") and filename != "template.md":
            ''''with open(os.path.join(directory, filename), 'r') as file:
                text = file.read()
                html = markdown.markdown(text)
                post = json_post.JsonPost(filename)
                post.parsehtml(text)
                #print(html)'''
            post = json_post.JsonPost(filename)

def main():

    # Parse command line arguments
    parser = argparse.ArgumentParser(
        prog="markdown_to_json",
        description="Convert markdown files to json"
    )
    parser.add_argument("-d", "--directory", help="input markdown directory", required=True)
    args = parser.parse_args()

    # Convert markdown files to json
    markdown_to_json(args.directory)


if __name__ == '__main__':
    main()