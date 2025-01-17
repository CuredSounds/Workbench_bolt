Intro: Building an AI Server for My Daughters
0:00
I built an AI server for my daughters. Well, first it was more for me.
0:03
I wanted to run all of my AI locally.
0:05
And I'm not just talking command line with alama. No, no, no. We have a gui,
0:09
a beautiful chat interface and this thing's feature filled.
0:12
It's got our back chat histories, multiple models,
0:15
we can even add stable diffusion.
0:16
And I was able to add this to my notes application obsidian and have my chat
0:19
interface right there. I'm going to show you how to do this.
0:21
Now you don't need something crazy like Terry, that's what I named my AI server.
0:25
It can be something as simple as this, this laptop,
0:28
I'll actually demo the entire setup on this laptop.
0:30
So likely the computer you're using right now, the one you're watching,
0:32
this video one will probably work. And seriously, you're going to love this.
0:35
It's customizable, it's wicked fast, way faster than anything else I've used.
0:39
Isn't that amazing? And again, it's local, it's private. I control it,
0:43
which is important because I'm getting it to my daughters.
0:45
I want them to be able to use AI to help with school,
0:48
but I don't want them to cheat or do anything else weird.
0:50
But because I have control,
0:52
I can put in special model files that restrict what they can do, they can ask,
0:55
and I'll show you how to do that. So here we go. Get your coffee ready.
0:58
We're about to dive in, but first let me have you meet Terry.
Meet Terry: My Powerful AI Server Build
1:01
Now Terry has a lot of muscle. So for the case, I needed something big.
1:04
I got the Leon Lee zero 11 dynamic EVO xl.
1:07
It's a full tower EATX case perfect to hold my ASUS X six 70 E Creator pro
1:12
art motherboard. This thing's also a beast.
1:14
I'll put it in the description so you can look at it. Now,
1:15
I also gave Terry a big brain. He's got the A MD Ryzen 9 79 50 x.
1:20
That's 4.2 gigahertz and 16 cores. From memory, I went a little crazy.
1:24
I've got 128 gigabytes of the gki trite D five Neo,
1:29
it's DDR R five 6,000 and way overkill for what I'm doing.
1:32
I think I got a Leon Lee water cooler for the CPU.
1:35
I'm not sure if I'm seeing Leon Lee, right? I don't know.
1:37
Correct me in the comments. You always do. And then for the stuff AI loves,
1:40
I got two 40 nineties,
1:42
it's the MSI Sremm and their liquid cooled so they could fit on my motherboard.
1:45
24 gigabytes of memory each giving me plenty of muscle For my AI models for
1:50
storage, we got two Samsung nine 90 pros, two terabytes,
1:53
which you can't see because they're behind stuff.
1:55
And also of Corsair AX 1600 I power supply 1600 watts to power the entire build.
2:00
Terry is ready. Now,
Installing PopOS on the AI Server
2:02
I'm surprised to say my system actually posted on the first attempt,
2:05
which is amazing.
2:06
But what's not amazing is the fact that Ubuntu would not install.
2:09
I tried for hours actually for a whole day and I almost gave up and installed
2:13
Windows, but I said, no, Chuck, you're installing Linux.
2:15
So I tried something new, something I've never messed with before.
2:17
It's called Pop Os by system 76. This thing is awesome.
2:22
It worked the first time.
2:23
It even had a special image with Nvidia drivers built in.
2:26
It just stink and worked. So I sipped some coffee,
2:28
didn't question the magic and moved on.
2:30
Now if you do want to build something similar, I've got all the links below.
2:33
But anyways, let's talk about how to build your very own local AI server.
What You Need to Build Your Own Local AI Server
2:38
First, what do you need? Really all you'll need is a computer. That's it.
2:42
It can be any computer running Windows, Mac or Linux. And if you have a GPU,
2:46
you'll have a much better time. Now, again, I have to emphasize this,
2:49
you won't need something as beefy as Terry,
2:51
but the more powerful your computer is, the better time you'll have.
2:53
Don't come at me with a Chromebook please. Now step one, alama.
Step 1: Installing Ollama AI Foundation
2:58
This is the foundation for all of our AI stuff and what we'll use to run AI
3:01
models.
3:02
So we'll head on over to alama.ai and click on download and they've get a flavor
3:07
for every os. I love that. Now if you're on Mac,
3:10
just download it right now and run it. If you're on Windows,
3:12
they do have a preview version, but I don't want you to do that. Instead,
3:16
I want you to try the Linux version. We can install it with one command.
3:19
And yes, you can run Linux on Windows with WSL. Let's get that going real quick.
3:24
First thing I'll do is go to the start bar and search for terminal and launch my
3:28
terminal.
3:28
Now those first bit is for Windows folks only Linux people to hang on for a
3:31
moment, we got to get WSL installed or the Windows subsystem for Linux.
3:35
It's only one command WSL dash install and that's it.
3:40
Actually hit enter and that's going to start doing some stuff. When it's done,
3:44
we'll set up a username and password. I got a new keyboard by the way.
3:47
Do you hear that link below? It's my favorite keyboard of the entire world.
3:52
Now some of you may have to reboot. That's fine.
3:54
Just pause the video and come back. Mine is ready to go though.
3:56
And we're walking Ubuntu 22.04,
3:59
which is still amazing to me that we're running Linux on Windows.
4:02
That's just magic right now we're about to install Llama, but before we do that,
4:06
you got to do some best practice stuff like updating our packages.
4:09
So we'll do a pseudo a PT update and then we'll do a pseudo A PT
4:15
upgrade Y to apply all those updates.
4:20
And actually while it's updating,
4:21
can I tell you something about our sponsor IT Pro by a CI Learning.
Sponsor: ITPro Training from ACI Learning
4:25
Now in this video, we're going to be doing lots of heavy Linux things.
4:28
I'm going to walk you through it.
4:29
I'm going to hold your hand and you may not really understand what's happening.
4:32
That's where IT pro comes in.
4:34
If you want to learn Linux or really anything in it, they are your go-to,
4:38
that's what I use to learn new stuff.
4:39
So if you want to learn Linux to get better at this stuff or you want to start
4:42
making this whole hobby thing your career, actually learn some skills,
4:45
get some certifications, get your A plus, get your CNA,
4:48
get your AWS certifications,
4:49
your Azure certifications and go down this crazy IT path, which is incredible.
4:53
It's the whole reason I make this channel and make these videos.
4:56
Check out IT Pro they've got IT training that won't put you to sleep.
4:59
They have labs, they have practice exams,
5:01
and if you use my Code network check right now, you'll get 30% off forever.
5:04
So go learn some Linux and thank you to IT Pro for sponsoring this video and
5:07
making things like this possible. And speaking of my updates are done.
5:10
And by the way, I will have a guide for this entire thing. Every step,
5:13
all the commands, you can find it at the Free network Chuck Academy membership.
5:16
Click the link below to join and get some other cool stuff as well.
5:19
I can't wait to see you there. Now we can install llama with one command.
Testing Ollama Installation and Adding Models
5:22
And again, all commands are below.
5:24
It's going to paste this in a nice little curl command,
5:27
little magic stuff and I love how easy this is.
5:29
Watch you just sit there and let it happen.
5:31
Do you not feel like a wizard when you're installing stuff like this and the
5:34
fact that you're installing AI right now? Come on.
5:36
I noticed one thing real quick.
5:38
Old LAMA did automatically find out that I have an Nvidia GPU and it's like
5:42
awesome, you're going to have a great time.
5:44
If it didn't see that and you do have a GPU,
5:46
you may have to install some Nvidia Cuda drivers.
5:48
I'll put a link for that below, but not everyone will have to do that.
5:51
And if you're rocking a Mac with an M1 through M three chip,
5:53
you're going to have a good time too. They'll use the embedded GPU Now at this,
5:57
our Mac users, our Linux users and our Windows users are all converged.
6:00
We're on the same path. Welcome. We can hold hands and sing.
6:05
That's getting weird. Anyways,
6:06
first we have to test a few things to make sure alama is working.
Interacting with Llama2 AI Model Locally
6:09
And for that we're going to open our web browser. I know it's kind of weird,
6:11
just stick with me. I'm going to launch Chrome here and here are my address bar.
6:15
I want to type in local host, which is looking right here at my computer.
6:19
And port 1, 1 4, 3, 4, hit enter.
6:22
And if you see this right here, this message,
6:25
you're good to go and you're about to find this out.
6:27
Port 1 1 4 3 4 is what llama's API services is running on and it's how our other
6:32
stuff is going to interact with it. It's so powerful. Just check this out.
6:35
I'm so excited to show you this. Now before we move on,
6:38
let's go ahead and add an AI model to alama.
6:40
And we can do that right now with alama Pull and we'll pull down Llama two,
6:45
A very popular one. Hit enter and it's ready. Now let's test it out real quick.
6:49
We'll do Alama run Llama two.
6:53
And if this is your first time doing this, this is kind of magic.
6:55
We're about to interact with a chat GPT, like AI right here,
6:59
no internet required. It's all just happening in that five gigabyte file.
7:03
Tell me about the solar eclipse. Boom.
7:08
And you can actually control see that to stop it. Now I want to show you this.
7:11
I'm going to open up a new window.
7:12
This is actually an awesome command and with this WSL command,
7:14
I'm just connecting to the same incident. Again, a new window.
7:17
I'm going to type in watch dash N 0.5,
7:21
not four five Nvidia dash smmi.
7:25
This is going to watch the performance of my GPU right here in the terminal and
7:29
keep refreshing it. So keep an eye on this right here.
7:33
As I chat with llama two,
7:36
give me a list of all Adam Sandler
7:41
movies and look at that GPU Go. Ah,
Comparing AI Performance on Different Hardware
7:46
it's so fun. Now can I show you what Terry does? Real quick?
7:48
I got to show you Terry. Terry has two GPUs here.
7:51
They're right here and Alama can actually use both of them at the same time.
7:56
Check this out. It's so cool.
7:59
All the semi old Jackson movies. And look at that.
8:04
Isn't that amazing? And look how fast it went. That's ridiculous.
8:07
This is just the beginning. So anyways, I had to show you Terry.
8:09
So now we have a llama installed. That's just our base.
8:12
Remember I'm going to say bye. So slash bye to end that session.
8:16
Step two is all about the web ui. And this thing is amazing.
Step 2: Setting Up Open WebUI
8:19
It's called Open Web ui and it's actually one of many web UI you can get for
8:23
Llama, but I think Open Web UI is the best.
8:26
Now Open Web UI will be run inside a Docker container.
8:28
So you will need Docker installed and we'll do that right now.
8:31
So we'll just copy and paste the commands from Network Struck Academy.
8:34
This is also available on Docker's website.
8:37
First step is updating our repositories and getting docker's GPG key.
8:42
And then with one command we will install Docker and all its goodies. Ready,
8:45
set, go. Yes, let's do it. And now with Docker install,
8:49
we'll use it to deploy our open web UI container.
8:52
It'll be one command you can simply copy and paste.
8:55
This Docker Run Command is going to pull this image to run this container from
8:59
Open Web ui. It's looking at your local computer for the llama base,
9:03
URL because it's going to integrate and use Llama and it's going to be using the
9:07
host network adapter to make things nice and easy.
9:10
Keeping in mind this will use Port 80 80 on whatever system you are using.
9:14
And all we have to do is hit enter
9:17
after we add some pseudo at the beginning,
9:20
pseudo docker run and let it do its thing. Let's verify it real quick.
9:24
We'll do a little pseudo docker PS. We can see that it is indeed running.
9:29
And now let's go log in. It's kind of exciting. Okay,
Logging into Open WebUI for the First Time
9:32
let's go to our web browser and we'll simply type in local host
9:37
colon port 80, 80, and whoa, okay, it's really zoomed in.
9:41
I'm not sure why yours shouldn't do that. Now for the first time you run it,
9:45
you'll want to click on sign up right here at the bottom and just put your stuff
9:48
in. This login info is only pertinent to this instance,
9:52
this local instance, we'll create the account and we're logged in.
9:56
Now just so you know,
9:56
the first account you log in with or sign up with will automatically become an
10:00
admin account. So right now, you as a first time user logging in,
10:04
you get the power. But look at this. How amazing is this? Let's play with it.
Admin Panel: User Management and Permissions
10:08
So the first thing we have to do is select the model.
10:10
I'll click that drop down and we should have one llama two. Awesome.
10:14
And that's how we know also our connection is working.
10:16
I'll go ahead and select that. And by the way,
10:17
another way to check your connection is by going to your little icon down here
10:20
at the bottom left and clicking on settings and then connections.
10:24
And you can see our oh LAMA based CRL is right here.
10:26
If you ever have to change that for whatever reason. Now with LAMA two selected,
10:30
we can just start chatting and just like that,
10:34
we have our own little chat,
10:35
GBT that's completely local and this sucker is beautiful and
10:40
extremely powerful. Now, first things we can download more models.
10:43
We can go out to llama and see what they have available.
10:46
Look on their models to see their list of models. Code Gemma is a big one.
10:50
Let's try that. So to add code Gemma, our second model,
10:52
we'll go back to our command line here and type in Alama pull code Gemma.
10:59
Cool, it's done. Once that's pulled,
11:01
we can go up here and just change our model by clicking on the little dropdown
11:04
icon at the top. Yep, there's code gma. We can switch.
Customizing AI Models with Prompts and Restrictions
11:07
And actually I've never done this before,
11:08
so I have no idea what's going to happen.
11:11
I want to click on my original model LAMA two.
11:14
You can actually add another model to this conversation. Now we have two here.
11:18
What's going to happen?
11:21
So code Gemma is answering it first. I'm actually not sure what that does.
11:26
Maybe you guys can try it out and tell me. I want to move on though.
11:29
Now some of the crazy stuff you can see right here,
11:30
it's almost more featured than chat GBT In some ways.
11:34
You got a bunch of options for editing your responses, copying,
11:37
liking and disliking it to help it learn.
11:39
You can also have it read things out to you, continue response,
11:41
regenerate response, or even just add stuff with your own voice.
11:45
I can also go down here and this is crazy.
11:49
I can mention another model and it's going to respond to this and think about
11:53
it. Did you see that? I just had my other model.
11:57
Talk to my current. That's just weird, right?
12:00
Let's try to make 'em have a conversation. They're going to have a conversation.
12:04
What are they going to talk about?
12:05
Let's bring back in LAMA two to ask the question. This is hilarious.
12:10
I love this so much. Okay, anyways, I can spend all day doing this.
12:13
We can also with this plus sign upload files. This includes a lot of things.
12:17
Let's try, do I have any documents here?
12:20
I'll just copy and paste the contents of an article,
12:22
save that and that'll be our file. Summarize this.
12:27
You can see our GPU being used over here. I love that so much. Running locally.
12:31
Cool. We can also add pictures for multimodal models.
12:35
I'm not sure coma can do that. Let's try it out real quick.
12:39
So alama can't do it, but there is a multimodal model called lava.
12:43
Let's pull that down real quick with lava pulled, let's go to our browser here.
12:47
Once more, we'll refresh it, change our model to lava. Add the image.
12:53
That's really scary. There we go. That's pretty cool. Now here in a moment,
12:57
I will show you how we can generate images right here in this web interface by
13:01
using stable diffusion. But first let's play around a bit more.
Step 3: Installing Stable Diffusion with Automatic1111
13:03
And actually the first place I want to go to is the admin panel For you,
13:07
the admin, we have one user and if we click on the top right,
13:10
we have admin settings. Here's where a ton of power comes in first.
13:13
We can restrict people from signing up. We can say enabled or disabled. Now,
13:16
right now, by default it's enabled. That's perfect.
13:18
And when they try to sign up initially,
13:20
there'll be a pending user until you're approved, lemme show you.
13:24
So now real quick,
13:25
if you want to have someone else use this server on your laptop or computer or
13:28
whatever it is,
13:30
they can access it from anywhere as long as they have your IP address.
13:32
So lemme do a new user signup real quick just to show you.
13:35
I'll open an incognito window, create account, and look. It's saying, Hey,
13:39
you got to wait. Your guy has to approve you.
13:41
And if we go here and refresh our page on the dashboard, there is Bernard hack.
13:44
Well, we can say, you know what? He's a user or click it again, he's an admin.
13:48
No, no he's not. He's going to be a user. And if we check again, boom,
13:52
we have access.
13:53
Now what's really cool is if I go to admin settings and I go to users,
13:57
I can say, Hey, you know what? Don't allow Chad deletion, which is good.
14:00
If I'm trying to monitor what my daughters are kind of up to on their chats,
14:04
I can also whitelist models. So you know what,
14:06
they're only allowed to use LAMA two and that's it.
14:09
So when I get back to Bernard hack Well's session over here,
14:12
I should only have access to LAMA two.
14:15
It's pretty sick and it becomes even better when you can make your own models
14:18
that are restricted.
14:19
We're going to mo you on over to the section called model files right up here.
14:23
And we'll click on create a model file.
14:25
You can also go to the community and see what people have created.
14:28
That's pretty cool. I'm going to show you what I've done for my daughter, Chloe,
14:31
to prevent her from cheating. She named her assistant Deborah.
14:34
And here's the content. I'm going to paste it in right now.
14:36
The main thing is up here where it says from, and you choose your model.
14:39
So from llama two. And then you have your system prompt,
14:42
which is going to be between three double quotes.
14:45
And I've got all this telling it what a can and can't do,
14:47
what Chloe's allowed to ask. And it ends down here with three double quotes.
14:51
You can do a few more things. I'm just going to say,
14:52
as an assistant education save and create.
14:55
Then I'll go over to my settings once more and make sure that for the users,
14:58
this model is whitelisted. I'll add one more. Debra Notice she's an option now.
15:03
And if Bernard's going to try and use Debra and say Debra
15:07
paper for me on the Civil War.
15:12
And immediately I was shut down saying, Hey, that's cheating. Now Llama two,
15:16
the model we're using, it's okay. There's a better one called mixed roll Lemme,
15:20
lemme show you Terry. I'll use Deborah or Deb and say,
15:23
write me a paper on Benjamin Franklin.
15:27
I notice how it didn't write it for me, but it says it's going to guide me.
15:31
And that's what I told it to do to be a guide.
15:35
I tried to push it and it said no. So that's pretty cool.
15:38
You can customize these prompts,
15:39
put in some guard rails for people that don't need full access to the kind of
15:42
stuff right now. I think it's awesome. Now,
15:45
OpenWeb UI does have a few more bells and whistles,
15:47
but I want to move on to getting stable diffusion set up.
15:49
This thing is so cool and powerful. Step three, stable diffusion.
Prerequisites and Python Version Management with pyenv
15:54
I didn't think that image generation locally would be as fun or as powerful as
15:58
chat GPT, but it's more, it's crazy. You got to see it.
16:03
Now we'll be installing Stable diffusion with a UI called Automatic 1 1 1 1.
16:08
So let's knock it out. Now before we install it,
16:10
we got some prereqs and one of them is an amazing tool.
16:12
I have been using a lot called PI ENV,
16:15
which helps us manage our Python versions and switch between them,
16:18
which is normally such a pain. Anyways,
16:20
the first thing we got to do is make sure we have a bunch of prerequisites
16:23
installed. Go ahead and copy and paste this from the Network Check Academy.
16:26
Let it do its thing for a bit. And with the prereqs installed,
16:28
we'll copy and paste this command,
16:29
a curl command that'll automatically do everything for us. I love it. Run that.
16:34
And then right here it tells us we need to add all this or just run this command
16:37
to put this in our bash RC file. So we can actually use the pie EMV command.
16:41
I'll just copy this, paste it,
16:44
and then we'll type in source B RC to refresh our
16:49
terminal. And let's see if pi ENV works, PI ENV,
16:52
we'll do a dash H to see if it's up and running. Perfect.
16:56
Now let's make sure we have a version of Python install that we will work for
16:59
most of our stuff. We'll do PI ENV install three point 10.
17:04
This will of course install Python three point 10, the latest version.
17:07
Excellent Python three point 10 is installed.
17:09
We'll make it our global Python by typing in PI ENV global
17:15
three point 10. Perfect.
17:17
And now we're going to install automatic 1, 1, 1, 1.
Installing Automatic1111 Web UI
17:21
The first thing we'll do is make a new directory M-K-D-A-R for make directory,
17:24
we'll call it stable. And then we'll jump in there. CD stable diff.
17:29
And then we'll use this W get command to w get this BS script.
17:35
We'll type it Ls to make sure it's there. There it is.
17:37
Let's go ahead and make that sucker executable by typing in CH mod.
17:40
We'll do a plus x and then web UI sh. Now it's executable.
17:45
Now we can run it. Period slash web ui sh. Ready,
17:50
set, go. This is going to do a lot of stuff.
17:53
It's going to install everything you need for open web ui.
17:56
It's going to install PyTorch and download stable diffusion. It's awesome.
18:01
Again, a little coffee break. Okay, that took a minute,
18:06
a long time. I hope you got plenty of coffee.
18:08
Now it might not seem like it's ready,
18:10
but it actually is running and you'll see the URL pop up around here.
18:14
It's kind of messed up, but it's running on port 78 60. Let's try it out.
18:18
And this is fun. Oh my gosh.
Testing Stable Diffusion Image Generation Locally
18:21
So local host 78 60,
18:25
what you're seeing here is hard to explain. Lemme just show you
18:33
And let's generate, okay, it got confused.
18:38
Lemme take away the MPA Lupa part. But this isn't being sped up.
18:41
This is how fast this is. No, that's a little terrible. What do you say?
18:46
We make it look a little bit better. Okay, that's terrifying.
18:50
But just one of the many things you can do with your own ai.
18:53
Now you can actually download other models.
18:55
Lemme show you what it looks like on Terry and my new editor, Mike, tell me,
18:58
do this. That's weird. Let's make it take more time.
19:02
But look how fast this is.
19:03
It's happening in real time as I'm talking to you right now.
19:06
But if you've ever made images with GT four, it just takes forever.
19:10
But I just love the fact that this is running on my own hardware and it's kind
19:13
of powerful. Lemme know in the comments below, which is your favorite image,
19:17
actually post on Twitter and tag me. This is awesome.
19:21
Now this won't be a deep dive on Stable Diffusion. I barely know what I'm doing.
Integrating Stable Diffusion into Open Web UI
19:24
But let me show you real quick how you can easily integrate automatic
19:27
1, 1 1, 1 1. Did I have to do enough ones? I'm not sure.
19:31
And they're stable diffusion inside Open Web ui.
19:34
So it's just right here back at Open Web ui.
19:36
If we go down to our little settings here and go to settings,
19:39
you'll see an option for images here. We can put our automatic 1 1 1 1 base URL,
19:44
which will simply be HTTP colon whack wack
19:47
1 2 7 0 0 1,
19:49
which is the same as saying local host Port 78. What is it?
19:53
0 6 60 60 think is what it's,
19:56
we'll hit the refresh option over here to make sure it works.
19:59
And actually no it didn't. And here's why.
20:01
There's one more thing you got to know.
20:03
Here we have OpenWeb UI running in our terminal.
20:06
The head control C is going to stop it from running.
20:08
In order to make it work with open web ui,
20:10
we got to use two switches to make it work.
20:14
So let's go ahead and run our script one more time. Open web UI or web UI sh.
20:18
And we'll do dash listen and dash API Once we see
20:23
the URL come up. Okay, cool, it's running. We can go back over here and say,
20:27
why don't you try that again buddy? Perfect.
20:29
And then over here we have image Generation experimental.
20:32
They're still trying it out. We'll say on and we'll say save.
20:36
So now if we go to any prompt,
20:37
let's do a new chat and we'll chat with llama two. I'll say,
20:42
describe a man in a dog suit.
20:47
This is for a stable diffusion prompt.
20:53
A bit wordy for my taste. But then notice we have a new icon. This is so neat.
20:57
Boom. An image icon.
20:59
And all we have to do is click on that to generate an image based on that
21:02
prompt. I clicked on it, it's doing it. And there it is right in line.
21:07
That is so cool. And that's really terrifying. I love this. It's so fun.
21:12
Now this video is getting way too long,
21:13
but there are still two more things I want to show you.
21:15
I'm going to do that really quickly right now. The first one is,
Bonus 1: Using Documents for Context in Open Web UI
21:18
it's just magic. Check it out. There's another option here inside Open Web ui,
21:22
a little section right here called Documents. Here.
21:24
We can simply just add a document.
21:26
I'll add that one from before it's there available for us.
21:30
And now when we have a new chat, I'll chat with Code Gemma.
21:33
All I have to do is do a hashtag and say,
21:36
let's talk about this and say,
21:38
give me five bullet points about this.
21:43
Cool. Give me three social media posts. Okay, go Gemma.
21:48
Lemme try it again. What just happened? Okay,
21:52
let's do a new prop. Oh, there we go. And I'm just scratching the surface.
21:57
Now the second thing I want to show you, last thing. I am a huge obsidian nerd.
Bonus 2: Integrating Local AI with Obsidian Note-Taking
22:01
It's my notes application. It's what I use for everything.
22:04
It's been very recent. I haven't made a video about it, but I plan to.
22:06
But one of the cool things about this,
22:08
this very local private notes taking application is that you can add your own
22:12
local GBT to it, like what we just deployed. Check this out.
22:16
I'm going to go to settings. I'll go to community plugins. I'll browse for one.
22:20
I'm going to search for one called B-M-O-B-M-O Chatbot.
22:24
I'm going to install that, enable it. And then I'm going to go to settings.
22:28
I'll have BMO chatbots. And right here I can have an Alama connection,
22:31
which is going to connect to let's say Terry.
22:34
So I'll connect 'em to Terry and I'll choose my model. I'll use Llama two,
22:38
why not? And now right here in my note,
22:41
I can have a chat bot come right over here to the side and say like,
22:46
Hey, how's it going? And I can do things like look at the help file,
22:49
see what I can use here. Ooh, turn on reference.
22:52
So I'm going to say reference on,
22:54
it's now going to reference the current note I'm in.
22:57
Tell me about the system prompt.
23:02
Yep, there it is.
23:03
And it's actually going through and telling me about the note I'm in.
23:05
So I have a chat bot right there,
23:07
always available for me to ask questions about what I'm doing.
23:10
And I can even go in here and go highlight this,
23:14
do a little prompt,
23:15
select generate it's generating right now and just generate some stuff for me.
23:19
I'm going to undo that. Let me do another note.
23:22
So I want to tell a story about a man in a dog suit.
23:25
I'll quickly talk to my chat bot and start to do some stuff that's pretty crazy.
23:29
And this I think for me is just scratching the surface of running local AI
23:35
private in your home on your own hardware.
Wrap-up: The Power and Potential of Local AI
23:37
This is seriously so powerful and I can't wait to do more stuff with this. Now.
23:40
I would love to hear what you've done with your own projects.
23:42
If you attempted this, if you have this running in your lab,
23:45
let me know in the comments below. Also,
23:47
do you know of any other cool projects I can try that I can make a video about?
23:50
I will love to hear that. I think AI is just the coolest thing,
23:53
but also privacy is a big concern for me.
23:55
So to be able to run AI locally and play with it this way is just the best
24:00
thing ever. Anyways, that's all I got.
24:02
If you want to continue the conversation and talk more about this,
24:04
please check out our Discord community.
24:06
The best way to join that is to jump through our Network Check Academy
24:09
membership, the free one. And if you do want to join the paid version,
24:12
we do have some extra stuff for you there too,
24:13
and it'll help support what we do here.
24:15
But I'd love to hang out with you and talk more. That's all I got.
24:18
I'll catch you guys next time. I.

