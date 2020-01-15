# HTS_website_UCR
Submission form for sequencing center at UCR

## Initial Setup Instructions

Clone the repo and `cd` into the cloned folder.

1. `cd hts_site`
2. Create a virtualenv __[Optional, recommended]__
3. The `requirements.txt` file is outdated, used the following instead:

   ```bash
     pip install 'Django<1.9' 'django-cms==3.5.3' djangocms-admin-style django-treebeard 'djangocms-text-ckeditor==3.5.3' djangocms-link djangocms-style djangocms-googlemap djangocms-snippet djangocms-video 'djangocms-column==1.8.0' 'easy_thumbnails==2.5' 'django-filer==1.5.0' cmsplugin-filer pytz 'django-classy-tags==0.8.0' 'html5lib==0.9999999' Pillow 'django-sekizai==0.10.0' six 'djangorestframework==3.9.0' django-extensions 'django-mptt==0.9.0' 'django-polymorphic==1.3.1' 'django-formtools==2.1'
     ```

4. Run the database migrations for the site: `python manage.py migrate`
    - If running in production, the database settings should be changed before running this command.
    - If running in production, **make sure you change the SECRET_KEY in `settings.py`**
5. Start the site: `python manage.py runserver`


## Site Setup Instructions

These steps are to be completed after setting up the database and the site:

1. Make a new admin user: `python manage.py createsuperuser`
2. Add any static pages. Note that Bootstrap tags will work and as it is already imported.
3. Create endpoints for the Management and Api AppHooks
    - The API endpoint (named `Management` in the UI) should have a slug of `api`.
    - The Display endpoint should have a slug of `view`. __[Optional, recommended]__
4. Publish the pages created in step 3 to make them visible to users.
