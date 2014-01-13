date: 2014-01-01
author: Sample Author
title: This is a sample post
slug: sample-post-for-pelican-powered-blog
tags: blog, sample
summary: A sample post to start it all

This is a sample post powered by [Pelican].

The fields at the top are meta data about the post. Pelican will read those fields and generate the title, author, dates, and other content based up on it. Most should be self explanatory. 

`slug` refers to the final filename of the post. For example this post is "sample-post-for-pelican-powered-blog.md" so Pelican will generate a file named "sample-post-for-pelican-powered-blog.html" which is what will appear in the address bar of your browser. Note that this can be different that the title of the post. The point of this attribute is to have a consistent name for the page that will *never* change even if the title/content changes.

`tags` are comma seperated list of metadata describing your posts. They're optional but if you add them to your posts the Pelican will automatically generate pages listing your posts by tag. For example you could have all your 'foobar' organized together.

`summary` refers to the text summary that will appear on the front page of your blog.

And here is how you add a image:

<img width="200" height="200" src="/images/smiley.png" alt="Smiley" title="What you feel like when blogging with Pelican" />

[Pelican]: http://getpelican.com/
