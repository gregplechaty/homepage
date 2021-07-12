# Static Site Generator
Thanks for checking this out. This project is used to continuously regenerate and manage a static webpage with redundancies removes and 

- Jinja templating used
- Content HTML independent of header/footer templates
- Blog feature allows for each new blog post to only need the HTML of the text itself. The rest of the page and blog page get generated automatically.
- Note that the current generator utilizes Bootstrap 4.

## Usage

After downloading, install pipenv and dependencies:
```
$ pipenv install
```
```
$ pipenv shell
```
```
$ pipenv update
```

After making updates, to update/generate a new static site:
```
pipenv shell
```
```
python manage.py build
``` 

To create a new page (if done successfully, you'll be asked to specify a file name):
```
pipenv shell
```
```
python manage.py new
``` 


All final content is generated in the Docs folder, but this HTML is generated. To edit HTML:
- Templates used for the headers and footers: --> /templates
- HTML content: --> /content
- CSS: /docs/css
- images: /docs/images
- Blog posts: /blog
   - To add a new blog post, just create a new html file in /blog. The new file should get picked up

#### Questions? Ideas? Feel free to reach out. Portfolio page below:
https://gregplechaty.github.io/portfolio-page-simple/
