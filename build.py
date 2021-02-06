### Site Generator created  1/24 ###
### refactored 2/3/21 ###
from string import Template
import datetime
def main():
    
    pages = [
        {
            'title': 'Home',
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

    def replace_placeholders(file,content,page_title=''):
        base_template = Template(file)
        return base_template.safe_substitute(content=content,title=page_title,get_year=datetime.datetime.now().strftime("%Y"))

   
    def write_pages(complete_page,filename):
        open(filename, "w+").write(complete_page)

    def set_navbar(page,base_input):
        base = Template(base_input)
        if page['title'] == 'Home':
            return base.safe_substitute(nav_index=' active',nav_thoughts='',nav_projects='',nav_about='')
        elif page['title'] == 'Thoughts':
            return base.safe_substitute(nav_index='',nav_thoughts=' active',nav_projects='',nav_about='')
        elif page['title'] == 'Projects':
            return base.safe_substitute(nav_index='',nav_thoughts='',nav_projects=' active',nav_about='')
        elif page['title'] == 'About':
            return base.safe_substitute(nav_index='',nav_thoughts='',nav_projects='',nav_about=' active')
        
        

    for page in pages:
        file_name = page['filename']
        file_output = page['output']
        file_title = ' - ' + page['title']
        content = read_content(file_name)
        base = read_base()
        base_final = set_navbar(page,base)
        complete_page = replace_placeholders(base_final,content,file_title)
        write_pages(complete_page,file_output)

    print('Site complete! Please review for accuracy.')
    


if __name__ == "__main__":
    main()