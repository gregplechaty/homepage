### Site Generator created  1/24 ###
### refactored 2/3/21 ###
### jinja2 added 2/13/21###
import datetime
import glob
import os
from jinja2 import Template
##########################################################

### Create dictionaries - pages and blog_posts

def create_page_list():
    all_html_files = glob.glob("content/*.html")
    pages = []
    for file in all_html_files:
        filename = os.path.basename(file)
        name_only, extension = os.path.splitext(filename)
        title = name_only.capitalize()
        content = "./content/" + filename
        output = "./docs/" + filename
        pages.append({
            "title": title,
            "filename": content,
            "output": output,
            "link": filename,
        })
    return pages

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

### Create Blank html page (in content directory)

def create_new_html_page(file_name_input):
    #file_name scrubbed
    content_template_html = """<div class="row"></div>"""
    open("./content/" + file_name_input, "w+").write(content_template_html)
    return file_name_input


### Read input files

def read_content(file_name):
    return open(file_name).read()

### Placeholder replacement, using Jinja

def placeholder_replacement_base(base,page_title,content,pages):
    base = Template(base)
    return base.render({
            'pages_dict': pages,
            'content': content,
            'title': page_title,
            'get_year': datetime.datetime.now().strftime("%Y")
})


### write 'thoughts' blog pages


def write_blog_posts(blog_posts,base,pages):
    for post in blog_posts:
        #define variables
        blog_post_date = post['date']
        blog_post_title = post['title']
        blog_post_subtitle = post['subtitle']
        blog_post_output = post['output']
        blog_post_image = post['image']
        #read input files
        blog_base = open("./templates/blog_base.html").read()
        blog_post_content = open(post['filename']).read()
        #set variable text
        #Write blog
        blog_base_template = Template(blog_base)
        blog_base_final = blog_base_template.render({
            'blog_post_image': blog_post_image,
            'blog_post_title': blog_post_title,
            'blog_post_subtitle': blog_post_subtitle,
            'blog_post_content': blog_post_content,
        })
        #write complete blog page
        base_template = Template(base)
        blog_page_final = base_template.render({
                                'title': 'Thoughts',
                                'pages_dict': pages,
                                'content': blog_base_final,
                                'get_year': datetime.datetime.now().strftime("%Y"),
        })
        write_pages(blog_page_final,post['output'])

def write_thoughts_blog_past_posts(blog_posts_info,past_posts_html):
    blog_past_posts = '' #this is the placeholder to append each old post info
    for post in reversed(blog_posts_info):
        #define variables
        blog_post_title = post['title']
        blog_post_subtitle = post['subtitle']
        blog_post_date = post['date']
        blog_post_output = post['output'].replace('/docs','')
        blog_post_image = post['image']
        blog_post_filename = post['filename']
        #read input files
        past_post_layout = open(past_posts_html).read()
        #set variable text
        past_post_layout_template = Template(past_post_layout)
        past_post_layout_template_with_subs = past_post_layout_template.render({
                            'blog_post_link': blog_post_output,
                            'blog_post_title': blog_post_title,
                            'blog_post_date': blog_post_date,
                            'blog_post_subtitle': blog_post_subtitle,
                            'blog_post_image': blog_post_image,
        })
        blog_past_posts = blog_past_posts + past_post_layout_template_with_subs
    return blog_past_posts
    
    
def write_thoughts_content(thoughts_base,blog_posts,blog_past_posts):
    #write 'thoughts' (blog_post_image, blog_post_link, blog_post_title, blog_post_subtitle, blog_past_posts)
    base_template = Template(thoughts_base)
    last = True
    for post in reversed(blog_posts):
        if last:
            last = False
            return base_template.render(
                blog_post_image = post['image'],
                blog_post_link = post['output'].replace('/docs',''),
                blog_post_title = post['title'],
                blog_post_subtitle = post['subtitle'],
                blog_past_posts = blog_past_posts,
            )


### write final pages


def write_pages(complete_page,filename):
    open(filename, "w+").write(complete_page)



###########################################################################################
def main():
    pages = create_page_list()
    for page in pages:
        #define variables
        file_name = page['filename']
        file_output = page['output']
        file_title = page['title']
        #read input files
        base = open("./templates/base.html").read()
        base_html = read_content(file_name)
        if page['title'] == 'Thoughts':
            #write specific blog post
            write_blog_posts(blog_posts,base,pages)
            #write thoughts - first past posts, then complete page
            blog_past_posts = write_thoughts_blog_past_posts(blog_posts,"./templates/blog_past_post_base.html")
            thought_content = write_thoughts_content(base_html,blog_posts,blog_past_posts)
            #write 'content' for Thoughts main page
            complete_page = placeholder_replacement_base(base,file_title,thought_content,pages)
        else:
            complete_page = placeholder_replacement_base(base,file_title,base_html,pages)
        write_pages(complete_page,file_output)
    

    print('Site complete! Please review for accuracy.')
 ###########################################################################################
