# flashpolicytwistd

Flash policy server written in Python/Twisted

Simple, yet production-ready flash policy server. 
Distinguished from other similar projects by using async IO (no threads), 
which is the only sane solution for such a task. 
I use it in production environment with ~20k socket connections to server. 
And it copes quite well thanks to async IO of Twisted.

#### Features:
- Asyncronous IO (no threads) for production scalability
- Optional Monit resource file for continuous sanity checking
- init.d script
- Configurable flashpolicy.xml
- Only 20 lines of Python code!

#### Installation:
1. Install Twisted (Ubuntu: sudo apt-get install python-twisted)
2. Install flashpolicytwistd itself. Ubuntu users can download deb package and sudo dpkg -i flashpolicytwistd.deb.
3. Optionally, modify /etc/flashpolicy.xml
4. sudo /etc/init.d/flashpolicytwistd start
5. Optionally, install Monit. The package above provides /etc/monit/conf.d/flashpolicytwistd. Update Monit configuration to make use of it.

Comments are welcome.
