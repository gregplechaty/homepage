### Site Generator created  1/24 ###
### refactored 2/3/21 ###
from string import Template
def main():
    
    pages = [
        {
            'title': 'Index',
            'filename': "./content/index.html",
            'output': "./docs/index.html",
            
        },
        {
            'title': 'Thoughts',
            'filename': "./content/thoughts.html",
            'output': "./docs/thoughts.html",
            
        },
        {
            'title': 'Projects',
            'filename': "./content/projects.html",
            'output': "./docs/projects.html",
            
        },
        {
            'title': 'About',
            'filename': "./content/about.html",
            'output': "./docs/about.html",
            
        },
    ]
    
    def create_pages(pages):
        for page in pages:
            file_name = page['filename']
            file_title = page['title']
            file_output = page['output']
            open_content = open(file_name).read()
            content = open_content
            print('Creating...', file_title)
            top = open("./templates/top.html").read()
            bottom = open("./templates/bottom.html").read()
            top = Template(open("./templates/top.html").read())
            top = top.safe_substitute(title='')
            index_full = top + content + bottom
            open(file_output, "w+").write(index_full)


    create_pages(pages)


    print('Site complete! Please review for accuracy.')

main()