


The Beauty of Crawl4AI
0:00
one of the biggest challenges we face
0:01
with large language models right now is
0:03
their knowledge is too General and it's
0:05
very limited for new things because of
0:07
its training cut off for example my
0:10
favorite new shiny framework for
0:11
building AI agents is pantic AI but if I
0:15
go over to Claude right now and ask it
0:16
what pantic AI is it has no clue and
0:20
even if I use an llm that can search the
0:22
web the information that I get back is
0:24
still going to be very Bare Bones but on
0:27
the other hand if I take all of the
0:29
framework documentation for pantic AI
0:31
and put it in a knowledge base for the
0:33
llm and I ask it the exact same question
0:36
the answer that I get is spot on that is
0:39
why rag is such a huge topic when it
0:41
comes to AI right now which that by the
0:43
way stands for retrieval augmented
0:45
generation it's a method for giving
0:47
external knowledge that you curate
0:49
yourself into an llm basically to make
0:51
it an expert at something that it wasn't
0:53
before like an AI agent framework you're
0:55
using your e-commerce store you name it
0:58
the problem is that Cur R step can be
1:00
very difficult and slow for example if
1:03
you want to ingest an entire website
1:05
into a knowledge base for your llm how
1:08
do you actually do that and get it done
1:10
fast so that it's not 2027 by the time
1:13
your knowledge base is ready and AI has
1:15
taken over the world anyway that is
1:16
where crawl for AI comes in crawl for AI
1:20
is an open-source web crawling framework
1:22
specifically designed to scrape websites
1:24
and format the output in the best way
1:26
for llms to understand and the best part
1:29
is it's it solves a lot of problems that
1:31
we typically see with these systems for
1:34
website scraping usually they're very
1:36
slow overly complicated and super
1:38
resource intensive but crawl for AI is
1:41
the complete opposite it's super
1:43
intuitive very very fast easy to set up
1:47
and extremely memory efficient so in
1:49
this video I'll show you how to super
1:51
easily use crawl for AI to scrape any
1:54
website for an llm in just seconds and
1:56
at the end of this video I'll even
1:58
quickly showcase a rag AI agent that I
2:00
built basically to be an expert at the
2:03
pantic AI framework of course using
2:05
crawl for AI to curate all the framework
2:08
knowledge into my knowledge base and
2:10
really you could take what I built and
2:11
use it for any website super exciting
2:14
stuff so let's go ahead and dive right
Why Crawl4AI?
2:16
into it so the two big things that we're
2:18
going to focus on right now is crawl for
2:20
AI which this is their GitHub right here
2:23
completely open source and then also
2:25
pantic AI now this is not a pantic AI
2:28
video but it's just a very good example
2:31
of full documentation that we can scrape
2:33
with crawl 4 Ai and bring into a
2:36
knowledge base for our llm now back over
2:38
to crawl for AI the first obvious
2:41
question when we visit this page is what
2:43
is the point of crawl for AI why even
2:45
use it and luckily at the top of their
2:47
readme here on their homepage they have
2:49
a very concise description for why you
2:51
should care about crawl for AI and the
2:54
first big thing is when you visit a
2:56
website and you extract the raw HTML
2:59
from it
3:00
I mean this looks like a mess and as a
3:02
human looking at this it's very hard for
3:04
us to actually extract useful
3:06
information from it and a good general
3:08
rule of thumb is if it's hard for us as
3:10
a human to understand something it's
3:13
probably harder for a large language
3:14
model as well and so one of the most
3:17
important things that crawl for AI does
3:20
is it takes this ugly HTML that we get
3:23
when we visit the raw content of a web
3:26
page and it turns it into markdown form
3:30
which is actually even human readable
3:32
format like a super clean way to
3:34
represent a web page and all the
3:36
information that we see when we
3:37
typically visit a UI like this just in
3:40
something that's all text space so we
3:41
can give it to a large language model
3:43
for reg and just for llms to understand
3:46
it better in general so that's the first
3:47
thing and it does it very very
3:49
efficiently it's super super fast it
3:51
handles a ton of things under the hood
3:53
like proxies and session management
3:56
things that are not easy to handle so
3:57
it's not like you can go and make your
3:59
own version of crawl for AI very easily
4:01
as well just because you know how to use
4:03
the request module in Python to pull
4:05
HTML from websites and it's also
4:08
completely open- source and very easy to
4:11
deploy they even have a Docker option
4:12
which I'll probably cover in another
4:14
video on my channel later on they're
4:15
doing major updates soon to their Docker
4:17
deployment so I don't want to focus on
4:19
that now but just know that that is
4:20
available as well and there's a ton of
4:23
other things that they do that are super
4:24
valuable as well like one really
4:26
important thing is removing irrelevant
4:28
content I mean when we go to the h ml
4:30
here we have a ton of script tags and
4:32
there's probably a lot of information um
4:34
that we can view on the page that is
4:36
very obviously redundant or just not
4:38
useful to us and that they take care of
4:40
removing that as well So eventually what
4:41
we get back from scraping the site with
4:43
crawl for AI contains just what we care
4:46
about actually ingesting into our
4:48
knowledge base and getting started with
4:51
crawl for AI is so easy all you have to
4:54
do is PIP install the python package and
4:57
then run this setup command which is
4:58
going to install playright under the
5:00
hood that is the tool that crawl for AI
5:02
uses under the hood to scrape websites
5:05
and basically have this browser running
5:07
in the background that can visit these
5:09
sites and playright is a fantastic also
5:12
open source tool that I use for a lot of
5:14
testing for my web applications as well
5:16
so very very familiar with it I can
5:18
recommend this as well so I think it's a
5:19
great choice for actually having that
5:22
web scraping functionality under the
5:24
hood and getting started is so so easy
Basic Crawl4AI Example - Single Page Crawl
5:27
it's just as simple as this little
5:29
script right here and so I actually have
5:30
my own version of it if I go into my
5:33
source control here I've got my own
5:35
version of it just scraping the homepage
5:37
of pantic AI their documentation so
5:40
let's go ahead and test this out and see
5:41
what kind of output we get and by the
5:43
way all of the code that I go over in
5:45
this video I'll have in a GitHub
5:46
repository that I will link below and so
5:48
right now we're starting with just these
5:49
basic examples right here starting with
5:52
this one to pull the homage of the
5:54
documentation for pantic AI and then
5:56
we'll get to my rag AI agent later and
5:59
I'll show showcase that a little bit as
6:01
well and so yeah I've already installed
6:03
crawl for AI it took like 30 seconds to
6:05
install everything including play right
6:07
under the hood and so now I can just go
6:09
ahead and run our script and within
6:11
seconds we're going to have the entire
6:13
page printed out in the terminal here so
6:16
so fast very very impressed with this
6:18
and this isn't like the perfect format
6:20
for us as humans to understand cuz we
6:22
have all this little markdown syntax and
6:24
stuff but this is definitely a great
6:27
format for an llm to understand this
6:29
entire page especially compared to what
6:32
we get if I just go back to the pantic
6:35
documentation here I'll just open this
6:36
back up if I inspect the page Source
6:39
this is the HTML that we got the
6:41
markdown from and imagine pasting all of
6:43
this into an llm prompt I mean it's just
6:45
a mess it's definitely going to
6:47
hallucinate when you try to ask a
6:48
question with all of the HTML tags and
6:51
everything in there and so it's just so
6:53
much better when we have something that
6:55
looks like this all right so we saw a
Crawling Multiple Pages
6:57
basic example using for AI to get the
7:00
markdown for a single file but obviously
7:03
we have to take this a lot further to do
7:05
something that is actually useful for
7:07
our llms now the first thing that we
7:09
want to do is make it possible to ingest
7:12
every single one of the pages in the
7:14
pantic AI documentation so you want to
7:16
get the markdown for the introduction
7:18
page installation getting help
7:20
contributing all of these at the same
7:22
time and the first problem we have to
7:24
tackle to actually make that possible is
7:26
we need an efficient and scalable way to
7:29
be extract all of the URLs from the
7:32
documentation here now I could just go
7:34
and manually copy and paste the homepage
7:36
and the installation page and the agent
7:38
page and just bring that into a list in
7:40
my code but that is very inefficient and
7:42
not scalable as more pages are added
7:44
I'll have to manually do the same thing
7:46
and constantly update the list myself
7:49
and so luckily there is a very good
7:51
solution for this introducing the idea
7:54
of a s map so for most Pages out there
7:57
on the internet right now if you go to
7:59
the homepage and then add SLS
8:01
sitemap.xml it's going to give you this
8:04
XML which gives you the entire structure
8:07
of the website all of the pages that
8:09
exist there and so you can do this right
8:11
now for the pantic documentation like
8:13
I'm doing right here and all the pages
8:15
that you see here are the same ones that
8:17
we see in the navigation right here and
8:20
I can do the exact same thing for the
8:22
crawl 4 AI documentation it's very meta
8:25
but I could use the sitemap.xml to get
8:28
all the pages in The crawl for AI
8:30
documentation to scrape with crawl for
8:32
AI so yeah you can do this with most
8:34
websites most e-commerce stores like if
8:36
they're built with Shopify or WordPress
8:38
they'll have this as well CU in general
8:40
websites have this for search engine
8:42
optimization and also for crawlers I
8:44
mean a lot of websites want you to crawl
8:47
them because they want their information
8:48
very widespread like if I'm building an
8:50
AI agent framework I want people to
8:53
crawl this and build agents around it
8:55
because then they're using my framework
8:57
and it's just more accessible which by
Ethics of Web Scraping
8:58
the way if you are curious if you can
9:01
scrape a website there's a lot of Ethics
9:03
behind web scraping typically what you
9:06
can do is go to a website like
9:08
youtube.com and then add robots. text to
9:11
the URL here and this will give you a
9:14
page that tells you their rules for web
9:16
scraping so this says that any agent is
9:19
allowed to scrape YouTube however there
9:22
are certain pages that are not allowed
9:24
and so this is super important to keep
9:26
in mind if you want to be very ethical
9:28
with your web scrap scraping which I
9:29
highly recommend check the websites
9:31
you're scraping for robot. text first
9:34
before you just go ahead and do it like
9:36
GitHub is another good example here
9:38
where they actually say if you want to
9:39
crawl GitHub please contact them first a
9:42
lot of them will be like this so keep
9:44
this in mind I very much owe it to you
9:46
to provide this little segment talking
9:48
about ethics before I dive into the rest
9:50
of the video um it it's very fitting to
9:52
do that because we're talking about uh
9:53
URLs that you can add to pretty much any
9:55
websites you can do/ robots. text or
9:58
the/ sitemap.xml and so we're going to
Crawling Multiple Pages Continued
10:02
in code pull this sit map and then we
10:05
are going to extract every single URL
10:08
and then feed all of those into craw for
10:10
AI and we want to do that very
10:12
efficiently as well cuz right here we're
10:15
just going to be pulling in every URL
10:17
and then looping and going through one
10:19
at a time if we do it just in a loop
10:21
with this code right here we want
10:23
something more efficient and so if we go
10:25
to the documentation for crawl for AI
10:28
which is right here that'll bring us to
10:31
this page right here and if we go down
10:33
to multi URL crawling there is a lot
10:36
that crawl for AI gives us for this and
10:38
that's what we're going to be leveraging
10:39
for the rest of this video so first of
10:42
all if you just crawl your websites in a
10:45
loop like this like we would do if we
10:47
just continued off of this example right
10:49
here it would be very inefficient we're
10:51
spinning up a brand new browser for
10:53
every URL that we are visiting and
10:56
there's no opportunity for parallel
10:58
process processing which we're going to
11:00
get into as well and so their
11:02
recommendation they give a full example
11:04
for this for how you can use the same
11:06
browser session for all of the pages
11:09
that you're visiting and pulling and so
11:11
that brings us to the second script that
11:13
I have built for us here and I'm not
11:15
going to go over all the code in detail
11:17
because this is mostly following the
11:18
example that we just saw right here so I
11:21
just copied this in brought it into my
11:23
code editor and then I have this custom
11:25
function right here where I pull that
11:28
site map that I just showed you so I
11:30
pull it I extract using XML processing
11:34
all the URLs from the sit map and then I
11:37
pass them all into this function to
11:39
crawl the URL sequentially with the same
11:41
browser session and so the code gets a
11:44
little complicated with the browser
11:45
config and crawler config but don't
11:47
worry about that in general you can just
11:49
take this example and use it for
11:51
yourself it crawls every single URL and
11:54
it's not going to print out the content
11:56
of every markdown CU that would just be
11:57
way too much in the terminal it'll just
11:58
show us the length and whether or not it
12:01
succeeded in crawling the site and so
12:03
I'm going to go back to my terminal here
12:05
and run this second script here and it's
12:07
going to take a little bit because it
12:09
has to crawl all of them sequentially
12:11
we'll get into parallel processing next
12:13
to make this even faster but even this
12:15
just took seconds it was so fast
12:18
processing each one of these Pages
12:20
giving me the length and whether is
12:22
success or not for each one of these
FAST Parallel Page Crawling
12:24
URLs so at this point we already have a
12:27
very fast way to get the markdown for
12:29
every single pantic AI documentation
12:31
page and it's ready now for us to put in
12:33
a vector database for rag to use with
12:36
our large language model it's super neat
12:38
and it was so easy to set this up with
12:40
crawl for AI but before we actually get
12:42
into anything with rag I want to take
12:44
this one step further because I want to
12:46
make this even faster it was already
12:49
fast here but we're still processing
12:51
each one of these URLs sequentially
12:54
there's no parallel processing and we
12:56
can definitely do that with crawl for AI
12:59
so we can visit multiple Pages at the
13:01
exact same time pull the mark down for
13:03
every single one of them and then
13:04
combine it all at the end to a single
13:06
list just like we're doing right here
13:08
and so the way that we can do that if I
13:10
go back to the crawl for AI
13:11
documentation and just scroll down a
13:13
little bit they have an example doing
13:16
this exactly this parallel processing
13:18
and it's essentially going to be the
13:20
same we're still just using one browser
13:22
but we're creating different sessions
13:24
that are all going to be up at the same
13:26
time visiting these URLs in parallel and
13:29
just like last time I mostly just copied
13:31
the example that they had right here and
13:33
then brought it into my code editor and
13:35
then again just like last time the main
13:38
thing that I added is that function to
13:40
use the pantic AI sitemap.xml to get all
13:43
the pages that I want to pull the
13:45
markdown for and scrape and so I'm going
13:48
to open up my terminal again and
13:50
actually one last thing before I do that
13:51
for the batch size we are doing 10 so
13:54
it's going to visit 10 pages at the
13:56
exact same time get the markdown for all
13:58
of them and then move on to the next set
14:00
of 10 and then repeat that until it has
14:02
pulled the mark down for every single
14:04
page and so I have a new terminal open
14:07
up right here I'm just going to run this
14:08
script just like I did before and last
14:11
time I showed how fast each run was now
14:13
I'm going to show how memory efficient
14:15
it is so when I run this it'll show the
14:17
current RAM usage for the script which
14:19
it starts at 91 megabytes it's going
14:22
through all these batches very very
14:24
quickly and at the end we can see the
14:26
peak usage which is only 119 megabytes
14:29
so throughout this entire time even
14:31
though there's an entire browser running
14:33
in the background visiting 10 pages at a
14:35
time it's still only ever used 119
14:39
megabytes of memory at once which is
14:41
just
14:42
incredible and the last example was
14:45
actually basically as fast but that's
14:48
only because of caching in general this
14:50
batch processing is going to speed it up
14:52
a ton which is super impressive and so
14:54
now we have the perfect thing for rag
14:57
because we're doing it very very quickly
14:59
and a lot of times you need that I mean
15:00
this example has 42 pages but if you
15:03
have something like an e-commerce store
15:05
with hundreds or thousands of products
15:07
you can imagine that this is going to
15:08
start to be a drag if you are processing
15:11
things sequentially not using the same
15:13
browser and same session that's why
15:15
using crawl for AI and having all these
15:17
efficiencies is so important very last
Crawl4AI RAG AI Agent
15:20
thing and this is my true gift to you I
15:22
have already built out a full rag AI
15:25
agent that is a pantic AI expert so
15:27
using the exact same process with crawl
15:29
for AI that we just did I pulled all of
15:32
the pantic AI documentation and then I
15:34
put it into a vector database for its
15:37
knowledge base built a full agent around
15:39
it and created a front end that we're
15:41
looking at right here and my gift to you
15:43
is this is already available to you I
15:45
have the code in a GitHub repository
15:47
that I have linked below and then in the
15:49
next video on my channel I'll be go
15:51
covering how I actually built this agent
15:54
and it will be available on the live
15:56
Asian studio for you to try immediately
15:58
so super super neat and also a little
16:00
bit of a sneak peek right now so let me
16:02
paste this in here I'll just ask a basic
16:04
question like what are the supported
16:06
models and this is the kind of thing
16:09
that Claude or any other General llm
16:11
would definitely not have the answer for
16:14
and it even links me to the different
16:16
pages in the pantic AI documentation for
16:19
my reference very very neat and I can
16:21
ask a ton of other questions as well
16:23
like I can say something like give me
16:25
the weather agent example for from the
16:29
documentation obviously I just know that
16:31
this agent example exists and so I'll
16:34
ask for it and it'll go and search for
16:35
it find this full example for me and it
16:38
does it so fast as well and this is
16:40
perfect like this is a pretty complex
16:42
example because it's showing me
16:43
basically every part of creating an
16:45
agent with pantic AI which is super
16:48
super neat so there we go this is the
16:50
full agent and I'll be showing you
16:51
exactly how to build it very very soon
16:53
on my channel now the reason that I'm
16:55
not covering how to build the entire
16:57
agent in this video is I want to keep it
16:59
concise and focused on just crawl for AI
17:02
especially because there's a lot of
17:03
other use cases for web scraping besides
17:05
just rag even though rag is definitely
17:07
one of the biggest ones for AI and just
17:10
in general right now but if you go to
17:12
the GitHub repo I have a readme right
17:15
here covering everything with this agent
17:17
you have all the code for my entire
17:19
process of crawling all these sites
17:22
again with a very similar process to
17:23
what we went over in this video and then
17:25
actually inserting that into our Vector
17:28
database which I'm actually using PG
17:29
Vector with superbase here and then I
17:32
have my agent that I built with pantic
17:34
AI very meta but it is my favorite
17:36
framework right now and then I have my
17:38
streamlet interface so all this is
17:40
available for you with instructions on
17:41
how to run it yourself and then also
17:43
stay tuned for my video later this week
17:46
where I'll show you exactly how I built
Outro
17:48
it so there you have it a bulletproof
17:50
lightning fast way to scrape any sight
17:52
and give it to your llm as a knowledge
17:54
base and this is useful for you pretty
17:56
much no matter what your use case is
17:58
because there is almost always a time
18:00
and place to take data from external
18:02
websites and bring that into your llm
18:05
and so that in my mind makes crawl for
18:07
AI a GameChanger and don't get me wrong
18:09
there are a lot of ways to bring
18:11
knowledge into an llm you can manually
18:13
curate data use new advanced concepts
18:16
like KAG a lot of things I'll cover in
18:18
more videos on my channel but it is
18:20
still the most common way to make an AI
18:22
agent and expert at something you care
18:24
about to scrape data from a site and
18:26
provide it to a knowledge base for rag
18:28
and in the next video on my channel I'll
18:30
do a deep dive into the rag AI agent
18:32
that I demoed earlier which I'm super
18:34
excited about because I put a lot of
18:36
effort into building it for you so if
18:38
you appreciated this content I would
18:39
really appreciate a like and a subscribe
18:41
and with that I will see you in the next