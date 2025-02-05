Notes:


- gnu-coreutils

- grammar
    - pronoun(pro noun) 
        - who, which, what
    - noun
    - adverb(ad verb)
        - up
    - verb
    - auxiliary verb
        - do
    - modal verb
        - will, would, can
    - adjective
    - preposition
        - to, as
    - conjunction
    - determiner
        - either, what
    - predeterminer

- grammar examples
    - as(proposition)
        - used as the subject...
    - will(modal verb)
    - what(determiner, pronoun)
        - (determiner) what thing or things
        - (pronoun) what is in production
        - (pronoun) is what the branch looked like on the last commit to it
    - up(adverb)
        - end up staying at...
    - out
    - for(proposition)
        - n+n
            - intended to be given to 
                - *buy something for baby*
            - having the purpose of 
                - *for sale*
                - *for hire* 
                - *for use*
        - clause+n/v-ing 
            - because of or as a result of something
                - *all the better for seeing you*
                - *The things you do for love*
                - *Scotland is famous for its spectacular countryside*
                - *He's best remembered for his novels*
            - used to show an amount of distance/time
                - *We walked for miles*
                - *for years*
            - on the occasion of or at the time of
                - *for Christmas*
                - *for nine o'clock*
                - *for Jim's 60th birthday*
            - used for comparing one thing with others of the same type
                - *She's very mature for her age*
                - *For every two people in favour of the law there are three against* 
                - *The winter has been unusually cold for Florida*
                - *It's a difficult decision, especially for a child*
                - *For a man of his wealth he isn't exactly generous*
            - used to say whose responsibility something is 
                - *She knew the driver of the other car wasn't responsible for her son's death*
            - in support of or in agreenment with
                - *I voted for the Greens at the last election* 
                - *Who's for tennis?*
            - in order to help someone
                - *What can I do for you?*
            - in relation to something or someone
                - *Her feelings for him had changed*
                - *How are you doing for money/time?*
            - in exchange
                - *How much did you pay for your glasses?*
                - *I've sponsored her $1 for every mile that she runs*
            - being employed by or representing a company, country, etc 
                - *She works for a charity*
            - towards; in direction of
                - *They looked as if they were heading for the train station* 
                - *Just follow signs for the museum*
                - *It says this train is for Birminghan and Coventry only*
            - show meaning
                - *What's the Spanish word for "vegetarian"?*
                - *What does the "M.J." stand for? Maria Jose?*
            - in order to get or achieve
                - *I had to run for the bus*
            - the duty or responsibility of 
                - *That's for you to decide*
                - *It's not for me to tell her what she should do with her life*
    - the(determiner)
        - used before nouns
            - *important* to refer to particular things or person that have been already talked about or are already known or are in a situation where it is clear what is happening
                - *Please would you pass the salt*
                - *I'll pick you at the airport*
                - *I have bought a new shirt and some new shoes. The shirt was pretty expensive, but the shoes weren't* 
            - the range of meaning of the noun is limited in some way
                - *I really enjoy the book that I've finished reading* 
            - to refer to things or person when only one exist at any one time
                - *in the future*
                - *the world*
                - *in the north of Spain* 
        - used before adjectives
            - to turn adjectives into nouns to refer to one particular thing or person described by the adjective
                - *It's seem the decesed had no living relatives*
                - *I suppose we'll just have to wait for the inevatable*
            - to turn adjectives into nouns to refer to people or things in general that can be described by the adjective
                - *She lives in a special home for the elderly*
                - *The French was defeated at Waterloo in 1815*

- sentence example
    - of, it is ... for ... to ...
        - *There are often cases where it is desirable for a function to take a variable number of arguments*

- grammar layer
    - action, condition and experience
    - physical
    - mental

- word
    - conversion, transform
        - conversion
            - the process of conversing something from one thing to another
        - transform
            - a complete change in the appearance or character of something or someone, especially so that that thing or person is improved 

- dao
    - wei miao xuan tong 
    - shang shan ruo shui
    - chong ru ruo jin
    - gui da huan ruo sheng

- code
    - self review
    - config in file/field/property vs config in behaviour(function)
        - config in file/field/property:
            - identity, address
        - config in behaviour(function):
            - branch behaviour
    - interface vs virtual function 
        - interface:
            - the abstract behaviour which is relative to objects not belong to a same concept 
        - virtual function
            - the abstract behaviour which is relative to objects belong to a same concept 
    - abstract
        - layer
        - available
    - character encode
        - all files are restored with binary format in computer
        - what dose decode do is explain and extract thoese binary and convert them to another format correctly

- python
    - module
        - what is python module?
            - .py file
        - how to import modules?
            - *import module-a*
            - *from module-a import symbol-b as alias-c*
        - module search path
            - *sys.buildin_module_names*
                - build-in module 
            - *sys.path*
                - the directory containing input script 
                - PYTHONPATH
                    - prefix/lib/pythonversion, exec_prefix/lib/pythonversion
                        - prefix and exec_prefix are installation-dependent directory, both defaulting to /usr/local
                - the installation-dependent default(by convention including a *site-packages* directory)
    - package
        - what is python package
            - a directory containing a script named *__init__.py*
        - how to import a python package
            - *import packge-a.subdir-b.subdir-c*
    - string
        - f-string
            - a formatted string literal that is prefixed with a 'f' or 'F'
            - *f"This is a {variable}"*
        - r-string
            - make escape letter(\) invalid
                - *r"\\"* is identical with *"\\\\"*
    - list
        - initialization
            - *l = [1,2,3]*
        - frequently used function
            - *extend(iterator)*
            - *append(item)*
    - lambda
        - initialization
            - *lambda o:o.get_result()*
    
- approach
    - target and method
    - 5 why

- set theory
    - union
    - intersection
    - difference
    - complement

- rendering 
    - Stencil Op
    - ZTest

- graphic math
    - matrix(4x4, xyzw):
        - translation matrix
            - v
                - x,y,z,1
            - M
                - 1 0 0 dx
                - 0 1 0 dy
                - 0 0 1 dz
                - 0 0 0 1
            - M*v => (x+dx, y+dy, z+dz, 1)
            - math equation
                - vector add
            - point
                - change position
            - vector
                - change length and direction
    - rotation matrix(anticlockwise)
        - x
            - coscos - sinsin
        - y 
            - sincos + cossin
        - Mz
            - cos -sin 0 0
            - sin cos 0 0
            - 0 0 1 0
            - 0 0 0 1
        - My
            - ...
        - Mx
            - ...
    - scaling matrix
        - M
            - sx 0 0 0
            - 0 sy 0 0
            - 0 0 sz 0
            - 0 0 0 1
        - M*v => (x*sx, y*sy, z*sz, 1)
        - point
            - change position
        - vector
            - change length and direction

    - basis change matrix
        - translation * rotation...

- vector operations
    - v add(addition): 
        - graphic meaning
            - diagonal line
            - change length and direction
        - equation
            - (x1+x2, y1+y2)
    - v sub(subtraction)
        - graphic meaning
            - end-to-end line(from subtrahend to minuend)
            - change length and direction
        - equation
            - (x1-x2, y1-y2)
    - v scalar mul(multiplication)
        - graphic meaning
            - only change length
        - equation
            - (x*s, y*s)
    - v dot product
        - graphic meaning
            - projection
            - only scalar
        - equation
            - x1*x2+y1*y2
    - v cross product
        - graphic meaning
            - perpendicular vector
            - length equal area of the parallelogram
            - change length and direction
        - equation
            - (y1*z2-z1*y2, z1*x2-x1*z2, x1*y2-y1*x2)
