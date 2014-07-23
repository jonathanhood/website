Fixing arrow keys in vim
========================

:category: Notes

Vim is an amazing text editor that many people swear by. On occasion though, it does do some frustrating stuff. For example, ever have vim do weird things whenever you press an error key? Happens to me pretty often, and I always have to scour the internet for a solution. It typically happens to me in two cases:


1. Using vim on a laptop
2. Using vim inside of putty


Never fear, there is a fix! Edit your .vimrc file ::

    > pico ~/.vimrc

Insert the following lines ::

    set t_ku=^[OA
    set t_kd=^[OB
    set t_kr=^[OC
    set t_kl=^[OD

Now, try out your arrow keys in vim. They should work. If not, there are more solutions at the vim wikia. Maybe you'll find something that will work for you there.

