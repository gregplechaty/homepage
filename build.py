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
    

    def read_content(file_name):
        return open(file_name).read()

    def read_base():
        return open("./templates/base.html").read()

    def replace_placeholders(file,content):
        base_template = Template(file)
        return base_template.safe_substitute(content=content)

    def write_pages(complete_page,filename):
        open(filename, "w+").write(complete_page)

    for page in pages:
        file_name = page['filename']
        file_output = page['output']
        content = read_content(file_name)
        base = read_base()
        complete_page = replace_placeholders(base,content)
        write_pages(complete_page,file_output)




    

    print('Site complete! Please review for accuracy.')

main()