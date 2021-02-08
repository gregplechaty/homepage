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
    
    blog_posts = [
        {
            "filename": "blog/1_too_many_pieces.html",
            "date": "January 15th, 2021",
            "title": "Too Many Pieces?",
            "subtitle": "When the quantity of tools is immense, and your skills are not, how do you know where to start?",
            "output": "./docs/1_too_many_pieces.html",
            "image": "./images/legos.jpg",
        },
        {
            "filename": "blog/2_one_month_in.html",
            "date": "February 7th, 2021",
            "title": "Balance is hard.",
            "subtitle": "Doing something new takes time what to give up?",
            "output": "./docs/2_one_month_in.html",
            "image": "./images/balance.jpg",
        },
        {
            "filename": "blog/3.html",
            "date": "September 15th, 2018",
            "title": "My thoughts on Python so far",
            "subtitle": "A lot can be done with just a few commands.",
            "output": "./docs/3.html",
            "image": "./images/coconuts.jpg",
        },
    ]

    ### Read input files



    def read_content(file_name):
        return open(file_name).read()




    ### Placeholder replacement

    def set_navbar(page_title,base):
        base_input = Template(base)
        if page_title == 'Home':
            return base_input.safe_substitute(nav_index=' active',nav_thoughts='',nav_projects='',nav_about='')
        elif page_title == 'Thoughts':
            return base_input.safe_substitute(nav_index='',nav_thoughts=' active',nav_projects='',nav_about='')
        elif page_title == 'Projects':
            return base_input.safe_substitute(nav_index='',nav_thoughts='',nav_projects=' active',nav_about='')
        elif page_title == 'About':
            return base_input.safe_substitute(nav_index='',nav_thoughts='',nav_projects='',nav_about=' active')

    def replace_placeholders(file,content,page_title=''):
        base_template = Template(file)
        return base_template.safe_substitute(content=content,title=page_title,get_year=datetime.datetime.now().strftime("%Y"))

    def replace_blog_placeholders(blog_base,blog_post_title,blog_post_subtitle,blog_post_image,blog_post_content=''):
        blog_base_template = Template(blog_base)
        return blog_base_template.safe_substitute(blog_post_title=blog_post_title,blog_post_subtitle=blog_post_subtitle,blog_post_image=blog_post_image,blog_post_content=blog_post_content)


    ### write final pages


    def write_pages(complete_page,filename):
        open(filename, "w+").write(complete_page)


    def write_thoughts_content(page,blog_posts_info,blog_past_posts="./templates/blog_past_post_base.html"):
        thoughts_content = ''
        for post in reversed(blog_posts_info):
            #define variables
            blog_post_title = post['title']
            blog_post_subtitle = post['subtitle']
            blog_post_output = post['output']
            blog_post_date = post['date']
            blog_post_output = post['output'].replace('/docs','')
            blog_post_image = post['image']
            #read input files
            past_posts = open(blog_past_posts).read()
            #set variable text
            past_posts_template = Template(past_posts)
            with_subs = past_posts_template.safe_substitute(blog_post_link=blog_post_output,blog_post_title=blog_post_title,blog_post_date=blog_post_date,blog_post_subtitle=blog_post_subtitle,blog_post_image=blog_post_image)
            thoughts_content = thoughts_content + with_subs
            #write final blog page
        page_template = Template(page)
        page_template_with_subs = page_template.safe_substitute(blog_past_posts=thoughts_content)
        return page_template_with_subs

    def write_thoughts_featured(thoughts_page,blog_posts):
        last = True
        for post in reversed(blog_posts):
            if last:
                last = False
                thoughts_page_template = Template(thoughts_page)
                return thoughts_page_template.safe_substitute(blog_post_image=post['image'],blog_post_title=post['title'],blog_post_subtitle=post['subtitle'],blog_post_link=post['output'].replace('/docs',''))
            


    def write_blog_posts(blog_posts):
        for post in blog_posts:
            #define variables
            blog_post_date = post['date']
            blog_post_title = post['title']
            blog_post_subtitle = post['subtitle']
            blog_post_output = post['output']
            blog_post_image = post['image']
            #read input files
            base = open("./templates/base.html").read()
            blog_base = open("./templates/blog_base.html").read()
            blog_post_content = open(post['filename']).read()
            #set variable text
            base_final = set_navbar('Thoughts',base)
            blog_page = replace_placeholders(base_final,blog_base," - Thoughts")
            blog_complete =  replace_blog_placeholders(blog_page,blog_post_title,blog_post_subtitle,blog_post_image,blog_post_content)
            #write final blog page
            open(blog_post_output, "w+").write(blog_complete)

    
    for page in pages:
        #define variables
        file_name = page['filename']
        file_output = page['output']
        file_title = ' - ' + page['title']
        #read input files
        content = read_content(file_name)
        base = open("./templates/base.html").read()
        #set variable text
        base_final = set_navbar(page['title'],base)
        complete_page = replace_placeholders(base_final,content,file_title)
        if page['title'] == 'Thoughts':
            complete_page = write_thoughts_content(complete_page,blog_posts,"./templates/blog_past_post_base.html")
            complete_page = write_thoughts_featured(complete_page,blog_posts)
        #write final .html page
        write_pages(complete_page,file_output)

    write_blog_posts(blog_posts)



    print('Site complete! Please review for accuracy.')
    


if __name__ == "__main__":
    main()