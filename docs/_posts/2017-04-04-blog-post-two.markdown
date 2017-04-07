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

We've been looking into ways to do topic extraction and word simplification, which seem like overarching tasks we'll need to tackle regardless of what project we choose. Aakash has been doing a lot of good digging into finding potential solutions to word simplification using embeddings to find clustering of similar words (this motivated us to check out the Keras tutorial). We've also been looking more specifically into how we can do excerpt summarization if we decide to make a congress-bill-simplifier: There are a bunch of algorithms similar to <a href="http://smmry.com/">SMMRY</a> that we can use to solve that problem (yay!). Initial runs through SMMRY show that there a few domain specific obstacles that we will need to overcome. The summarized output had certain incomprehensible sections as well as strings that were gibberish and various scattered numbers. We theorize this is because of the inherently complicated legal jargon and numerated structure of the bills we fed it. 

Apart from topic extraction, we also played around with libraries that seem like they could help us exploit the structure of our domain specific documents. Specifically we looked at the TextRank algorithm, which is very similar to Google's PageRank algorithm but applied to natural language instead (paper can be found here: <a href="https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf">TextRank</a>). We set up a basic implementation of the algorithm found in this public Git repo: <a href="https://github.com/summanlp/textrank">TextRank Implementations</a>. Initial results look fairly promising, and we have ideas of how to build better graph models using the repetitive structure of bills (such as references to other clauses and headers/subheaders). This is very useful for excerpting (extracting key phrases verbatim from the document) which is a natural first step for our project before getting to far more difficult generated summaries. We would also like to compare TextRank against other Unsupervised Learning methods, of which a few can be found in this repo: <a href="https://github.com/miso-belica/sumy"> Automatic Text Summarization </a>.

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
