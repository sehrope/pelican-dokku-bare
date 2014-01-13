A bare bones example of a [Pelican] generated static site for a blog that you can easily deploy to a PaaS.

### Installation

First [install Pelican](http://docs.getpelican.com/en/3.3.0/getting_started.html#installing-pelican). For example on Ubuntu you can install it via:

    # Install pip
    $ sudo apt-get install python-pip

    # Install pelican via pip
    $ sudo pip install pelican
    
    # Install markdown via pip (we're going to write our posts in Markdown)
    $ sudo pip install markdown

Then to set the bare site up locally, clone this repository:

    # Clone it locally:
    $ git clone --recursive https://github.com/sehrope/pelican-dokku-bare my-blog

    # Enter the directory:
    $ cd my-blog

### Usage

To run the dev server locally (*i.e. while you are writing a post*):

    # Start it up:
    $ ./develop_server.sh start

The dev server will keep running until you stop it. Any edits made to your site will be noticed (it polls the filesystem) and the site will be regenerated. To stop the dev server:

    # Stop it
    $ ./develop_server.sh stop

To deploy it your Dokku powered PaaS:

    # Add a git remote for your Dokku server:
    $ git add remote production dokku@example.org:blog

    # Push it:
    $ git push production master

### Features

* Easy to setup
* Should "just work" out of the box.
* Includes custom 403, 404, and 500 error pages.
* Defaults to using a slightly customized Octopress theme. Changing to a different theme is just a matter of picking one and editing pelicanconf.py. There [a lot of themes](https://github.com/getpelican/pelican-themes) to choose from.
* Preconfigured for "git style" deploys to Dokku with a slightly customized pelican build pack (mainly adds additional error pages to the nginx config).

### Customization Steps

1. Edit `pelicanconf.py`

    1. Change `AUTHOR`
    1. Change `SITE_NAME`
    1. Change `SITE_SUBTITLE`
    1. Change `AUTHOR_ABOUT` (optional)
    1. Change `TIMEZONE` (optional)

1. Edit `publishconf.py`

    1. Change `SITEURL`
    1. Set `GOOGLE_ANALYTICS` (optional)

1. Edit `pages/about.md`
1. Edit `pages/contact.md`
1. Add your GPG key to `extras/publickey.asc` (optional)
1. Edit `content/posts/intro.md`

### New Posts

Add new posts written in Markdown by creating new ".md" files in the `content/posts` directory. You can use the `intro.md` file as an example.

### License
[Pelican] itself is licensed under the [AGPL](https://github.com/getpelican/pelican/blob/master/LICENSE).

The sample site published in this repo is released under the MIT license. See the file [LICENSE](LICENSE).

[Pelican]: http://blog.getpelican.com/
