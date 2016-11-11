1 Welcome to Sonic Pi

# Welcome friend :-)

Welcome to Sonic Pi. Hopefully you're as excited to get started making
crazy sounds as I am to show you. It's going to be a really *fun* ride
where you'll learn all about music, synthesis, programming, composition,
performance and more.

But wait, how rude of me! Let me introduce myself - I'm
[Sam Aaron](http://twitter.com/samaaron) - the chap that created Sonic
Pi. You can find me at [@samaaron](http://twitter.com/samaaron) on
Twitter and I'd be more than happy to say hello to you.  You might also
be interested in finding out more about my
[Live Coding Performances](http://facebook.com/livecodersamaaron) where
I code with Sonic Pi live in front of audiences.

If you have any thoughts, or ideas for improving Sonic Pi - please
pass them on - feedback is so helpful. You never know, your idea might
be the next big feature!

This tutorial is divided up into sections grouped by category. Whilst
I've written it to have an easy learning progression from start to
finish, feel very free just to dip in and out of sections as you see
fit. If you feel that there's something missing, do let me know and I'll
consider it for a future version.

Finally, watching others live code is a really great way to learn. I
regularly stream live on
[livecoding.tv/samaaron](http://livecoding.tv/samaaron) so please do
drop by, say hi and ask me lots of questions :-)

OK, let's get started...
1.1 Live Coding

# Live Coding

One of the most exciting aspects of Sonic Pi is that it enables you to
write and *modify code live* to make music, just like you might perform
live with a guitar. This means that given some practice you can take
Sonic Pi on stage and gig with it.

## Free your mind

Before we get into the real details of how Sonic Pi works in the rest of
this tutorial, I'd like to give you an experience of what it's like to
live code. Don't worry if you don't understand much (or any) of
this. Just try to hold onto your seats and enjoy...

## A live loop

Let's get started, copy the following code into an empty buffer above:

```
live_loop :flibble do
  sample :bd_haus, rate: 1
  sleep 0.5
end
```

Now, press the `Run` button and you'll hear a nice fast bass drum
beating away. If at any time you wish to stop the sound just hit the
`Stop` button. Although don't hit it just yet... Instead, follow these steps:

1. Make sure the bass drum sound is still running
2. Change the `sleep` value from `0.5` to something higher like `1`.
3. Press the `Run` button again
4. Notice how the drum speed has changed.
5. Finally, *remember this moment*, this is the first time you've live
   coded with Sonic Pi and it's unlikely to be your last...

Ok, that was simple enough. Let's add something else into the mix. Above
`sample :bd_haus` add the line `sample :ambi_choir, rate: 0.3`. Your
code should look like this:


```
live_loop :flibble do
  sample :ambi_choir, rate: 0.3
  sample :bd_haus, rate: 1
  sleep 1
end
```

Now, play around. Change the rates - what happens when you use high
values, or small values or negative values? See what happens when you
change the `rate:` value for the `:ambi_choir` sample just slightly (say
to 0.29). What happens if you choose a really small `sleep` value? See
if you can make it go so fast your computer will stop with an error
because it can't keep up (if that happens, just choose a bigger `sleep`
time and hit `Run` again).

Try commenting one of the `sample` lines out by adding a `#` to the
beginning:

```
live_loop :flibble do
  sample :ambi_choir, rate: 0.3
#  sample :bd_haus, rate: 1
  sleep 1
end

```

Notice how it tells the computer to ignore it, so we don't hear it. This
is called a comment. In Sonic Pi we can use comments to remove and add
things into the mix.

Finally, let me leave you something fun to play with. Take the code below,
and copy it into a spare buffer. Now, don't try to understand it too
much other than see that there are two loops - so two things going round
at the same time. Now, do what you do best - experiment and play
around. Here are some suggestions:

* Try changing the blue `rate:` values to hear the sample sound change.
* Try changing the `sleep` times and hear that both loops can spin round
  at different rates.
* Try uncommenting the sample line (remove the `#`) and enjoy the sound
  of the guitar played backwards.
* Try changing any of the blue `mix:` values to numbers between `0` (not
  in the mix) and `1` (fully in the mix).


Remember to press `Run` and you'll hear the change next time the loop
goes round. If you end up in a pickle, don't worry - hit `Stop`, delete
the code in the buffer and paste a fresh copy in and you're ready to
jam again. Making mistakes is how you'll learn the quickest...


```
live_loop :guit do
  with_fx :echo, mix: 0.3, phase: 0.25 do
    sample :guit_em9, rate: 0.5
  end
#  sample :guit_em9, rate: -0.5
  sleep 8
end

live_loop :boom do
  with_fx :reverb, room: 1 do
    sample :bd_boom, amp: 10, rate: 1
  end
  sleep 8
end
```

Now, keep playing and experimenting until your curiosity about how this
all actually works kicks in and you start wondering what else you can do
with this. You're now ready to read the rest of the tutorial.

So what are you waiting for...
1.2 Exploring the Interface

# The Sonic Pi Interface

Sonic Pi has a very simple interface for coding music. Let's spend a
little time exploring it.

![Sonic Pi Interface](../images/tutorial/GUI.png)


* *A* - Play Controls
* *B* - Editor Controls
* *C* - Info and Help
* *D* - Code Editor
* *E* - Prefs Panel
* *F* - Log Viewer
* *G* - Help System


## A. Play Controls

These pink buttons are the main controls for starting and stopping
sounds. There's the *Run* button for running the code in the editor,
*Stop* for stopping all running code, *Save* for saving the code to an
external file and *Record* to create a recording (a WAV file) of the
sound playing.

## B. Editor Controls

These orange buttons allow you to manipulate the code editor. The *Size
+* and *Size -* buttons allow you to make the text bigger and
smaller. The *Align* button will neaten the code for you to make it look
more professional.

## C. Info and Help

These blue buttons give you access to information, help and
preferences. The *Info* button will open up the information window which
contains information about Sonic Pi itself - the core team, history,
contributors and community. The *Help* button toggles the help system
(*F*) and the *Prefs* button toggles the preferences window which allows
you to control some basic system parameters.

## D. Code Editor

This is the area where you'll write your code and compose/perform
music. It's a simple text editor where you can write code, delete it,
cut and paste, etc. Think of it like a very basic version of Word or
Google Docs. The editor will automatically colour words based on their
meaning in the code. This may seem strange at first, but you'll soon
find it very useful. For example, you'll know something is a number
because it is blue.

## E. Prefs Panel

Sonic Pi supports a number of tweakable preferences which can be
accessed by toggling the *prefs* button in the Info and Help button
set. This will toggle the visibility of the Prefs Panel which includes a
number of options to be changed. Examples are forcing mono mode,
inverting stereo, Toggling log output verbosity and also a volume slider
and audio selector on the Raspberry Pi.

## F. Log Viewer

When you run your code, information about what the program is doing will
be displayed in the log viewer. By default, you'll see a message for
every sound you create with the exact time the sound was triggered. This
is very useful for debugging your code and understanding what your code
is doing.

## G. Help System

Finally, one of the most important parts of the Sonic Pi interface is
the help system which appears at the bottom of the window. This can be
toggled on and off by clicking on the blue *Help* button. The help
system contains help and information about all aspects of Sonic Pi
including this tutorial, a list of available synths, samples, examples,
FX and a full list of all the functions Sonic Pi provides for coding
music.
1.3 Learning through Play

# Learning through Play

Sonic Pi encourages you to learn about both computing and music through
play and experimentation. The most important thing is that you're having
fun, and before you know it you'll have accidentally learned how to
code, compose and perform.

## There are no mistakes

Whilst we're on this subject, let me just give you one piece of advice
I've learned over my years of live coding with music - *there are no
mistakes, only opportunities*. This is something I've often heard in
relation to jazz but it works equally well with live coding. No matter
how experienced you are - from a complete beginner to a seasoned
Algoraver, you'll run some code that has a completely unexpected
outcome. It might sound insanely cool - in which case run with
it. However, it might sound totally jarring and out of place. It doesn't
matter that it happened - what matters is what you do next with it. Take
the sound, manipulate it and morph it into something awesome. The crowd
will go *wild*.

## Start Simple

When you're learning, it's tempting to want to do amazing things
*now*. However, just hold that thought and see it as a distant goal to
reach *later*. For now, instead think of the *simplest* thing you could
write which would be fun and rewarding that's a small step towards the
amazing thing you have in your head. Once you have an idea about that
simple step, then try and build it, play with it and then see what new
ideas it gives you. Before long you'll be too busy having fun and making
real progress. 

Just make sure to share your work with others!
2 Synths

# Synths

OK, enough of the intros - let's get into some sound.

In this section we'll cover the basis of triggering and manipulating
synths. Synth is short for synthesiser which is a fancy word for
something which creates sounds. Typically synths are quite complicated
to use - especially analog synths with many patch wires and
modules. However, Sonic Pi gives you much of that power in a very simple
and approachable manner. 

Don't be fooled by the immediate simplicity of Sonic Pi's interface. You
can get very deep into very sophisticated sound manipulation if that's
your thing. Hold on to your hats...
2.1 Your First Beeps

# Your First Beeps

Take a look at the following code:

```
play 70
```

This is where it all starts. Go ahead, copy and paste it into the code
window at the top of the app (the big white space under the Run
button). Now, press Run...

## Beep!

Intense. Press it again. And again. *And again...*

Woah, crazy, I'm sure you could keep doing that all day. But wait,
before you lose yourself in an infinite stream of beeps, try changing
the number:

```
play 75
```

Can you hear the difference? Try a lower number:

```
play 60

```

So, lower numbers make lower pitched beeps and higher numbers make
higher pitched beeps. Just like on a piano, the keys at the lower part
of the piano (the left hand side) play lower notes and the keys on the
higher part of the piano (the right hand side) play higher notes. In
fact, the numbers actually relate to notes on the piano. `play 47`
actually means play the 47th note on the piano. Which means that `play 48`
is one note up (the next note to the right). It just so happens that
the 4th octave C is number 60. Go ahead and play it: `play 60`.

*Don't worry* if this means nothing to you - it didn't to me when I
 first started. All that matters right now is that you know that *low
 numbers make lower beeps* and *high numbers make higher beeps*.

## Chords

Playing a note is quite fun, but playing many at the same time can be
even better. Try it:

```
play 72
play 75
play 79
```

Jazzy! So, when you write multiple `play`s, they all play at the same
time. Try it for yourself - which numbers sound good together? Which
sound terrible? Experiment, explore and find out for yourself.

## Melody

So, playing notes and chords is fun - but how about a melody? What if
you wanted to play one note after another and not at the same time?
Well, that's easy, you just need to `sleep` between the notes:

```
play 72
sleep 1
play 75
sleep 1
play 79
```

How lovely, a little arpeggio. So what does the `1` mean in `sleep 1`?
Well it means the *duration of the sleep*. It actually means sleep for
one beat, but for now we can think about it as sleeping for 1
second. So, what if we wanted to make our arpeggio a little faster?
Well, we need to use shorter sleep values. What about a half i.e. `0.5`:

```
play 72
sleep 0.5
play 75
sleep 0.5
play 79
```

Notice how it plays faster. Now, try for yourself, change the times -
use different times and notes.

One thing to try is in-between notes such as `play 52.3` and `play 52.63`. 
There's absolutely no need to stick to standard whole notes. Play 
around and have fun.


## Traditional Note Names

For those of you that already know some musical notation (don't worry if
you don't - you don't need it to have fun) you might want to write a
melody using note names such as C and F# rather than numbers. Sonic Pi
has you covered. You can do the following:

```
play :C
sleep 0.5
play :D
sleep 0.5
play :E
```

Remember to put the colon `:` in front of your note name so that it
goes pink. Also, you can specify the octave by adding a number after
the note name:

```
play :C3
sleep 0.5
play :D3
sleep 0.5
play :E4
```

If you want to make a note sharp, add an `s` after the note name such as
`play :Fs3` and if you want to make a note flat, add a `b` such as `play :Eb3`.

Now go *crazy* and have fun making your own tunes.
2.2 Synth Options

# Synth Options: Amp and Pan

As well as allowing you to control which note to play or which sample to
trigger, Sonic Pi provides a whole range of options to craft and
control the sounds. We'll be covering many of these in this tutorial and
there's extensive documentation for each in the help system. However,
for now we'll introduce two of the most useful: *amplitude* and *pan*.
First, let's look at what options actually are.


## Options

Sonic Pi supports the notion of options (or opts for short) for its
synths. Opts are controls you pass to `play` which modify and
control aspects of the sound you hear. Each synth has its own set of
opts for finely tuning its sound. However, there are common sets
of opts shared by many sounds such as `amp:` and envelope
opts (covered in another section).

Opts have two major parts, their name (the name of the control) and
their value (the value you want to set the control at). For example, you
might have a opt called `cheese:` and want to set it with a value
of `1`.

Opts are passed to calls to `play` by using a comma
`,` and then the name of the opt such as `amp:` (don't forget the
colon `:`) and then a space and the value of the opt. For example:

```
play 50, cheese: 1
```

(Note that `cheese:` isn't a valid opt, we're just using it as an example).

You can pass multiple opts by separating them with a comma:

```
play 50, cheese: 1, beans: 0.5
```

The order of the opts doesn't matter, so the following is identical:

```
play 50, beans: 0.5, cheese: 1
```

Opts that aren't recognised by the synth are just ignored (like
`cheese` and `beans` which are clearly ridiculous opt names!)

If you accidentally use the same opt twice with different values, the
last one wins. For example, `beans:` here will have the value 2 rather
than 0.5:

```
play 50, beans: 0.5, cheese: 3, eggs: 0.1, beans: 2
```

Many things in Sonic Pi accept opts, so just spend a little time
learning how to use them and you'll be set! Let's play with our first
opt: `amp:`.

## Amplitude

Amplitude is a computer representation of the loudness of a sound. A
*high amplitude produces a loud sound* and a *low amplitude produces a
quiet sound*. Just as Sonic Pi uses numbers to represent time and notes,
it uses numbers to represent amplitude. An amplitude of 0 is silent
(you'll hear nothing) whereas an amplitude of 1 is normal volume. You
can even crank up the amplitude higher to 2, 10, 100. However, you
should note that when the overall amplitude of all the sounds gets too
high, Sonic Pi uses what's called a compressor to squash them all to
make sure things aren't too loud for your ears. This can often make the
sound muddy and strange. So try to use low amplitudes, i.e. in the range
0 to 0.5 to avoid compression.


## Amp it up

To change the amplitude of a sound, you can use the `amp:`
opt. For example, to play at half amplitude pass 0.5:

```
play 60, amp: 0.5
```

To play at double amplitude pass 2:

```
play 60, amp: 2
```

The `amp:` opt only modifies the call to `play` it's associated
with. So, in this example, the first call to play is at half volume and
the second is back to the default (1):

```
play 60, amp: 0.5
sleep 0.5
play 65
```

Of course, you can use different `amp:` values for each call to play:

```
play 50, amp: 0.1
sleep 0.25
play 55, amp: 0.2
sleep 0.25
play 57, amp: 0.4
sleep 0.25
play 62, amp: 1
```

## Panning

Another fun opt to use is `pan:` which controls the panning of a
sound in stereo. Panning a sound to the left means that you hear it out
of the left speaker, and panning it to the right means you hear it out
of your right speaker. For our values, we use a -1 to represent fully
left, 0 to represent center and 1 to represent fully right in the stereo
field. Of course, we're free to use any value between -1 and 1 to
control the exact positioning of our sound.

Let's play a beep out of the left speaker:

```
play 60, pan: -1
```

Now, let's play it out of the right speaker:

```
play 60, pan: 1
```

Finally let's play it back out of the center of both (the default
position):

```
play 60, pan: 0
```

Now, go and have fun changing the amplitude and panning of your sounds!
2.3 Switching Synths

# Switching Synths

So far we've had quite a lot of fun making beeps. However, you're
probably starting to get bored of the basic beep noise. Is that all
Sonic Pi has to offer? Surely there's more to live coding than just
playing beeps? Yes there is, and in this section we'll explore the
exciting range of sounds that Sonic Pi has to offer.

## Synths

Sonic Pi has a range of instruments it calls synths which is *short for
synthesisers*. Whereas samples represent pre-recorded sounds, synths are
capable of generating new sounds depending on how you control them
(which we'll explore later in this tutorial). Sonic Pi's synths are very
powerful and expressive and you'll have a lot of fun exploring and
playing with them. First, let's learn how to select the current synth to
use.

## Buzzy saws and prophets

A fun sound is the *saw wave* - let's give it a try:

```
use_synth :saw
play 38
sleep 0.25
play 50
sleep 0.25
play 62
sleep 0.25
```

Let's try another sound - the *prophet*:

```
use_synth :prophet
play 38
sleep 0.25
play 50
sleep 0.25
play 62
sleep 0.25
```

How about combining two sounds. First one after another:

```
use_synth :saw
play 38
sleep 0.25
play 50
sleep 0.25
use_synth :prophet
play 57
sleep 0.25

```

Now at the same time:

```
use_synth :tb303
play 38
sleep 0.25
use_synth :dsaw
play 50
sleep 0.25
use_synth :prophet
play 57
sleep 0.25
```

Notice that the `use_synth` command only affects the following calls to
`play`. Think of it like a *big switch* - new calls to `play` will play
whatever synth it's currently pointing to. You can move the switch to a
new synth with `use_synth`.


## Discovering Synths

To see which synths Sonic Pi has for you to play with take a look at the
Synths option in the far left vertical menu (above Fx). There are
over 20 to choose from. Here are a few of my favourites:

* `:prophet`
* `:dsaw`
* `:fm`
* `:tb303`
* `:pulse`

Now play around with *switching synths during your music*. Have fun
combining synths to make new sounds as well as using different synths
for different sections of your music.
2.4 Duration with Envelopes

# Duration with Envelopes

In an earlier section, we looked at how we can use the `sleep` command
to control when to trigger our sounds. However, we haven't yet been able
to control the duration of our sounds.

In order to give us a simple, yet powerful means of *controlling the
duration* of our sounds, Sonic Pi provides the notion of an *ADSR
amplitude envelope* (we'll cover what ADSR means later in this
section). An amplitude envelope offers two useful aspects of control:

* control over the duration of a sound
* control over the amplitude of a sound

## Duration

The duration is the length the sound lasts for. A longer duration means
that you hear the sound for longer. Sonic Pi's sounds all have a
controllable amplitude envelope, and the total duration of that envelope
is the duration of the sound. Therefore, by controlling the envelope you
control the duration.

## Amplitude

The ADSR envelope not only controls duration, it also gives you *fine
control over the amplitude of the sound*. All audible sounds start and
end silent and contain some non-silent part in-between. Envelopes allow
you to slide and hold the amplitude of non-silent parts of the
sound. It's like giving someone instructions on how to turn up and down
the volume of a guitar amplifier. For example you might ask someone to
"start at silence, slowly move up to full volume, hold it for a bit,
then quickly fall back to silence." Sonic Pi allows you to program
exactly this behaviour with envelopes.

Just to recap, as we have seen before, an amplitude of 0 is silence and
an amplitude of 1 is normal volume.

Now, let us look at each of the parts of the envelopes in turn.

## Release Phase

The only part of the envelope that's used by default is the release
time. This is the time it takes for the synth's sound to fade out. All
synths have a release time of 1 which means that by default they have a
duration of 1 beat (which at the default BPM of 60 is 1 second):

```
play 70
```

The note will be audible for 1 second.  Go ahead and time it :-) This is
short hand for the longer more explicit version:

```
play 70, release: 1
```

Notice how this sounds exactly the same (the sound lasts for one
second). However, it's now very easy to change the duration by modifying
the value of the `release:` opt:


```
play 60, release: 2
```

We can make the synth sound for a very short amount of time by using a
very small release time:

```
play 60, release: 0.2
```

The duration of the release of the sound is called the *release phase*
and by default is a linear transition (i.e. a straight line). The
following diagram illustrates this transition:

![release envelope](../images/tutorial/env-release.png)

The vertical line at the far left of the diagram shows that the sound
starts at 0 amplitude, but goes up to full amplitude immediately (this
is the attack phase which we'll cover next). Once at full amplitude it
then moves in a straight line down to zero taking the amount of time
specified by `release:`.  *Longer release times produce longer synth
fade outs.*

You can therefore change the duration of your sound by changing the
release time. Have a play adding release times to your music.

## Attack Phase

By default, the *attack phase* is 0 for all synths which means they move
from 0 amplitude to 1 immediately. This gives the synth an initial
percussive sound. However, you may wish to fade your sound in. This can
be achieved with the `attack:` opt. Try fading in some sounds:

```
play 60, attack: 2
sleep 3
play 65, attack: 0.5
```

You may use multiple opts at the same time. For example for a short
attack and a long release try:

```
play 60, attack: 0.7, release: 4
```

This short attack and long release envelope is illustrated in the
following diagram:

![attack release envelope](../images/tutorial/env-attack-release.png)

Of course, you may switch things around. Try a long attack and a short
release:

```
play 60, attack: 4, release: 0.7
```

![long attack short release envelope](../images/tutorial/env-long-attack-short-release.png)

Finally, you can also have both short attack and release times for
shorter sounds.

```
play 60, attack: 0.5, release: 0.5
```

![short attack short release envelope](../images/tutorial/env-short-attack-short-release.png)

## Sustain Phase

In addition to specifying attack and release times, you may also specify
a sustain time to control the *sustain phase*. This is the time for
which the sound is maintained at full amplitude between the attack and
release phases.

```
play 60, attack: 0.3, sustain: 1, release: 1
```

![ASR envelope](../images/tutorial/env-attack-sustain-release.png)

The sustain time is useful for important sounds you wish to give full
presence in the mix before entering an optional release phase. Of
course, it's totally valid to set both the `attack:` and `release:` opts
to 0 and just use the sustain to have absolutely no fade in or fade out
to the sound. However, be warned, a release of 0 can produce clicks in
the audio and it's often better to use a very small value such as 0.2.


## Decay Phase

For an extra level of control, you can also specify a decay time. This
is a phase of the envelope that fits between the attack and sustain
phases and specifies a time where the amplitude will drop from the
`attack_level:` to the `decay_level:` (which unless you explicitly set
it will be set to the `sustain_level:`). By default, the `decay:` opt is
0 and both the attack and sustain levels are 1 so you'll need to specify
them for the decay time to have any effect:

```
play 60, attack: 0.1, attack_level: 1, decay: 0.2, sustain_level: 0.4, sustain: 1, release: 0.5
```

![ADSR envelope](../images/tutorial/env-attack-decay-sustain-release.png)


## Decay Level

One last trick is that although the `decay_level:` opt defaults to be
the same value as `sustain_level:` you can explicitly set them to
different values for full control over the envelope. This allows you to
to create envelopes such as the following:

```
play 60, attack: 0.1, attack_level: 1, decay: 0.2, decay_level: 0.3, sustain: 1, sustain_level: 0.4, release: 0.5
```

![ASR envelope](../images/tutorial/env-decay-level.png)

It's also possible to set the `decay_level:` to be higher than `sustain_level:`:

```
play 60, attack: 0.1, attack_level: 0.1, decay: 0.2, decay_level: 1, sustain: 0.5, sustain_level: 0.8, release: 1.5
```

![ASR envelope](../images/tutorial/env-decay-level-2.png)

## ADSR Envelopes

So to summarise, Sonic Pi's ADSR envelopes have the following phases:

1. *attack* - time from 0 amplitude to the `attack_level`,
2. *decay* - time to move amplitude from `attack_level` to `decay_level`,
3. *sustain* - time to move the amplitude from `decay_level` to `sustain_level`,
4. *release* - time to move amplitude from `sustain_level` to 0

It's important to note that the duration of a sound is the summation of
the times of each of these phases. Therefore the following sound will
have a duration of 0.5 + 1 + 2 + 0.5 = 4 beats:

```
play 60, attack: 0.5, attack_level: 1, decay: 1, sustain_level: 0.4, sustain: 2, release: 0.5
```

Now go and have a play adding envelopes to your sounds...
3 Samples

# Samples

Another great way to develop your music is to use pre-recorded
sounds. In great hip-hop tradition, we call these pre-recorded sounds
*samples*. So, if you take a microphone outside, go and record the gentle
sound of rain hitting canvas, you've just created a sample.

Sonic Pi lets you do lots of fun things with samples. Not only does it
ship with over 90 public domain samples ready for you to jam with, it
lets you play and manipulate your own. Let's get to it...
3.1 Triggering Samples

# Triggering Samples

Playing beeps is only the beginning. Something that's a lot of fun is
triggering pre-recorded samples. Try it:

```
sample :ambi_lunar_land
```

Sonic Pi includes many samples for you to play with. You can use them
just like you use the `play` command. To play multiple samples and notes
just write them one after another:

```
play 36
play 48
sample :ambi_lunar_land
sample :ambi_drone
```

If you want to space them out in time, use the `sleep` command:

```
sample :ambi_lunar_land
sleep 1
play 48
sleep 0.5
play 36
sample :ambi_drone
sleep 1
play 36
```

Notice how Sonic Pi doesn't wait for a sound to finish before starting
the next sound. The `sleep` command only describes the separation of the
*triggering* of the sounds. This allows you to easily layer sounds
together creating interesting overlap effects. Later in this tutorial
we'll take a look at controlling the *duration* of sounds with
envelopes.


## Discovering Samples

There are two ways to discover the range of samples provided in Sonic
Pi. First, you can use this help system. Click on Samples in the far
left vertical menu, choose your category and then you'll see a list of
available sounds.

Alternatively you can use the *auto-completion system*. Simply type the
start of a sample group such as: `sample :ambi_` and you'll see a
drop-down of sample names appear for you to select. Try the following
category prefixes:

* `:ambi_` 
* `:bass_`
* `:elec_`
* `:perc_`
* `:guit_`
* `:drum_`
* `:misc_`
* `:bd_`

Now start mixing samples into your compositions!
3.2 Sample Parameters

# Sample Parameters: Amp and Pan

As we saw with synths, we can easily control our sounds with
parameters. Samples support exactly the same parameterisation
mechanism. Let's revisit our friends `amp:` and `pan:`.

## Amping samples

You can change the amplitude of samples with exactly the same
approach you used for synths:

```
sample :ambi_lunar_land, amp: 0.5
```

## Panning samples

We're also able to use the `pan:` parameter on samples. For example,
here's how we'd play the amen break in the left ear and then half way
through play it again through the right ear:

```
sample :loop_amen, pan: -1
sleep 0.877
sample :loop_amen, pan: 1
```

Note that 0.877 is half the duration of the `:loop_amen` sample in
seconds.

Finally, note that if you set some synth defaults with
`use_synth_defaults` (which we will discuss later), these will be
ignored by `sample`.
3.3 Stretching Samples

# Stretching Samples

Now that we can play a variety of synths and samples to create some music,
it's time to learn how to modify both the synths and samples to make the
music even more unique and interesting. First, let's explore the ability
to *stretch* and *squash* samples.

## Sample Representation

Samples are pre-recorded sounds stored as numbers which represent how to
move the speaker cone to reproduce the sound. The speaker cone can move
in and out, and so the numbers just need to represent how far in and out
the cone needs to be for each moment in time. To be able to faithfully
reproduce a recorded sound the sample typically needs to store many
thousands of numbers per second! Sonic Pi takes this list of numbers and
feeds them at the right speed to move your computer's speaker in and out
in just the right way to reproduce the sound. However, it's also fun to
change the speed with which the numbers are fed to the speaker to change
the sound.

## Changing Rate

Let's play with one of the ambient sounds: `:ambi_choir`. To play it
with the default rate, you can pass a `rate:` opt to `sample`:

```
sample :ambi_choir, rate: 1
```

This plays it at normal rate (1), so nothing special yet. However, we're
free to change that number to something else. How about `0.5`:

```
sample :ambi_choir, rate: 0.5
```

Woah! What's going on here? Well, two things. Firstly, the sample takes
twice as long to play, secondly the sound is an octave lower. Let's
explore these things in a little more detail.

## Let's stretch

A sample that's fun to stretch and compress is the Amen Break. At normal
rate, we might imagine throwing it into a *drum 'n' bass* track:

```
sample :loop_amen
```

However by changing the rate we can switch up genres. Try half speed for
*old school hip-hop*:

```
sample :loop_amen, rate: 0.5
```

If we speed it up, we enter *jungle* territory: 

```
sample :loop_amen, rate: 1.5
```

Now for our final party trick - let's see what happens if we use a
negative rate:

```
sample :loop_amen, rate: -1
```

Woah! It plays it *backwards*! Now try playing with lots of different
samples at different rates. Try very fast rates. Try crazy slow
rates. See what interesting sounds you can produce.

## A Simple Explanation of Sample Rate

A useful way to think of samples is as springs. Playback rate is like
squashing and stretching the spring. If you play the sample at rate 2,
you're *squashing the spring* to half its normal length. The sample
therefore takes half the amount of time to play as it's shorter. If you
play the sample at half rate, you're *stretching the spring* to double
its length. The sample therefore takes twice the amount of time to play
as it's longer. The more you squash (higher rate), the shorter it gets,
the more you stretch (lower rate), the longer it gets.

Compressing a spring increases its density (the number of coils per cm)
- this is similar to the sample sounding *higher pitched*. Stretching
the spring decreases its density and is similar to the sound having a
*lower pitch*.


## The Maths Behind Sample Rate

(This section is provided for those that are interested in the
details. Please feel free to skip it...)

As we saw above, a sample is represented by a big long list of numbers
representing where the speaker should be through time. We can take this
list of numbers and use it to draw a graph which would look similar to
this:

![sample graph](../images/tutorial/sample.png)

You might have seen pictures like this before. It's called the
*waveform* of a sample. It's just a graph of numbers. Typically a
waveform like this will have 44100 points of data per second (this is
due to the Nyquist-Shannon sampling theorem). So, if the sample lasts
for 2 seconds, the waveform will be represented by 88200 numbers which
we would feed to the speaker at a rate of 44100 points per second. Of
course, we could feed it at double rate which would be 88200 points per
second. This would therefore take only 1 second to play back. We could
also play it back at half rate which would be 22050 points per second
taking 4 seconds to play back.

The duration of the sample is affected by the playback rate: 

* Doubling the playback rate halves the playback time,
* Halving the playback rate doubles the playback time,
* Using a playback rate of one fourth quadruples the playback time,
* Using a playback rate of 1/10 makes playback last 10 times longer.

We can represent this with the formula:

```
new_sample_duration = (1 / rate) * sample_duration 
```

Changing the playback rate also affects the pitch of the sample. The
frequency or pitch of a waveform is determined by how fast it moves up
and down. Our brains somehow turn fast movement of speakers into high
notes and slow movement of speakers into low notes. This is why you can
sometimes even see a big bass speaker move as it pumps out super low
bass - it's actually moving a lot slower in and out than a speaker
producing higher notes.

If you take a waveform and squash it it will move up and down more times
per second. This will make it sound higher pitched. It turns out that
doubling the amount of up and down movements (oscillations) doubles the
frequency. So, *playing your sample at double rate will double the
frequency you hear it*. Also, *halving the rate will halve the
frequency*. Other rates will affect the frequency accordingly.
3.4 Enveloped Samples

# Enveloped Samples

It is also possible to modify the *duration* and *amplitude* of a sample
using an ADSR envelope. However, this works slightly differently to the
ADSR envelope available on synths. Sample envelopes only allow you to
reduce the amplitude and duration of a sample - and never to increase
it. The sample will stop when either the sample has finished playing or
the envelope has completed - whichever is first. So, if you use a very
long `release:`, it won't extend the duration of the sample.

## Amen Envelopes

Let's return to our trusty friend the Amen Break:

```
sample :loop_amen
```

With no opts, we hear the full sample at full amplitude. If we
want to fade this in over 1 second we can use the `attack:` param:

```
sample :loop_amen, attack: 1
```

For a shorter fade in, choose a shorter attack value:

```
sample :loop_amen, attack: 0.3
```

## Auto Sustain

Where the ADSR envelope's behaviour differs from the standard synth
envelope is in the *sustain* value. In the standard synth envelope, the
sustain defaulted to 0 unless you set it manually. With samples, the
sustain value defaults to an *automagical* value - the time left to play
the rest of the sample. This is why we hear the full sample when we pass
no defaults. If the attack, decay, sustain and release values were all 0
we'd never hear a peep. Sonic Pi therefore calculates how long the
sample is, deducts any attack, decay and release times and uses the
result as your sustain time. If the attack, decay and release values add
up to more than the duration of the sample, the sustain is simply set to
0.

## Fade Outs

To explore this, let's consider our Amen break in more detail. If we ask
Sonic Pi how long the sample is:

```
print sample_duration :loop_amen
```

It will print out `1.753310657596372` which is the length of the sample
in seconds. Let's just round that to `1.75` for convenience here. Now,
if we set the release to `0.75`, something surprising will happen:

```
sample :loop_amen, release: 0.75
```

It will play the first second of the sample at full amplitude before
then fading out over a period of 0.75 seconds. This is the *auto
sustain* in action. By default, the release always works from the end of
the sample. If our sample was 10.75 seconds long, it would play the
first 10 seconds at full amplitude before fading out over 0.75s.

Remember: by default, `release:` fades out at the end of a sample.

## Fade In and Out

We can use both `attack:` and `release:` together with the auto sustain
behaviour to fade both in and out over the duration of the sample:

```
sample :loop_amen, attack: 0.75, release: 0.75
```

As the full duration of the sample is 1.75s and our attack and release
phases add up to 1.5s, the sustain is automatically set to 0.25s. This
allows us to easily fade the sample in and out.

## Explicit sustain

We can easily get back to our normal synth ADSR behaviour by manually
setting `sustain:` to a value such as 0:

```
sample :loop_amen, sustain: 0, release: 0.75
```

Now, our sample only plays for 0.75 seconds in total. With the default
for `attack:` and `decay:` at 0, the sample jumps straight to full
amplitude, sustains there for 0s then releases back down to 0 amplitude
over the release period - 0.75s.

## Percussive cymbals

We can use this behaviour to good effect to turn longer sounding samples
into shorter, more percussive versions. Consider the sample
`:drum_cymbal_open`:

```
sample :drum_cymbal_open
```

You can hear the cymbal sound ringing out over a period of
time. However, we can use our envelope to make it more percussive:

```
sample :drum_cymbal_open, attack: 0.01, sustain: 0, release: 0.1
```

You can then emulate hitting the cymbal and then dampening it by
increasing the sustain period:

```
sample :drum_cymbal_open, attack: 0.01, sustain: 0.3, release: 0.1
```

Now go and have fun putting envelopes over the samples. Try changing the
rate too for really interesting results.
3.5 Partial Samples

# Partial Samples

This section will conclude our exploration of Sonic Pi's sample
player. Let's do a quick recap. So far we've looked at how we can
trigger samples:

```
sample :loop_amen
```

We then looked at how we can change the rate of samples such as
playing them at half speed:

```
sample :loop_amen, rate: 0.5
```

Next, we looked at how we could fade a sample in (let's do it at half
speed):

```
sample :loop_amen, rate: 0.5, attack: 1
```

We also looked at how we could use the start of a sample percussively
by giving `sustain:` an explicit value and setting both the attack and
release to be short values:

```
sample :loop_amen, rate: 2, attack: 0.01, sustain: 0, release: 0.35
```

However, wouldn't it be nice if we didn't have to always start at the
beginning of the sample? Wouldn't it also be nice if we didn't have to
always finish at the end of the sample?

## Choosing a starting point

It is possible to choose an arbitrary starting point in the sample as a
value between 0 and 1 where 0 is the start of the sample, 1 is the end
and 0.5 is half way through the sample. Let's try playing only the last
half of the amen break:

```
sample :loop_amen, start: 0.5
```

How about the last quarter of the sample:

```
sample :loop_amen, start: 0.75
```

## Choosing a finish point

Similarly, it is possible to choose an arbitrary finish point in the
sample as a value between 0 and 1. Let's finish the amen break half way
through:

```
sample :loop_amen, finish: 0.5
```

## Specifying start and finish

Of course, we can combine these two to play arbitrary segments of the
audio file. How about only a small section in the middle:

```
sample :loop_amen, start: 0.4, finish: 0.6
```

What happens if we choose a start position after the finish position?


```
sample :loop_amen, start: 0.6, finish: 0.4
```

Cool! It plays it backwards!

## Combining with rate

We can combine this new ability to play arbitrary segments of audio with
our friend `rate:`. For example, we can play a very small section of the
middle of the amen break very slowly:

```
sample :loop_amen, start: 0.5, finish: 0.7, rate: 0.2
```

## Combining with envelopes

Finally, we can combine all of this with our ADSR envelopes to produce
interesting results:

```
sample :loop_amen, start: 0.5, finish: 0.8, rate: -0.2, attack: 0.3, release: 1
```

Now go and have a play mashing up samples with all of this fun stuff...
3.6 External Samples

# External Samples

Whilst the built-in samples can get you up and started quickly, you
might wish to experiment with other recorded sounds in your music. Sonic
Pi totally supports this. First though, let's have a quick discussion on
the portability of your piece.

## Portability

When you compose your piece purely with built-in synths and samples, the
code is all you need to faithfully reproduce your music. Think about
that for a moment - that's amazing! A simple piece of text you can email
around or stick in a [Gist](https://gist.github.com) represents
everything you need to reproduce your sounds. That makes it *really easy
to share* with your friends as they just need to get hold of the code.

However, if you start using your own pre-recorded samples, you lose this
portability. This is because to reproduce your music other people not
only need your code, they need your samples too. This limits the ability
for others to manipulate, mash-up and experiment with your work. Of
course this shouldn't stop you from using your own samples, it's just
something to consider.

<!-- ## Freesound Support -->

<!-- One way to get the ability to experiment with new sounds whilst keeping -->
<!-- code portability is to use the [Freesound](http:freesound.org) -->
<!-- support. http://freesound.org is a website which allows people to upload -->
<!-- and share their samples. Each sample uploaded gets a special number -->
<!-- (kind of like a phone number) which you can use to dial up that sample -->
<!-- from Sonic Pi. The only drawback is that you need to have internet -->
<!-- access for it to work. -->

<!-- If you currently have internet access, try it for yourself: -->

<!-- ``` -->
<!-- freesound 24787 -->
<!-- ``` -->

<!-- The first time you do this you'll hear a standard `:elec_beep` as a -->
<!-- placeholder for the sound. Y -->


## Local Samples

So how do you play any arbitrary WAV or AIFF file on your computer?
All you need to do is pass the path of that file to `sample`:

```
# Raspberry Pi, Mac, Linux
sample "/Users/sam/Desktop/my-sound.wav"
# Windows
sample "C:/Users/sam/Desktop/my-sound.wav"
```

Sonic Pi will automatically load and play the sample. You can also pass
all the standard params you're used to passing `sample`:

```
# Raspberry Pi, Mac, Linux
sample "/Users/sam/Desktop/my-sound.wav", rate: 0.5, amp: 0.3
# Windows
sample "C:/Users/sam/Desktop/my-sound.wav", rate: 0.5, amp: 0.3
```
4 Randomisation

# Randomisation

A great way to add some interest into your music is using some random
numbers. Sonic Pi has some great functionality for adding randomness to
your music, but before we start we need to learn a shocking truth: in
Sonic Pi *random is not truly random*. What on earth does this mean?
Well, let's see.

## Repeatability

A really useful random function is `rrand` which will give you a random
value between two numbers - a *min* and a *max*. (`rrand` is short for
ranged random). Let's try playing a random note:

```
play rrand(50, 95)
```

Ooh, it played a random note. It played note `83.7527`. A nice random
note between 50 and 95. Woah, wait, did I just predict the exact random
note you got too? Something fishy is going on here. Try running the code
again. What? It chose `83.7527` again? That can't be random!

The answer is that it is not truly random, it's pseudo-random. Sonic Pi
will give you random-like numbers in a repeatable manner. This is very
useful for ensuring that the music you create on your machine sounds
identical on everybody else's machine - even if you use some randomness
in your composition.

Of course, in a given piece of music, if it 'randomly' chose `83.7527`
every time, then it wouldn't be very interesting. However, it
doesn't. Try the following:

```
loop do
  play rrand(50, 95)
  sleep 0.5
end 
```

Yes! It finally sounds random. Within a given *run* subsequent calls
to random functions will return random values. However, the next run
will produce exactly the same sequence of random values and sound
exactly the same. It's as if all Sonic Pi code went back in time to
exactly the same point every time the Run button was pressed. It's the
Groundhog Day of music synthesis!

## Haunted Bells

A lovely illustration of randomisation in action is the haunted bells
example which loops the `:perc_bell` sample with a random rate and sleep
time between bell sounds:

```
loop do
  sample :perc_bell, rate: (rrand 0.125, 1.5)
  sleep rrand(0.2, 2)
end
```

## Random cutoff

Another fun example of randomisation is to modify the cutoff of a
synth randomly. A great synth to try this out on is the `:tb303`
emulator:

```
use_synth :tb303

loop do
  play 50, release: 0.1, cutoff: rrand(60, 120)
  sleep 0.125
end
```

## Random seeds

So, what if you don't like this particular sequence of random numbers
Sonic Pi provides? Well it's totally possible to choose a different
starting point via `use_random_seed`. The default seed happens to be
0, so choose a different seed for a different random experience!

Consider the following:

```
5.times do
  play rrand(50, 100)
  sleep 0.5
end
```

Every time you run this code, you'll hear the same sequence of 5
notes. To get a different sequence simply change the seed:

```
use_random_seed 40
5.times do
  play rrand(50, 100)
  sleep 0.5
end
```

This will produce a different sequence of 5 notes. By changing the seed
and listening to the results you can find something that you like - and
when you share it with others, they will hear exactly what you heard
too.

Let's have a look at some other useful random functions.


## choose

A very common thing to do is to choose an item randomly from a list of
known items. For example, I may want to play one note from the
following: 60, 65 or 72. I can achieve this with `choose` which lets
me choose an item from a list. First, I need to put my numbers in a list
which is done by wrapping them in square brackets and separating them
with commas: `[60, 65, 72]`. Next I just need to pass them to `choose`:

```
choose([60, 65, 72])
```

Let's hear what that sounds like:

```
loop do
  play choose([60, 65, 72])
  sleep 1
end
```

## rrand

We've already seen `rrand`, but let's run over it again. It returns a
random number between two values exclusively. That means it will never
return either the top or bottom number - always something in between the
two. The number will always be a float - meaning it's not a whole number
but a fraction of a number. Examples of floats returned by
`rrand(20, 110)`:

* 87.5054931640625
* 86.05255126953125
* 61.77825927734375

## rrand_i

Occasionally you'll want a whole random number, not a float. This is
where `rrand_i` comes to the rescue. It works similarly to `rrand`
except it may return the min and max values as potential random values
(which means it's inclusive rather than exclusive of the
range). Examples of numbers returned by `rrand_i(20, 110)` are:

* 88
* 86
* 62

## rand

This will return a random float between 0 (inclusive) and the max
value you specify (exclusive). By default it will return a value
between 0 and one. It's therefore useful for choosing random `amp:`
values:

```
loop do
  play 60, amp: rand
  sleep 0.25
end
```

## rand_i

Similar to the relationship between `rrand_i` and `rrand`, `rand_i` will
return a random whole number between 0 and the max value you specify.

## dice

Sometimes you want to emulate a dice throw - this is a special case of
`rrand_i` where the lower value is always 1. A call to `dice` requires
you to specify the number of sides on the dice. A standard dice has 6
sides, so `dice(6)` will act very similarly - returning values of either
1, 2, 3, 4, 5, or 6. However, just like fantasy role-play games, you
might find value in a 4 sided dice, or a 12 sided dice, or a 20 sided
dice - perhaps even a 120 sided dice!

## one_in

Finally you may wish to emulate throwing the top score of a dice such
as a 6 in a standard dice. `one_in` therefore returns true with a
probability of one in the number of sides on the dice. Therefore
`one_in(6)` will return true with a probability of 1 in 6 or false
otherwise. True and false values are very useful for `if` statements
which we will cover in a subsequent section of this tutorial.

Now, go and jumble up your code with some randomness!
5 Programming Structures

# Programming Structures

Now that you've learned the basics of creating sounds with `play` and
`sample` and creating simple melodies and rhythms by `sleep`ing between
sounds, you might be wondering what else the world of code can offer
you...

Well, you're in for an exciting treat! It turns out that basic
programming structures such as looping, conditionals, functions and
threads give you amazingly powerful tools to express your musical ideas.

Let's get stuck in with the basics...
5.1 Blocks

# Blocks

A structure you'll see a lot in Sonic Pi is the block. Blocks allow us
to do useful things with large chunks of code. For example, with synth
and sample parameters we were able to change something that happened on
a single line. However, sometimes we want to do something meaningful to
a number of lines of code. For example, we may wish to loop it, to add
reverb to it, to only run it 1 time out of 5, etc. Consider the
following code:

```
play 50
sleep 0.5
sample :elec_plip
sleep 0.5
play 62
```

To do something with a chunk of code, we need to tell Sonic Pi where
the code block *starts* and where it *ends*. We use `do` for start and
`end` for end. For example:

```
do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end
```

However, this isn't yet complete and won't work (try it and you'll get
an error) as we haven't told Sonic Pi what we want to do with this
*do/end block*. We tell Sonic Pi this by writing some special code
before the `do`. We'll see a number of these special pieces of code
later on in this tutorial. For now, it's important to know that wrapping
your code within `do` and `end` tells Sonic Pi you wish to do something
special with that chunk of code.
5.2 Iteration and Loops

# Iteration and Loops

So far we've spent a lot of time looking at the different sounds you
can make with `play` and `sample` blocks. We've also learned how to
trigger these sounds through time using `sleep`.

As you've probably found out, there's a *lot* of fun you can have with
these basic building blocks. However, a whole new dimension of fun opens
up when you start using the power of code to structure your music and
compositions. In the next few sections we'll explore some of these
powerful new tools. First up is iteration and loops.

## Repetition

Have you written some code you'd like to repeat a few times? For
example, you might have something like this:

```
play 50
sleep 0.5
sample :elec_blup
sleep 0.5
play 62
sleep 0.25
```

What if we wished to repeat this 3 times? Well, we could do something
simple and just copy and paste it three times:

```
play 50
sleep 0.5
sample :elec_blup
sleep 0.5
play 62
sleep 0.25

play 50
sleep 0.5
sample :elec_blup
sleep 0.5
play 62
sleep 0.25

play 50
sleep 0.5
sample :elec_blup
sleep 0.5
play 62
sleep 0.25
```

Now that's a lot of code! What happens if you want to change the
sample to `:elec_plip`? You're going to have to find all the places
with the original `:elec_blup` and switch them over. More importantly,
what if you wanted to repeat the original piece of code 50 times or
1000? Now that would be a lot of code, and a lot of lines of code to
alter if you wanted to make a change.

## Iteration

In fact, repeating the code should be as easy as saying *do this three
times*. Well, it pretty much is. Remember our old friend the code
block? We can use it to mark the start and end of the code we'd like
to repeat three times. We then use the special code `3.times`. So,
instead of writing *do this three times*, we write `3.times do` -
that's not too hard. Just remember to write `end` at the end of the
code you'd like to repeat:

```
3.times do
  play 50
  sleep 0.5
  sample :elec_blup
  sleep 0.5
  play 62
  sleep 0.25
end
```

Now isn't that much neater than cutting and pasting! We can use this to
create lots of nice repeating structures:

```
4.times do
  play 50
  sleep 0.5
end

8.times do
  play 55, release: 0.2
  sleep 0.25
end

4.times do
  play 50
  sleep 0.5
end
```

## Nesting Iterations

We can put iterations inside other iterations to create interesting
patterns. For example:

```
4.times do
  sample :drum_heavy_kick
  2.times do
    sample :elec_blip2, rate: 2
    sleep 0.25
  end
  sample :elec_snare
  4.times do
    sample :drum_tom_mid_soft
    sleep 0.125
  end
end
```

## Looping

If you want something to repeat a lot of times, you might find yourself
using really large numbers such as `1000.times do`. In this case, you're
probably better off asking Sonic Pi to repeat forever (at least until
you press the stop button!). Let's loop the amen break forever:

```
loop do
  sample :loop_amen
  sleep sample_duration :loop_amen
end
```

The important thing to know about loops is that they act like black
holes for code. Once the code enters a loop it can never leave until you
press stop - it will just go round and round the loop forever. This
means if you have code after the loop you will *never* hear it. For
example, the cymbal after this loop will never play:

```
loop do
  play 50
  sleep 1
end

sample :drum_cymbal_open
```

Now, get structuring your code with iteration and loops!
5.3 Conditionals

# Conditionals

A common thing you'll likely find yourself wanting to do is to not only
play a random note (see the previous section on randomness) but also
make a random decision and based on the outcome run some code or some
other code. For example, you might want to randomly play a drum or a
cymbal. We can achieve this with an `if` statement.

## Flipping a Coin 

So, let's flip a coin: if it's heads, play a drum, if it's tails, play a
cymbal. Easy. We can emulate a coin flip with our `one_in` function
(introduced in the section on randomness) specifying a probability of 1
in 2: `one_in(2)`. We can then use the result of this to decide between
two pieces of code, the code to play the drum and the code to play the
cymbal:

```
loop do

  if one_in(2)
    sample :drum_heavy_kick
  else
    sample :drum_cymbal_closed
  end
  
  sleep 0.5
  
end
```

Notice that `if` statements have three parts:

* The question to ask
* The first choice of code to run (if the answer to the question is yes)
* The second choice of code to run (if the answer to the question is no)

Typically in programming languages, the notion of yes is represented by
the term `true` and the notion of no is represented by the term
`false`. So we need to find a question that will give us a `true` or
`false` answer which is exactly what `one_in` does.

Notice how the first choice is wrapped between the `if` and the `else`
and the second choice is wrapped between the `else` and the `end`. Just
like do/end blocks you can put multiple lines of code in either
place. For example:

```
loop do

  if one_in(2)
    sample :drum_heavy_kick
    sleep 0.5
  else
    sample :drum_cymbal_closed
    sleep 0.25
  end
  
end
```

This time we're sleeping for a different amount of time depending on
which choice we make.


## Simple if

Sometimes you want to optionally execute just one line of code. This is
possible by placing `if` and then the question at the end. For example:

```
use_synth :dsaw

loop do
  play 50, amp: 0.3, release: 2
  play 53, amp: 0.3, release: 2 if one_in(2)
  play 57, amp: 0.3, release: 2 if one_in(3)
  play 60, amp: 0.3, release: 2 if one_in(4)
  sleep 1.5
end
```

This will play chords of different numbers with the chance of each note
playing having a different probability.
5.4 Threads

# Threads

So you've made your killer bassline and a phat beat. How do you play
them at the same time? One solution is to weave them together manually -
play some bass, then a bit of drums, then more bass... However, the
timing soon gets hard to think about, especially when you start weaving
in more elements.

What if Sonic Pi could weave things for you automatically? Well, it can,
and you do it with a special thing called a *thread*.

## Infinite Loops

To keep this example simple, you'll have to imagine that this is a
phat beat and a killer bassline:

```
loop do
  sample :drum_heavy_kick
  sleep 1
end

loop do
  use_synth :fm
  play 40, release: 0.2
  sleep 0.5
end
```

As we've discussed previously, loops are like *black holes* for the
program. Once you enter a loop you can never exit from it until you hit
stop. How do we play both loops at the same time? We have to tell Sonic
Pi that we want to start something at the same time as the rest of the
code. This is where threads come to the rescue.

## Threads to the Rescue

```
in_thread do
  loop do
    sample :drum_heavy_kick
    sleep 1
  end
end

loop do
  use_synth :fm
  play 40, release: 0.2
  sleep 0.5
end
```

By wrapping the first loop in an `in_thread` do/end block we tell Sonic
Pi to run the contents of the do/end block at *exactly* the same time as
the next statement after the do/end block (which happens to be the
second loop). Try it and you'll hear both the drums and the bassline
weaved together!

Now, what if we wanted to add a synth on top. Something like:

```
in_thread do
  loop do
    sample :drum_heavy_kick
    sleep 1
  end
end

loop do
  use_synth :fm
  play 40, release: 0.2
  sleep 0.5
end

loop do
  use_synth :zawa
  play 52, release: 2.5, phase: 2, amp: 0.5
  sleep 2
end
```

Now we have the same problem as before. The first loop is played at the
same time as the second loop due to the `in_thread`. However, *the third
loop is never reached*. We therefore need another thread:

```
in_thread do
  loop do
    sample :drum_heavy_kick
    sleep 1
  end
end

in_thread do
  loop do
    use_synth :fm
    play 40, release: 0.2
    sleep 0.5
  end
end

loop do
  use_synth :zawa
  play 52, release: 2.5, phase: 2, amp: 0.5
  sleep 2
end
```

## Runs as threads

What may surprise you is that when you press the Run button, you're
actually creating a new thread for the code to run. This is why pressing
it multiple times will layer sounds over each other. As the runs
themselves are threads, they will automatically weave the sounds
together for you.

## Scope

As you learn how to master Sonic Pi, you'll learn that threads are the
most important building blocks for your music. One of the important jobs
they have is to isolate the notion of *current settings* from other
threads. What does this mean? Well, when you switch synths using
`use_synth` you're actually just switching the synth in the *current
thread* - no other thread will have their synth switched. Let's see this
in action:

```
play 50
sleep 1

in_thread do
  use_synth :tb303
  play 50
end

sleep 1
play 50

```

Notice how the middle sound was different to the others? The `use_synth`
statement only affected the thread it was in and not the outer main run
thread.

## Inheritance 

When you create a new thread with `in_thread`, the new thread will
automatically inherit all of the current settings from the current
thread. Let's see that:

```
use_synth :tb303
play 50
sleep 1

in_thread do
  play 55
end
```

Notice how the second note is played with the `:tb303` synth even though
it was played from a separate thread? Any of the settings modified with
the various `use_*` functions will behave in the same way.

When threads are created, they inherit all the settings from their
parent but they don't share any changes back.

## Naming Threads

Finally, we can give our threads names:

```
in_thread(name: :bass) do
  loop do
    use_synth :prophet
    play chord(:e2, :m7).choose, release: 0.6
    sleep 0.5
  end
end

in_thread(name: :drums) do
  loop do
    sample :elec_snare
    sleep 1
  end
end
```

Look at the log pane when you run this code. See how the log reports the
name of the thread with the message?

```
[Run 36, Time 4.0, Thread :bass]
 |- synth :prophet, {release: 0.6, note: 47}
```

## Only One Thread per Name Allowed

One last thing to know about named threads is that only one thread of
a given name may be running at the same time. Let's explore this.
Consider the following code:

```
in_thread do
  loop do
    sample :loop_amen
    sleep sample_duration :loop_amen
  end
end
```

Go ahead and paste that into a buffer and press the Run button. Press
it again a couple of times. Listen to the cacophony of multiple amen
breaks looping out of time with each other. Ok, you can press Stop now.

This is the behaviour we've seen again and again - if you press the Run
button, sound layers on top of any existing sound. Therefore if you have
a loop and press the Run button three times, you'll have three layers of
loops playing simultaneously.

However, with named threads it is different:

```
in_thread(name: :amen) do
  loop do
    sample :loop_amen
    sleep sample_duration :loop_amen
  end
end
```

Try pressing the Run button multiple times with this code. You'll only
ever hear one amen break loop. You'll also see this in the log:

```
==> Skipping thread creation: thread with name :amen already exists.
```

Sonic Pi is telling you that a thread with the name `:amen` is already
playing, so it's not creating another.

This behaviour may not seem immediately useful to you now - but it will
be very handy when we start to live code...
5.5 Functions

# Functions

Once you start writing lots of code, you may wish to find a way to
organise and structure things to make them tidier and easier to
understand. Functions are a very powerful way to do this. They give us
the ability to give a name to a bunch of code. Let's take a look.

## Defining functions

```
define :foo do
  play 50
  sleep 1
  play 55
  sleep 2
end
```

Here, we've defined a new function called `foo`. We do this with our old
friend the do/end block and the magic word `define` followed by the name
we wish to give to our function. We didn't have to call it `foo`, we could
have called it anything we want such as `bar`, `baz` or ideally
something meaningful to you like `main_section` or `lead_riff`.

Remember to prepend a colon `:` to the name of your function when you define
it.

## Calling functions

Once we have defined our function we can call it by just writing its
name:

```
define :foo do
  play 50
  sleep 1
  play 55
  sleep 0.5
end

foo

sleep 1

2.times do
  foo
end
```

We can even use `foo` inside iteration blocks or anywhere we may have
written `play` or `sample`. This gives us a great way to express
ourselves and to create new meaningful words for use in our compositions.

## Functions are remembered across runs

So far, every time you've pressed the Run button, Sonic Pi has started
from a completely blank slate. It knows nothing except for what is in
the buffer. You can't reference code in another buffer or another
thread. However, functions change that. When you define a function,
Sonic Pi *remembers* it. Let's try it. Delete all the code in your
buffer and replace it with:

```
foo
```

Press the Run button - and hear your function play. Where did the code
go? How did Sonic Pi know what to play? Sonic Pi just remembered your
function - so even after you deleted it from the buffer, it
remembered what you had typed. This behaviour only works with functions
created using `define` (and `defonce`).

## Parameterised functions

You might be interested in knowing that just like you can pass min and
max values to `rrand`, you can teach your functions to accept
arguments. Let's take a look:

```
define :my_player do |n|
  play n
end

my_player 80
sleep 0.5
my_player 90
```

This isn't very exciting, but it illustrates the point. We've created
our own version of `play` called `my_player` which is parameterised.

The parameters need to go after the `do` of the `define` do/end block,
surrounded by vertical goalposts `|` and separated by commas `,`. You
may use any words you want for the parameter names.

The magic happens inside the `define` do/end block. You may use the
parameter names as if they were real values. In this example I'm playing
note `n`.  You can consider the parameters as a kind of promise that
when the code runs, they will be replaced with actual values. You do
this by passing a parameter to the function when you call it. I do this
with `my_player 80` to play note 80. Inside the function definition, `n`
is now replaced with 80, so `play n` turns into `play 80`. When I call
it again with `my_player 90`, `n` is now replaced with 90, so `play n`
turns into `play 90`.

Let's see a more interesting example:

``` 
define :chord_player do |root, repeats| 
  repeats.times do
    play chord(root, :minor), release: 0.3
    sleep 0.5
  end
end

chord_player :e3, 2
sleep 0.5
chord_player :a3, 3
chord_player :g3, 4
sleep 0.5
chord_player :e3, 3

```

Here I used `repeats` as if it was a number in the line `repeats.times
do`. I also used `root` as if it was a note name in my call to `play`.

See how we're able to write something very expressive and easy to read
by moving a lot of our logic into a function!
5.6 Variables

# Variables

A useful thing to do in your code is to create names for things. Sonic
Pi makes this very easy, you write the name you wish to use, an equal
sign (`=`), then the thing you want to remember:

```
sample_name = :loop_amen
```

Here, we've 'remembered' the symbol `:loop_amen` in the variable
`sample_name`. We can now use `sample_name` everywhere we might have
used `:loop_amen`. For example:

```
sample_name = :loop_amen
sample sample_name
```

There are three main reasons for using variables in Sonic Pi:
communicating meaning, managing repetition and capturing the results
of things.

## Communicating Meaning

When you write code it's easy to just think you're telling the computer
how to do stuff - as long as the computer understands it's OK. However,
it's important to remember that it's not just the computer that reads
the code. Other people may read it too and try to understand what's going
on. Also, you're likely to read your own code in the future and try to
understand what's going on. Although it might seem obvious to you now -
it might not be so obvious to others or even your future self! 

One way to help others understand what your code is doing is to write
comments (as we saw in a previous section). Another is to use meaningful
variable names. Look at this code:

```
sleep 1.7533
```

Why does it use the number `1.7533`? Where did this number come from?
What does it mean? However, look at this code:

```
loop_amen_duration = 1.7533
sleep loop_amen_duration
```

Now, it's much clearer what `1.7533` means: it's the duration of the
sample `:loop_amen`! Of course, you might say why not simply write:

```
sleep sample_duration(:loop_amen)
```

Which, of course, is a very nice way of communicating the intent of the
code.

## Managing Repetition

Often you see a lot of repetition in your code and when you want to
change things, you have to change it in a lot of places. Take a look at
this code:

```
sample :loop_amen
sleep sample_duration(:loop_amen)
sample :loop_amen, rate: 0.5
sleep sample_duration(:loop_amen, rate: 0.5)
sample :loop_amen
sleep sample_duration(:loop_amen)
```

We're doing a lot of things with `:loop_amen`! What if we wanted to
hear what it sounded like with another loop sample such as
`:loop_garzul`? We'd have to find and replace all `:loop_amen`s with
`:loop_garzul`. That might be fine if you have lots of time - but what
if you're performing on stage? Sometimes you don't have the luxury of
time - especially if you want to keep people dancing.

What if you'd written your code like this:

```
sample_name = :loop_amen
sample sample_name
sleep sample_duration(sample_name)
sample sample_name, rate: 0.5
sleep sample_duration(sample_name, rate: 0.5)
sample sample_name
sleep sample_duration(sample_name)
```

Now, that does exactly the same as above (try it). It also gives us
the ability to just change one line `sample_name = :loop_amen` to
`sample_name = :loop_garzul` and we change it in many places through
the magic of variables.

## Capturing Results

Finally, a good motivation for using variables is to capture the results
of things. For example, you may wish to do things with the duration of a
sample:

```
sd = sample_duration(:loop_amen)
```

We can now use `sd` anywhere we need the duration of the `:loop_amen`
sample.

Perhaps more importantly, a variable allows us to capture the result
of a call to `play` or `sample`:

```
s = play 50, release: 8
```

Now we have caught and remembered `s` as a variable, which allows us
to control the synth as it is running:

```
s = play 50, release: 8
sleep 2
control s, note: 62
```

We'll look into controlling synths in more detail in a later section.
5.7 Thread Synchronisation

# Thread Synchronisation

Once you have become sufficiently advanced live coding with a number of
functions and threads simultaneously, you've probably noticed that it's
pretty easy to make a mistake in one of the threads which kills
it. That's no big deal, because you can easily restart the thread by
hitting Run. However, when you restart the thread it is now *out of
time* with the original threads.

## Inherited Time

As we discussed earlier, new threads created with `in_thread` inherit
all of the settings from the parent thread. This includes the current
time. This means that threads are always in time with each other when
started simultaneously.

However, when you start a thread on its own it starts with its own
time which is unlikely to be in sync with any of the other currently
running threads.

## Cue and Sync

Sonic Pi provides a solution to this problem with the functions `cue`
and `sync`.

`cue` allows us to send out heartbeat messages to all other threads. By
default the other threads aren't interested and ignore these heartbeat
messages. However, you can easily register interest with the `sync`
function.

The important thing to be aware of is that `sync` is similar to
`sleep` in that it stops the current thread from doing anything for a
period of time. However, with `sleep` you specify how long you want to
wait while with `sync` you don't know how long you will wait - as
`sync` waits for the next `cue` from another thread which may be soon
or a long time away.

Let's explore this in a little more detail:

```
in_thread do
  loop do
    cue :tick
    sleep 1
  end
end

in_thread do
  loop do
    sync :tick
    sample :drum_heavy_kick
  end
end
```

Here we have two threads - one acting like a metronome, not playing any
sounds but sending out `:tick` heartbeat messages every beat. The
second thread is synchronising on `tick` messages and when it receives
one it inherits the time of the `cue` thread and continues running.

As a result, we will hear the `:drum_heavy_kick` sample exactly when
the other thread sends the `:tick` message, even if the two threads
didn't start their execution at the same time:

```
in_thread do
  loop do
    cue :tick
    sleep 1
  end
end

sleep(0.3)

in_thread do
  loop do
    sync :tick
    sample :drum_heavy_kick
  end
end
```

That naughty `sleep` call would typically make the second thread out
of phase with the first. However, as we're using `cue` and `sync`, we
automatically sync the threads bypassing any accidental timing
offsets.

## Cue Names  

You are free to use whatever name you'd like for your `cue` messages -
not just `:tick`. You just need to ensure that any other threads are
`sync`ing on the correct name - otherwise they'll be waiting for ever
(or at least until you press the Stop button).

Let's play with a few `cue` names:

```
in_thread do
  loop do 
    cue [:foo, :bar, :baz].choose
    sleep 0.5
  end
end

in_thread do
  loop do 
    sync :foo 
    sample :elec_beep
  end
end

in_thread do
  loop do
    sync :bar
    sample :elec_flip
  end
end

in_thread do
  loop do
    sync :baz
    sample :elec_blup
  end
end
```

Here we have a main `cue` loop which is randomly sending one of the
heartbeat names `:foo`, `:bar` or `:baz`. We then also have three loop
threads syncing on each of those names independently and then playing a
different sample. The net effect is that we hear a sound every 0.5
beats as each of the `sync` threads is randomly synced with the `cue`
thread and plays its sample.

This of course also works if you order the threads in reverse as the
`sync` threads will simply sit and wait for the next `cue`.
6 FX

# Studio FX

One of the most rewarding and fun aspects of Sonic Pi is the ability to
easily add studio effects to your sounds. For example, you may wish to
add some reverb to parts of your piece, or some echo or perhaps even
distort or wobble your basslines.

Sonic Pi provides a very simple yet powerful way of adding FX. It even
allows you to chain them (so you can pass your sounds through
distortion, then echo and then reverb) and also control each individual
FX unit with opts (in a similar way to giving params to synths and
samples). You can even modify the opts of the FX whilst it's still
running. So, for example, you could increase the reverb on your bass
throughout the track...

## Guitar Pedals

If all of this sounds a bit complicated, don't worry. Once you play
around with it a little, it will all become quite clear. Before you do
though, a simple analogy is that of guitar FX pedals. There are many
kinds of FX pedals you can buy. Some add reverb, others distort etc. A
guitarist will plug his or her guitar into one FX pedal -
i.e. distortion -, then take another cable and connect (chain) a
reverb pedal. The output of the reverb pedal can then be plugged into
the amplifier:

```
Guitar -> Distortion -> Reverb -> Amplifier
```

This is called FX chaining. Sonic Pi supports exactly
this. Additionally, each pedal often has dials and sliders to allow
you to control how much distortion, reverb, echo etc. to apply. Sonic
Pi also supports this kind of control. Finally, you can imagine a
guitarist playing whilst someone plays with the FX controls whilst
they're playing. Sonic Pi also supports this - but instead of needing
someone else to control things for you, that's where the computer
steps in.

Let's explore FX!
6.1 Adding FX

# Adding FX

In this section we'll look at a couple of FX: reverb and echo. We'll
see how to use them, how to control their opts and how to chain
them.

Sonic Pi's FX system uses blocks. So if you haven't read section 5.1 you
might want to take a quick look and then head back.

## Reverb

If we want to use reverb we write `with_fx :reverb` as the special code
to our block like this:

```
with_fx :reverb do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end
```

Now play this code and you'll hear it played with reverb. It sounds
good, doesn't it! Everything sounds pretty nice with reverb.

Now let's look what happens if we have code outside the do/end block:

```
with_fx :reverb do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end

sleep 1
play 55
```

Notice how the final `play 55` isn't played with reverb. This is because
it is *outside* the do/end block, so it isn't captured by the reverb FX.

Similarly, if you make sounds before the do/end block, they also won't
be captured:

```
play 55
sleep 1

with_fx :reverb do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end

sleep 1
play 55
```

## Echo

There are many FX to choose from. How about some echo?

```
with_fx :echo do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end
```

One of the powerful aspects of Sonic Pi's FX blocks is that they may be
passed parameters similar to parameters we've already seen with `play`
and `sample`. For example a fun echo parameter to play with is `phase:`
which represents the duration of a given echo in beats. Let's make the
echo slower:

```
with_fx :echo, phase: 0.5 do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end
```

Let's also make the echo faster:

```
with_fx :echo, phase: 0.125 do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end
```

Let's make the echo take longer to fade away by setting the `decay:`
time to 8 beats:

```
with_fx :echo, phase: 0.5, decay: 8 do
  play 50
  sleep 0.5
  sample :elec_plip
  sleep 0.5
  play 62
end
```

## Nesting FX

One of the most powerful aspects of the FX blocks is that you can nest
them. This allows you to very easily chain FX together. For example,
what if you wanted to play some code with echo and then with reverb?
Easy, just put one inside the other:

```
with_fx :reverb do
  with_fx :echo, phase: 0.5, decay: 8 do
    play 50
    sleep 0.5
    sample :elec_blup
    sleep 0.5
    play 62
  end
end
```

Think about the audio flowing from the inside out. The sound of all
the code within the inner do/end block such as `play 50` is first sent
to the echo FX and the sound of the echo FX is in turn sent out to the
reverb FX.

We may use very deep nestings for crazy results. However, be warned, the
FX can use a lot of resources and when you nest them you're effectively
running multiple FX simultaneously. So be sparing with your use of FX
especially on low powered platforms such as the Raspberry Pi.

## Discovering FX

Sonic Pi ships with a large number of FX for you to play with. To find
out which ones are available, click on FX in the far left of this help
system and you'll see a list of available options. Here's a list of
some of my favourites:

* wobble,
* reverb,
* echo,
* distortion,
* slicer

Now go crazy and add FX everywhere for some amazing new sounds!
6.2 FX in Practice

# FX in Practice

Although they look deceptively simple on the outside, FX are actually
quite complex beasts internally. Their simplicity often entices people
to overuse them in their pieces. This may be fine if you have a
powerful machine, but if - like me - you use a Raspberry Pi to jam
with, you need to be careful about how much work you ask it to do if
you want to ensure the beats keep flowing.

Consider this code:

```
loop do
  with_fx :reverb do
    play 60, release: 0.1
    sleep 0.125
  end
end
```

In this code we're playing note 60 with a very short release time, so
it's a short note. We also want reverb so we've wrapped it in a reverb
block. All good so far. Except...

Let's look at what the code does. First we have a `loop` which means
everything inside of it is repeated forever. Next we have a `with_fx`
block. This means we will create a new reverb FX *every time we
loop*. This is like having a separate FX reverb pedal for every time you
pluck a string on a guitar. It's cool that you can do this, but it's not
always what you want. For example, this code will struggle to run nicely
on a Raspberry Pi. All the work of creating the reverb and then waiting
until it needs to be stopped and removed is all handled by `with_fx` for
you, but this takes CPU power which may be precious.

How do we make it more similar to a traditional setup where our
guitarist has just *one* reverb pedal which all sounds pass through?
Simple:

```
with_fx :reverb do
  loop do
    play 60, release: 0.1
    sleep 0.125
  end
end
```

We put our loop *inside* the `with_fx` block. This way we only create
a single reverb for all notes played in our loop. This code is a lot
more efficient and would work fine on a Raspberry Pi.

A compromise is to use `with_fx` over an iteration within a loop:

```
loop do
  with_fx :reverb do
    16.times do
      play 60, release: 0.1
      sleep 0.125
    end
  end
end
```

This way we've lifted the `with_fx` out of the inner part of the `loop`
and we're now creating a new reverb every 16 notes.

Remember, there are no mistakes, just possibilities. However, each of
these approaches will have a different sound and also different
performance characteristics. So play around and use the approach that
sounds best to you whilst also working within the performance
constraints of your platform.
7 Control

# Controlling running sounds

So far we've looked at how you can trigger synths and samples, and
also how to change their default opts such as amplitude, pan,
envelope settings and more. Each sound triggered is essentially its
own sound with its own list of options set for the duration of the
sound.

Wouldn't it also be cool if you could change a sound's opts whilst it's
still playing, just like you might bend a string of a guitar whilst it's
still vibrating?

You're in luck - this section will show you how to do exactly this.
7.1 Controlling Running Synths

# Controlling Running Synths

So far we've only concerned ourselves with triggering new sounds and
FX. However, Sonic Pi gives us the ability to manipulate and control
currently running sounds. We do this by using a variable to capture a
reference to a synth:

```
s = play 60, release: 5
```

Here, we have a run-local variable `s` which represents the synth
playing note 60. Note that this is *run-local* - you can't access it
from other runs like functions.

Once we have `s`, we can start controlling it via the `control`
function:

```
s = play 60, release: 5
sleep 0.5
control s, note: 65
sleep 0.5
control s, note: 67
sleep 3
control s, note: 72
```

The thing to notice is that we're not triggering 4 different synths here
- we're just triggering one synth and then change the pitch 3 times
afterwards, while it's playing.

We can pass any of the standard opts to `control`, so you can
control things like `amp:`, `cutoff:` or `pan:`.

## Non-controllable Options

Some of the opts can't be controlled once the synth has started. This is
the case for all the ADSR envelope parameters. You can find out which
opts are controllable by looking at their documentation in the
help system. If the documentation says *Can not be changed once set*,
you know it's not possible to control the opt after the synth has
started.
7.2 Controlling FX

# Controlling FX

It is also possible to control FX, although this is achieved in a
slightly different way:

```
with_fx :reverb do |r|
  play 50
  sleep 0.5
  control r, mix: 0.7
  play 55
  sleep 1
  control r, mix: 0.9
  sleep 1
  play 62
end
```

Instead of using a variable, we use the goalpost parameters of the
do/end block. Inside the `|` bars, we need to specify a unique name
for our running FX which we then reference from the containing do/end
block. This behaviour is identical to using parameterised functions.

Now go and control some synths and FX!
7.3 Sliding Options

# Sliding Opts

Whilst exploring the synth and FX opts, you might have noticed that
there are a number of opts ending with `_slide`. You might have
even tried calling them and seeing no effect. This is because they're
not normal parameters, they're special opts that only work when
you control synths as introduced in the previous section.

Consider the following example:

```
s = play 60, release: 5
sleep 0.5
control s, note: 65
sleep 0.5
control s, note: 67
sleep 3
control s, note: 72
```

Here, you can hear the synth pitch changing immediately on each
`control` call. However, we might want the pitch to slide between
changes. As we're controlling the `note:` parameter, to add slide, we
need to set the `note_slide` parameter of the synth:

```
s = play 60, release: 5, note_slide: 1
sleep 0.5
control s, note: 65
sleep 0.5
control s, note: 67
sleep 3
control s, note: 72
```

Now we hear the notes being bent between the `control` calls. It
sounds nice, doesn't it? You can speed up the slide by using a shorter
time such as `note_slide: 0.2` or slow it down by using a longer slide
time.

Every parameter that can be controlled has a corresponding `_slide`
parameter for you to play with.

## Sliding is sticky

Once you've set a `_slide` parameter on a running synth, it will be
remembered and used every time you slide the corresponding
parameter. To stop sliding you must set the `_slide` value to 0 before
the next `control` call.

## Sliding FX Opts

It is also possible to slide FX opts:

```
with_fx :wobble, phase: 1, phase_slide: 5 do |e|
  use_synth :dsaw
  play 50, release: 5
  control e, phase: 0.025
end
```

Now have fun sliding things around for smooth transitions and flowing
control...
8 Data Structures

# Data Structures

A very useful tool in a programmer's toolkit is a data structure.

Sometimes you may wish to represent and use more than one thing. For
example, you may find it useful to have a series of notes to play one
after another. Programming languages have data structures to allow you
do exactly this.

There are many exciting and exotic data structures available to
programmers - and people are always inventing new ones. However, for now
we only really need to consider a very simple data structure - the list.

Let's look at it in more detail. We'll cover its basic form and then
also how lists can be used to represent scales and chords.
8.1 Lists

# Lists

In this section we'll take a look at a data structure which is very
useful - the list. We met it very briefly before in the section on
randomisation when we randomly chose from a list of notes to play:

```
play choose([50, 55, 62])
```

In this section we'll explore using lists to also represent chords
and scales. First let's recap how we might play a chord. Remember that
if we don't use `sleep`, sounds all happen at the same time:

```
play 52
play 55
play 59
```

Let's look at other ways to represent this code.

## Playing a List

One option is to place all the notes in a list: `[52, 55, 59]`. Our
friendly `play` function is smart enough to know how to play a list of
notes. Try it:

```
play [52, 55, 59]
```

Ooh, that's already nicer to read. Playing a list of notes doesn't stop
you from using any of the parameters as normal:

```
play [52, 55, 59], amp: 0.3
```

Of course, you can also use the traditional note names instead of the
MIDI numbers:

```
play [:E3, :G3, :B3]
```

Now those of you lucky enough to have studied some music theory might
recognise that chord as *E Minor* played in the 3rd octave.

## Accessing a List

Another very useful feature of a list is the ability to get information
out of it. This may sound a bit strange, but it's no more complicated
than someone asking you to turn a book to page 23. With a list, you'd
say, what's the element at index 23? The only strange thing is that in
programming indexes usually start at 0 not 1. 

With list indexes we don't count 1, 2, 3... Instead we count 0, 1, 2...

Let's look at this in a little more detail. Take a look at this list:

```
[52, 55, 59]
```

There's nothing especially scary about this. Now, what's the second
element in that list? Yes, of course, it's `55`. That was easy. Let's
see if we can get the computer to answer it for us too:

```
puts [52, 55, 59][1]
```

OK, that looks a bit weird if you've never seen anything like it
before. Trust me though, it's not too hard. There are three parts to the
line above: the word `puts` , our list `52, 55, 59` and our index
`[1]`. Firstly we're saying `puts` because we want Sonic Pi to print the
answer out for us in the log. Next, we're giving it our list, and
finally our index is asking for the second element. We need to surround
our index with square brackets and because counting starts at `0`, the
index for the second element is `1`. Look:

```
# indexes:  0   1   2
           [52, 55, 59]
```

Try running the code `puts [52, 55, 59][1]` and you'll see `55` pop up
in the log. Change the index `1` to other indexes, try longer lists and
think about how you might use a list in your next code jam. For example,
what musical structures might be represented as a series of numbers...





8.2 Chords

# Chords

Sonic Pi has built-in support for chord names which will return
lists. Try it for yourself:

```
play chord(:E3, :minor)
```

Now, we're really getting somewhere. That looks a lot more pretty than
the raw lists (and is easier to read for other people). So what other
chords does Sonic Pi support? Well, a *lot*. Try some of these:

* `chord(:E3, :m7)`
* `chord(:E3, :minor)`
* `chord(:E3, :dim7)`
* `chord(:E3, :dom7)`

## Arpeggios

We can easily turn chords into arpeggios with the function
`play_pattern`:

```
play_pattern chord(:E3, :m7)
```

Ok, that's not so fun - it played it really slowly. `play_pattern` will
play each note in the list separated with a call to `sleep 1` between
each call to `play`. We can use another function `play_pattern_timed` to
specify our own timings and speed things up:

```
play_pattern_timed chord(:E3, :m7), 0.25
```

We can even pass a list of times which it will treat as a circle of
times:

```
play_pattern_timed chord(:E3, :m13), [0.25, 0.5]
```

This is the equivalent to:

```
play 52
sleep 0.25
play 55
sleep 0.5
play 59
sleep 0.25
play 62
sleep 0.5
play 66
sleep 0.25
play 69
sleep 0.5
play 73
```

Which would you prefer to write?
8.3 Scales

# Scales

Sonic Pi has support for a wide range of scales. How about
playing a C3 major scale?

```
play_pattern_timed scale(:c3, :major), 0.125, release: 0.1
```

We can even ask for more octaves:

```
play_pattern_timed scale(:c3, :major, num_octaves: 3), 0.125, release: 0.1
```

How about all the notes in a pentatonic scale?

```
play_pattern_timed scale(:c3, :major_pentatonic, num_octaves: 3), 0.125, release: 0.1
```

## Random notes

Chords and scales are great ways of constraining a random choice to
something meaningful. Have a play with this example which picks random
notes from the chord E3 minor:

```
use_synth :tb303
loop do
  play choose(chord(:E3, :minor)), release: 0.3, cutoff: rrand(60, 120)
  sleep 0.25
end
```

Try switching in different chord names and cutoff ranges.

## Discovering Chords and Scales

To find out which scales and chords are supported by Sonic Pi simply
click the Lang button on the far left of this tutorial and then choose
either chord or scale in the API list. In the information in the main
panel, scroll down until you see a long list of chords or scales
(depending on which you're looking at).

Have fun and remember: there are no mistakes, only opportunities.
8.4 Rings

# Rings

An interesting spin on standard lists are rings. If you know some
programming, you might have come across ring buffers or ring
arrays. Here, we'll just go for ring - it's short and simple.

In the previous section on lists we saw how we could fetch elements out
of them by using the indexing mechanism:

```
puts [52, 55, 59][1]
```

Now, what happens if you want index `100`? Well, there's clearly no
element at index 100 as the list has only three elements in it. So Sonic
Pi will return you `nil` which means nothing.

However, consider you have a counter such as the current beat which
continually increases. Let's create our counter and our list:

```
counter = 0
notes = [52, 55, 59]
```

We can now use our counter to access a note in our list:

```
puts notes[counter]
```

Great, we got `52`. Now, let's increment our counter and get another
note:

```
counter = (inc counter)
puts notes[counter]
```

Super, we now get `55` and if we do it again we get `59`. However, if we
do it again, we'll run out of numbers in our list and get `nil`. What if
we wanted to just loop back round and start at the beginning of the list
again? This is what rings are for.

## Creating Rings

We can create rings one of two ways. Either we use the `ring` function
with the elements of the ring as parameters:

```
(ring 52, 55, 59)
```

Or we can take a normal list and convert it to a ring by sending it the
`.ring` message:

```
[52, 55, 59].ring
```

## Indexing Rings

Once we have a ring, you can use it in exactly the same way you would
use a normal list with the exception that you can use indexes that are
negative or larger than the size of the ring and they'll wrap round to
always point at one of the ring's elements:

```
(ring 52, 55, 59)[0] #=> 52
(ring 52, 55, 59)[1] #=> 55
(ring 52, 55, 59)[2] #=> 59
(ring 52, 55, 59)[3] #=> 52
(ring 52, 55, 59)[-1] #=> 59
```

## Using Rings

Let's say we're using a variable to represent the current beat
number. We can use this as an index into our ring to fetch notes to
play, or release times or anything useful we've stored in our ring
regardless of the beat number we're currently on.

## Scales and Chords are Rings

A useful thing to know is that the lists returned by `scale` and `chord`
are also rings and allow you to access them with arbitrary indexes.

## Ring Constructors

In addition to `ring` there are a number of other functions which will
construct a ring for us.

* `range` invites you specify a starting point, end point and step size.
* `bools` allows you to use `1`s and `0`s to succinctly represent booleans.
* `knit` allows you to knit a sequence of repeated values.
* `spread` creates a ring of bools with a Euclidean distribution.

Take a look at their respective documentation for more information.

9 Live Coding

# Live Coding

One of the most exciting aspects of Sonic Pi is that it enables you to
write and modify code live to make music, just like you might perform
live with a guitar. One advantage of this approach is to give you more
feedback whilst composing (get a simple loop running and keep tweaking
it till it sounds just perfect). However, the main advantage is that you
can take Sonic Pi on stage and gig with it.

In this section we'll cover the fundamentals of turning your static code
compositions into dynamic performances.

Hold on to your seats...
9.1 Live Coding Fundamentals

# Live Coding

Now we've learned enough to really start having some fun. In this
section we'll draw from all the previous sections and show you how you
can start making your music compositions live and turning them into a
performance. For that we'll need 3 main ingredients:

* An ability to write code that makes sounds - CHECK!
* An ability to write functions - CHECK!
* An ability to use (named) threads - CHECK!

Alrighty, let's get started. Let's live code our first sounds. We first
need a function containing the code we want to play. Let's start
simple. We also want to loop calls to that function in a thread:

```
define :my_loop do
  play 50
  sleep 1
end

in_thread(name: :looper) do
  loop do
    my_loop
  end
end
```

If that looks a little too complicated to you, go back and re-read the
sections on functions and threads. It's not too complicated if you've
already wrapped your head around these things.

What we have here is a function definition which just plays note 50 and
sleeps for a beat. We then define a named thread called `:looper`
which just loops around calling `my_loop` repeatedly.

If you run this code, you'll hear note 50 repeating again and again...

## Changing it up

Now, this is where the fun starts. Whilst the code is *still running*
change 50 to another number, say 55, then press the Run button
again. Woah! It changed! Live!

It didn't add a new layer because we're using named threads which only
allow one thread for each name. Also, the sound changed because we
*redefined* the function. We gave `:my_loop` a new definition. When the
`:looper` thread looped around it simply called the new definition.

Try changing it again, change the note, change the sleep time. How about
adding a `use_synth` statement? For example, change it to:

```
define :my_loop do
  use_synth :tb303
  play 50, release: 0.3
  sleep 0.25
end
```

Now it sounds pretty interesting, but we can spice it up
further. Instead of playing the same note again and again, try playing
a chord:

```
define :my_loop do
  use_synth :tb303
  play chord(:e3, :minor), release: 0.3
  sleep 0.5
end
```

How about playing random notes from the chord:

```
define :my_loop do
  use_synth :tb303
  play choose(chord(:e3, :minor)), release: 0.3
  sleep 0.25
end
```

Or using a random cutoff value:

```
define :my_loop do
  use_synth :tb303
  play choose(chord(:e3, :minor)), release: 0.2, cutoff: rrand(60, 130)
  sleep 0.25
end
```

Finally, add some drums:

```
define :my_loop do
  use_synth :tb303
  sample :drum_bass_hard, rate: rrand(0.5, 2)
  play choose(chord(:e3, :minor)), release: 0.2, cutoff: rrand(60, 130)
  sleep 0.25
end
```

Now things are getting exciting! 

However, before you jump up and start live coding with functions and
threads, stop what you're doing and read the next section on
`live_loop` which will change the way you code in Sonic Pi forever...
9.2 Live Loops

# Live Loops

Ok, so this section of the tutorial is the real gem. If you only read
one section, it should be this one. If you read the previous section
on Live Coding Fundamentals, `live_loop` is a simple way of doing
exactly that but without having to write so much.

If you didn't read the previous section, `live_loop` is the best way to
jam with Sonic Pi.

Let's play. Write the following in a new buffer:

```
live_loop :foo do
  play 60
  sleep 1
end
```

Now press the Run button. You hear a basic beep every beat. Nothing
fun there. However, don't press Stop just yet. Change the `60` to `65`
and press Run again.

Woah! It changed *automatically* without missing a beat. This is live coding.

Why not change it to be more bass like? Just update your code whilst it's playing:

```
live_loop :foo do
  use_synth :prophet
  play :e1, release: 8
  sleep 8
end
```

Then hit Run.

Let's make the cutoff move around:

```
live_loop :foo do
  use_synth :prophet
  play :e1, release: 8, cutoff: rrand(70, 130)
  sleep 8
end
```

Hit Run again.

Add some drums:

```
live_loop :foo do
  sample :loop_garzul
  use_synth :prophet
  play :e1, release: 8, cutoff: rrand(70, 130)
  sleep 8
end
```

Change the note from `e1` to `c1`:

```
live_loop :foo do
  sample :loop_garzul
  use_synth :prophet
  play :c1, release: 8, cutoff: rrand(70, 130)
  sleep 8
end
```

Now stop listening to me and play around yourself! Have fun!
9.3 Multiple Live Loops

# Multiple Live Loops

Consider the following live loop:

```
live_loop :foo do
  play 50
  sleep 1
end
```

You may have wondered why it needs the name `:foo`. This name is
important because it signifies that this live loop is different from all
other live loops. 

*There can never be two live loops running with the same name*.

This means that if we want multiple concurrently running live loops, we
just need to give them different names:

```
live_loop :foo do
  use_synth :prophet
  play :c1, release: 8, cutoff: rrand(70, 130)
  sleep 8
end

live_loop :bar do
  sample :bd_haus
  sleep 0.5
end
```

You can now update and change each live loop independently and it all
just works.

## Syncing Live Loops

One thing you might have already noticed is that live loops work
automatically with the thread cue mechanism we explored
previously. Every time the live loop loops, it generates a new `cue`
event with the name of the live loop. We can therefore `sync` on these
cues to ensure our loops are in sync without having to stop anything.

Consider this badly synced code:

```
live_loop :foo do
  play :e4, release: 0.5
  sleep 0.4
end

live_loop :bar do
  sample :bd_haus
  sleep 1
end
```

Let's see if we can fix the timing and sync without stopping it. First,
let's fix the `:foo` loop to make the sleep a factor of 1 - something like
`0.5` will do:

```
live_loop :foo do
  play :e4, release: 0.5
  sleep 0.5
end

live_loop :bar do
  sample :bd_haus
  sleep 1
end
```

We're not quite finished yet though - you'll notice that the beats don't
quite line up correctly. This is because the loops are *out of
phase*. Let's fix that by syncing one to the other:

```
live_loop :foo do
  play :e4, release: 0.5
  sleep 0.5
end

live_loop :bar do
  sync :foo
  sample :bd_haus
  sleep 1
end
```

Wow, everything is now perfectly in time - all without stopping.

Now, go forth and live code with live loops!
9.4 Ticking

# Ticking

Something you'll likely find yourself doing a lot when live coding is
looping through rings. You'll be putting notes into rings for melodies,
sleeps for rhythms, chord progressions, timbral variations, etc. etc.

## Ticking Rings

Sonic Pi provides a *very* handy tool for working with rings within
`live_loop`s. It's called the tick system. It provides you with the ability to *tick through rings*. Let's look at an example:

```
live_loop :arp do
  play (scale :e3, :minor_pentatonic).tick, release: 0.1
  sleep 0.125
end
```

Here, we're just grabbing the scale E3 minor pentatonic and ticking through each element. This is done by adding `.tick` to the end of the scale declaration. This tick is local to the live loop, so each live loop can have its own independent tick:

```
live_loop :arp do
  play (scale :e3, :minor_pentatonic).tick, release: 0.1
  sleep 0.125
end

live_loop :arp2 do
  use_synth :dsaw
  play (scale :e2, :minor_pentatonic, num_octaves: 3).tick, release: 0.25
  sleep 0.25
end
```

## Tick

You can also call `tick` as a standard fn and use the value as an index:

```
live_loop :arp do
  idx = tick
  play (scale :e3, :minor_pentatonic)[idx], release: 0.1
  sleep 0.125
end
```

However, it is much nicer to call `.tick` at the end. The `tick` fn is
for when you want to do fancy things with the tick value and for when
you want to use ticks for other things than indexing into rings.


## Look

The magical thing about tick is that not only does it return a new index
(or the value of the ring at that index) it also makes sure that next
time you call tick, it's the next value. Take a look at the examples in
the docs for `tick` for many ways of working with this. However, for
now, it's important to point out that sometimes you'll want to just look
at the current tick value and *not increase* it. This is available via
the `look` fn. You can call `look` as a standard fn or by adding `.look`
to the end of a ring.

## Naming Ticks

Finally, sometimes you'll need more than one tick per live loop. This is achieved by giving your tick a name:

```
live_loop :arp do
  play (scale :e3, :minor_pentatonic).tick(:foo), release: 0.1
  sleep (ring 0.125, 0.25).tick(:bar)
end
```

Here we're using two ticks one for the note to play and another for the
sleep time. As they're both in the same live loop, to keep them separate
we need to give them unique names. This is exactly the same kind of
thing as naming `live_loop`s - we just pass a symbol prefixed with a
`:`. In the example above we called one tick `:foo` and the other
`:bar`. If we want to `look` at these we also need to pass the name of
the tick to `look`.

## Don't make it too complicated

Most of the power in the tick system isn't useful when you get
started. Don't try and learn everything in this section. Just focus on
ticking through a single ring. That'll give you most of the joy and
simplicity of ticking through rings in your `live_loop`s.

Take a look at the documentation for `tick` where there are many useful
examples and happy ticking!

10 Essential Knowledge

# Essential Knowledge

This section will cover some very useful - in fact *essential* - knowledge
for getting the most out of your Sonic Pi experience.

We'll cover how to take advantage of the many keyboard shortcuts
available to you, how to share your work and some tips on performing
with Sonic Pi.
10.1 Using Shortcuts

# Using Shortcuts

Sonic Pi is as much an instrument as a coding environment. Shortcuts can
therefore make playing Sonic Pi much more *efficient and natural* -
especially when you're playing live in front of an audience.

Much of Sonic Pi can be controlled through the keyboard. As you gain
more familiarity working and performing with Sonic Pi, you'll likely
start using the shortcuts more and more. *I personally touch-type* (I
recommend you consider learning too) and find myself frustrated whenever
I need to reach for the mouse as it slows me down. I therefore use all
of these shortcuts on a very regular basis! 

Therefore, if you learn the shortcuts, you'll learn to use your keyboard
effectively and you'll be live coding like a pro in no time.

However, *don't try and learn them all at once*, just try and remember the
ones you use most and then keep adding more to your practice.

## Consistency across Platforms

Imagine you're learning the clarinet. You'd expect all clarinets of
all makes to have similar controls and fingerings. If they didn't, you'd
have a tough time switching between different clarinets and you'd be
stuck to using just one make.

Unfortunately the three major operating systems (Linux, Mac OS X and
Windows) come with their own standard defaults for actions such as cut
and paste etc. Sonic Pi will try and honour these standards. However
*priority is placed on consistency across platforms* within Sonic Pi
rather than attempting to conform to a given platform's standards. This
means that when you learn the shortcuts whilst playing with Sonic Pi on
your Raspberry Pi, you can move to the Mac or PC and feel right at home.

## Control and Meta

Part of the notion of consistency is the naming of shortcuts. In Sonic
Pi we use the names *Control* and *Meta* to refer to the two main
combination keys. On all platforms *Control* is the same. However, on
Linux and Windows, *Meta* is actually the *Alt* key while on Mac *Meta* is
the *Command* key. For consistency we'll use the term *Meta* - just
remember to map that to the appropriate key on your operating system.

## Abbreviations

To help keep things simple and readable, we'll use the abbreviations *C-*
for *Control* plus another key and *M-* for *Meta* plus another key. For
example, if a shortcut requires you to hold down both *Meta* and *r*
we'll write that as `M-r`. The *-* just means "at the same time as."

The following are some of the shortcuts I find most useful.

## Stopping and starting

Instead of always reaching for the mouse to run your code, you can
simply press `M-r`. Similarly, to stop running code you can press `M-s`.

## Navigation

I'm really lost without the navigation shortcuts. I therefore highly
recommend you spend the time to learn them. These shortcuts also work
extremely well when you've learned to touch type as they use the
standard letters rather than requiring you to move your hand to the
mouse or the arrow keys on your keyboard.

You can move to the beginning of the line with `C-a`, the end of the
line with `C-e`, up a line with `C-p`, down a line with `C-n`, forward a
character with `C-f`, and back a character with `C-b`. You can even
delete all the characters from the cursor to the end of the line with
`C-k`.

## Tidy Code

To auto-align your code simply press `M-m`.

## Help System

To toggle the help system you can press `M-i`. However, a much more
useful shortcut to know is `C-i` which will look up the word underneath
the cursor and display the docs if it finds anything. Instant help!

For a full list take a look at section 10.2 Shortcut Cheatsheet.
10.2 Shortcut Cheatsheet

# Shortcut Cheatsheet

The following is a summary of the main shortcuts available within Sonic
Pi. Please see Section 10.1 for motivation and background.

## Conventions

In this list, we use the following conventions (where *Meta* is one of *Alt* on
Windows/Linux or *Cmd* on Mac):

* `C-a` means hold the *Control* key then press the *a* key whilst holding them both at the same time, then releasing.
* `M-r` means hold the *Meta* key and then press the *r* key whilst holding them both at the same time, then releasing.
* `S-M-z` means hold the *Shift* key, then the *Meta* key, then finally the *z* key all at the same time, then releasing.
* `C-M-f` means hold the *Control* key, then press *Meta* key, finally the *f* key all at the same time, then releasing.


## Main Application Manipulation

* `M-r` - Run code
* `M-s` - Stop code
* `M-i` - Toggle Help System
* `M-p` - Toggle Preferences
* `M-<` - Switch buffer to the left
* `M->` - Switch buffer to the right
* `M-+` - Increase text size of current buffer
* `M--` - Decrease text size of current buffer


## Selection/Copy/Paste

* `M-a`     - Select all
* `M-c`     - Copy selection to paste buffer
* `M-]`     - Copy selection to paste buffer
* `M-x`     - Cut selection to paste buffer
* `C-]`     - Cut selection to paste buffer
* `C-k`     - Cut to the end of the line
* `M-v`     - Paste from paste buffer to editor
* `C-y`     - Paste from paste buffer to editor
* `C-SPACE` - Set mark. Navigation will now manipulate highlighted region. Use `C-g` to escape.


## Text Manipulation

* `M-m` - Align all text
* `Tab` - Align current line/selection (or complete list)
* `C-l` - Centre editor
* `M-/` - Comment/Uncomment current line
* `C-t` - Transpose/swap characters
* `M-u` - Convert next word (or selection) to upper case.  
* `M-l` - Convert next word (or selection) to lower case.  


## Navigation

* `C-a`   - Move to beginning of line
* `C-e`   - Move to end of line
* `C-p`   - Move to previous line
* `C-n`   - Move to next line
* `C-f`   - Move forward one character
* `C-b`   - Move backward one character
* `M-f`   - Move forward one word
* `M-b`   - Move backward one word
* `C-M-n` - Move line or selection down
* `C-M-p` - Move line or selection up
* `S-M-u` - Move up 10 lines
* `S-M-d` - Move down 10 lines


## Deletion

* `C-h` - Delete previous character
* `C-d` - Delete next character


## Advanced Editor Features

* `C-i`   - Show docs for word under cursor
* `M-z`   - Undo
* `S-M-z` - Redo
* `C-g`   - Escape
* `S-M-f` - Toggle fullscreen mode
* `S-M-b` - Toggle visibility of buttons
* `S-M-l` - Toggle visibility of log
* `S-M-m` - Toggle between light/dark modes


10.3 Sharing

# Sharing

Sonic Pi is all about sharing and learning with each other. 

Once you've learned how to code music, sharing your compositions is as
simple as sending an email containing your code. Please do *share* your
code with others so they can *learn* from your work and even use parts
in a new *mash-up*. 

If you're unsure of the best way to share your work with others I
recommend putting your code on [GitHub](https://github.com) and your
music on [SoundCloud](https://soundcloud.com). That way you'll be able
to easily reach a large audience.

## Code -> GitHub

[GitHub](https://github.com) is a site for sharing and working with
code. It's used by professional developers as well as artists for
sharing and collaborating with code. The simplest way to share a new piece
of code (or even an unfinished piece) is to create a
[Gist](https://gist.github.com). A [Gist](https://gist.github.com) is a
simple way of uploading your code in a simple way that others can see,
copy and share.

## Audio -> SoundCloud

Another important way of sharing your work is to record the audio and
upload it to [SoundCloud](https://soundcloud.com). Once you've uploaded
your piece, other users can comment and discuss your work. I also
recommend placing a link to a [Gist](https://gist.github.com) of your
code in the track description.

To record your work, hit the `Rec` button in the toolbar, and
recording starts immediately.  Hit `Run` to start your code if
it isn't already in progress.  When you're done recording, press the
flashing `Rec` button again, and you'll be prompted to enter a
filename.  The recording will be saved as a WAV file, which can be
edited and converted to MP3 by any number of free programs (try
Audacity for instance).

## Hope

I encourage you to share your work and really hope that we'll all teach
each other new tricks and moves with Sonic Pi. I'm really excited by
what you'll have to show me.
10.4 Performing

# Performing

One of the most exciting aspects of Sonic Pi is that it enables you to
use code as a *musical instrument*. This means that writing code live can
now be seen as a new way of performing music.

We call this *Live Coding*.

## Show Your Screen

When you live code I recommend you *show your screen* to your
audience. Otherwise it's like playing a guitar but hiding your fingers
and the strings. When I practice at home I use a Raspberry Pi and a
little mini projector on my living room wall. You could use your TV or
one of your school/work projectors to give a show. Try it, it's a lot of
fun.

## Form a Band

Don't just play on your own - form a live coding band! It's a lot of fun
jamming with others. One person could do beats, another ambient
background, etc. See what interesting combinations of sounds you can
have together.

## TOPLAP

Live coding isn't completely new - a small number of people have been
doing it for a few years now, typically using bespoke systems they've
built for themselves. A great place to go and find out more about other
live coders and systems is [TOPLAP](http://toplap.org).

## Algorave

Another great resource for exploring the live coding world is
[Algorave](http://algorave.com). Here you can find all about a specific
strand of live coding for making music in nightclubs.
11 Minecraft Pi

# Minecraft Pi

Sonic Pi now supports a simple API for interacting with Minecraft Pi -
the special edition of Minecraft which is installed by default on the
Raspberry Pi's Raspbian Linux-based operating system.

## No need to import libraries

The Minecraft Pi integration has been designed to be insanely easy to
use. All you need to do is to launch a Minecraft Pi and create a
world. You're then free to use the `mc_*` fns just like you might use
`play` and `synth`. There's no need to import anything or install any
libraries - it's all ready to go and works out of the box.

## Automatic Connection

The Minecraft Pi API takes care of managing your connection to the
Minecraft Pi application. This means you don't need to worry about a
thing. If you try and use the Minecraft Pi API when Minecraft Pi isn't
open, Sonic Pi will politely tell you. Similarly, if you close Minecraft
Pi whilst you're still running a `live_loop` that uses the API, the live
loop will stop and politely tell you that it can't connect. To
reconnect, just launch Minecraft Pi again and Sonic Pi will
automatically detect and re-create the connection for you.

## Designed to be Live Coded

The Minecraft Pi API has been designed to work seamlessly within
`live_loop`s. This means it's possible to synchronise modifications in
your Minecraft Pi worlds with modifications in your Sonic Pi
sounds. Instant Minecraft-based music videos! Note however that
Minecraft Pi is alpha software and is known to be slightly buggy. If you
encounter any problems simply restart Minecraft Pi and carry on as
before. Sonic Pi's automatic connection functionality will take care of
things for you.

## Requires a Raspberry Pi 2.0

It is highly recommended that you use a Raspberry Pi 2 if you wish to
run both Sonic Pi and Minecraft at the same time - especially if you
want to use Sonic Pi's sound capabilities.

## API Support

At this stage, Sonic Pi supports basic block and player manipulations
which are detailed in Section 11.1. Support for event callbacks
triggered by player interactions in the world is planned for a future
release.
11.1 Basic API

# Basic Minecraft Pi API

Sonic Pi currently supports the following basic interactions with Minecraft Pi:

* Displaying chat messages
* Setting the position of the user
* Getting the position of the user
* Setting the block type at a given coordinate
* Getting the block type at a given coordinate


Let's look at each of these in turn.

## Displaying chat messages

Let's see just how easy it is to control Minecraft Pi from Sonic
Pi. First, make sure you have both Minecraft Pi and Sonic Pi open at the
same time and also make sure you've entered a Minecraft world and can
walk around.

In a fresh Sonic Pi buffer simply enter the following code:

```
mc_message "Hello from Sonic Pi"
```

When you hit the *Run* button, you'll see your message flash up on the
Minecraft window. Congratulations, you've written your first Minecraft
code! That was easy wasn't it.

## Setting the position of the user

Now, let's try a little magic. Let's teleport ourselves somewhere! Try
the following:

```
mc_teleport 50, 50, 50
```

When you hit *Run* - boom! You're instantantly transported to a new
place. Most likely it was somewhere in the sky and you fell down either
to dry land or into water. Now, what are those numbers: `50, 50, 50`?
They're the coordinates of the location you're trying to teleport
to. Let's take a brief moment to explore what coordinates are and how
they work because they're really, really important for programming
Minecraft.

## Coordinates

Imagine a pirate's map with a big `X` marking the location of some
treasure. The exact location of the `X` can be described with two
numbers - how far along the map from left to right and how far along the
map from bottom to top. For example `10cm` across and `8cm` up. These
two numbers `10` and `8` are coordinates. You could easily imagine
describing the locations of other stashes of treasure with other pairs
of numbers. Perhaps there's a big chest of gold at `2` across and `9`
up...

Now, in Minecraft two numbers isn't quite enough. We also need to know
how high we are. We therefore need three numbers:

* How far from right to left in the world - `x`
* How far from front to back in the world - `z`
* How high up we are in the world - `y`
One more thing - we typically describe these coordinates in this order
`x`, `y`, `z`.

## Finding your current coordinates

Let's have a play with coordinates. Navigate to a nice place in the
Minecraft map and then switch over to Sonic Pi. Now enter the following:

```
puts mc_location
```

When you hit the *Run* button you'll see the coordinates of your current
position displayed in the log window. Take a note of them, then move
forward in the world and try again. Notice how the coordinates changed!
Now, I recommend you spend some time repeating exactly this - move a bit
in the world, take a look at the coordinates and repeat. Do this until
you start to get a feel for how the coordinates change when you
move. Once you've understood how coordinates work, programming with the
Minecraft API will be a complete breeze.

## Let's Build!

Now that you know how to find the current position and to teleport using
coordinates, you have all the tools you need to start building things in
Minecraft with code. Let's say you want to make the block with
coordinates `40`, `50`, `60` to be glass. That's super easy:

```
mc_set_block :glass, 40, 50, 60
```

Haha, it really was that easy. To see your handywork just teleport
nearby and take a look:

```
mc_teleport 35, 50, 60
```

Now turn around and you should see your glass block! Try changing it to
diamond:

```
mc_set_block :diamond, 40, 50, 60
```

If you were looking in the right direction you might have even seen it
change in front of your eyes! This is the start of something exciting...

## Looking at blocks

Let's look at one last thing before we move onto something a bit more
involved. Given a set of coordinates we can ask Minecraft what the type
of a specific block is. Let's try it with the diamond block you just
created:

```
puts mc_get_block 40, 50, 60
```

Yey! It's `:diamond`. Try changing it back to glass and asking again -
does it now say `:glass`? I'm sure it does :-)

## Available block types

Before you go on a Minecraft Pi coding rampage, you might find this list
of available block types useful:

        :air
        :stone
        :grass
        :dirt
        :cobblestone
        :wood_plank
        :sapling
        :bedrock
        :water_flowing
        :water
        :water_stationary
        :lava_flowing
        :lava
        :lava_stationary
        :sand
        :gravel
        :gold_ore
        :iron_ore
        :coal_ore
        :wood
        :leaves
        :glass
        :lapis
        :lapis_lazuli_block
        :sandstone
        :bed
        :cobweb
        :grass_tall
        :flower_yellow
        :flower_cyan
        :mushroom_brown
        :mushroom_red
        :gold_block
        :gold
        :iron_block
        :iron
        :stone_slab_double
        :stone_slab
        :brick
        :brick_block
        :tnt
        :bookshelf
        :moss_stone
        :obsidian
        :torch
        :fire
        :stairs_wood
        :chest
        :diamond_ore
        :diamond_block
        :diamond
        :crafting_table
        :farmland
        :furnace_inactive
        :furnace_active
        :door_wood
        :ladder
        :stairs_cobblestone
        :door_iron
        :redstone_ore
        :snow
        :ice
        :snow_block
        :cactus
        :clay
        :sugar_cane
        :fence
        :glowstone_block
        :bedrock_invisible
        :stone_brick
        :glass_pane
        :melon
        :fence_gate
        :glowing_obsidian
        :nether_reactor_core
12 Conclusions

# Conclusions

This concludes the Sonic Pi introductory tutorial. Hopefully you've
learned something along the way. Don't worry if you feel you didn't
understand everything - just play and have fun and you'll pick things up
in your own time. Feel free to dive back in when you have a question that
might be covered in one of the sections.

If you have any questions that haven't been covered in the tutorial,
then please jump onto the [Sonic Pi forums](http://groups.google.com/group/sonic-pi/)
and ask your question there. You'll find someone friendly and willing to
lend a hand.

Finally, I also invite you to take a deeper look at the rest of the
documentation in this help system. There are a number of features that
haven't been covered in this tutorial that are waiting for your
discovery.

So play, have fun, share your code, perform for your friends, show your
screens and remember:

*There are no mistakes, only opportunities.*

[Sam Aaron](http://twitter.com/samaaron)