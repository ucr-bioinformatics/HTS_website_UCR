# HTS_website_UCR
Submission form for sequencing center at UCR

## Initial Setup Instructions

Clone the repo and `cd` into the cloned folder.

1. `cd hts_site`
2. Create a virtualenv __[Optional, recommended]__
3. Install the required dependencies using `pip -r requirements.txt`
4. Run the database migrations for the site: `python manage.py migrate`
    - If running in production, the database settings should be changed before running this command.
5. Start the site: `python manage.py runserver`


## Site Setup Instructions

These steps are to be completed after setting up the database and the site:

1. Make new user(s) __[Optional]__
2. Add any static pages. Note that Bootstrap tags will work and as it is already imported.
3. Create endpoints for the Management and Api AppHooks
    - The API endpoint should have a slug of `api`.
    - The Management endpoint should have a slug of `view`. __[Optional, recommended]__
