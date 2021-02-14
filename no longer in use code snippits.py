###NOT IN USE

###


def set_navbar(page_title,base):
    base_input = Template(base)
    if page_title == 'Index':
        return base_input.render(nav_index=' active',nav_thoughts='',nav_projects='',nav_about='')
    elif page_title == 'Thoughts':
        return base_input.render(nav_index='',nav_thoughts=' active',nav_projects='',nav_about='')
    elif page_title == 'Projects':
        return base_input.render(nav_index='',nav_thoughts='',nav_projects=' active',nav_about='')
    elif page_title == 'About':
        return base_input.render(nav_index='',nav_thoughts='',nav_projects='',nav_about=' active')

def write_thoughts_content(page,blog_posts_info,blog_past_posts):
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
        with_subs = past_posts_template.render(blog_post_link=blog_post_output,blog_post_title=blog_post_title,blog_post_date=blog_post_date,blog_post_subtitle=blog_post_subtitle,blog_post_image=blog_post_image)
        thoughts_content = thoughts_content + with_subs
        #write final blog page
    page_template = Template(page)
    page_template_with_subs = page_template.render(blog_past_posts=thoughts_content)
    return page_template_with_subs

def write_thoughts_featured(thoughts_page,blog_posts):
    last = True
    for post in reversed(blog_posts):
        if last:
            last = False
            thoughts_page_template = Template(thoughts_page)
            return thoughts_page_template.render(blog_post_image=post['image'],blog_post_title=post['title'],blog_post_subtitle=post['subtitle'],blog_post_link=post['output'].replace('/docs',''))
        



###


###/NOT IN USE




    
    #write final blog page
    #page_template = Template(page)
    #thoughts_blog_past_posts = page_template.render(blog_past_posts=thoughts_content)
    #return thoughts_blog_past_posts


            #complete_page = write_thoughts_content(complete_page,blog_posts,"./templates/blog_past_post_base.html")
            #complete_page = write_thoughts_featured(complete_page,blog_posts)