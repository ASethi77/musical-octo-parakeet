---
layout: post
title: "Blog Post 2 - Software Packages"
date: 2017-04-06
categories:
  - NLP
description: 
image: https://unsplash.it/2000/1200?image=1003
image-sm: https://unsplash.it/500/300?image=1003
comments: true
---

Here's some progress we've made over the last couple days...

Since we are team ????????, we don't really know what we're doing yet. So, we've spent the last few days getting more up to speed on classical NLP strategies, while also taking some time to learn a little about a neat tensorflow wrapper called Keras (<a href="https://github.com/MachinesWhoLearn/lectures/blob/master/2016-2017.Meetings/spring/01.keras_tutorial_duplicate_questions/03.train_model.ipynb">MachinesWhoLearn_KerasTutorial</a>). 

We've been looking into ways to do topic extraction and word simplification, which seem like overarching tasks we'll need to tackle regardless of what project we choose. Aakash has been doing a lot of good digging into finding potential solutions to word simplification using embeddings to find clustering of similar words (this motivated us to check out the Keras tutorial). We've also been looking more specifically into how we can do excerpt summarization if we decide to make a congress-bill-simplifier: There are a bunch of algorithms similar to <a href="http://smmry.com/">SMMRY</a> and <a href="https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf">Text Rank</a> that we can use to solve that problem (yay!). There are also many <a href="https://github.com/summanlp/textrank">opensource implementations</a> we can use and play around with.

Our friend Pooja has been really great in helping us go through previous NLP class slides, and we've been doing a lot of other independent work to get up to speed like going to the NLP PMP course, watching Standford lectures, etc. 


{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/

var PAGE_URL = "https://asethi77.github.io/musical-octo-parakeet";
var PAGE_ID = "BLOG_POST_1";

var disqus_config = function () {
this.page.url = PAGE_URL;
this.page.identifier = PAGE_IDENTIFIER;
};

(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://https-asethi77-github-io-musical-octo-parakeet.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>

{% endif %}
