Map Generator
#############

After playing Minecraft_ for awhile I got interested in procedural terrain generation. I wondered how a world could just be 'generated' while playing a game. So, like all good problems, I wrote a small program to solve it. In my research I can across the `Diamond-Square algorithm`_ and made an implementation of it. The output looks like this:

.. image:: {filename}/images/mapgen.jpg
   :alt: Map Generator Image
   :align: center
   :width: 500px

Here, if this image where to be interpreted as a height map, the blacker areas represent higher elevation and the white areas represent lower elevations. Using this data, a map can be generated.

If you want to try it out for yourself, download_ my implementation. It requires the pypng_ library to visualize its output. It has been tested on python 2.6.

.. _Minecraft: http://www.minecraft.net/
.. _Diamond-Square algorithm: http://en.wikipedia.org/wiki/Diamond-square_algorithm
.. _download: ??
.. _pypng: http://code.google.com/p/pypng/

