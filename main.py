import random


wordle_words = '''
focus
force
forth
forty
forum
found
frame
frank
fraud
fresh
front
fruit
fully
funny
giant
given
glass
globe
going
grace
grade
grand
grant
grass
great
green
gross
group
grown
guard
guess
guest
guide
happy
harry
heart
heavy
hence
henry
horse
hotel
house
human
ideal
image
index
inner
input
issue
japan
jimmy
joint
jones
judge
known
label
large
laser
later
laugh
layer
learn
lease
least
leave
legal
level
lewis
light
limit
links
lives
local
logic
loose
lower
lucky
lunch
lying
magic
major
maker
march
maria
match
maybe
mayor
meant
media
metal
might
minor
minus
mixed
model
money
month
moral
motor
mount
mouse
mouth
movie
music
needs
never
newly
night
noise
north
noted
novel
nurse
occur
ocean
offer
often
order
other
ought
paint
panel
paper
party
peace
peter
phase
phone
photo
piece
pilot
pitch
place
plain
plane
plant
plate
point
pound
power
press
price
pride
prime
print
prior
prize
proof
proud
prove
queen
quick
quiet
quite
radio
raise
range
rapid
ratio
reach
ready
refer
right
rival
river
robin
roger
roman
rough
round
route
royal
rural
scale
scene
scope
score
sense
serve
seven
shall
shape
share
sharp
sheet
shelf
shell
shift
shirt
shock
shoot
short
shown
sight
since
sixth
sixty
sized
skill
sleep
slide
small
smart
smile
smith
smoke
solid
solve
sorry
sound
south
space
spare
speak
speed
spend
spent
split
spoke
sport
staff
stage
stake
stand
start
state
steam
steel
stick
still
stock
stone
stood
store
storm
story
strip
stuck
study
stuff
style
sugar
suite
super
sweet
table
taken
taste
taxes
teach
teeth
terry
texas
thank
theft
their
theme
there
these
thick
thing
think
third
those
three
threw
throw
tight
times
tired
title
today
topic
total
touch
tough
tower
track
trade
train
treat
trend
trial
tried
tries
truck
truly
trust
truth
twice
under
undue
union
unity
until
upper
upset
urban
usage
usual
valid
value
video
virus
visit
vital
voice
waste
watch
water
wheel
where
which
while
white
whole
whose
woman
women
world
worry
worse
'''.split() 

x = random.choice(wordle_words)

guess = "" 
number_guesses = 6
while guess != x:
    print("Put in a 5 letter word to see if it matches the correct answer")
    guess = input()
    while len(guess) != len(x):
        print ("Your guess is invalid, try again")
        guess = input()
 
    if guess == x:
        print ("Game over")

    v = 0    
    error = ''
    for y in guess:
        if x[v] == y:
             error = error + "_"
        elif x[v]in y :
             error = error + "0"
        elif x[v] != y:
             error = error + "X"
        v = v + 1
    number_guesses = number_guesses - 1
    
    print (error)

    if number_guesses == 0:
        print ("You have lost the game, The word was")
        print (x)
        break
    



            
    


    
    


 



