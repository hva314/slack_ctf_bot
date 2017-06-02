# CTF Bot for Slack

A bot for slack prints out ctf schedule from `ctftime.org`

### Requirement:
```
python2.7
slackclient
urllib2
bs4, lxml
texttable
```

### Command: 
`showschedule`

### Example

+----------------------+------------------------------+--------------------+----------------------------------+
|         CTF          |             Time             |        Type        |               Link               |
+======================+==============================+====================+==================================+
| 0CTF 2017 Finals     |  02 June, 08:00 UTC  03 June |           Jeopardy | https://ctf.0ops.net/            |
|                      |              2017, 15:00 UTC |    Shenzhen, China |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
| LabyREnth 2017       |  09 June, 16:00 UTC  23 July |           Jeopardy | http://labyrenth.com/            |
|                      |              2017, 16:00 UTC |            On-line |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
| Google Capture The   |  17 June, 00:00 UTC  18 June |           Jeopardy | https://g.co/ctf                 |
| Flag 2017            |              2017, 23:59 UTC |            On-line |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
| Trend Micro CTF 2017 |  24 June, 04:00 UTC  25 June |           Jeopardy | http://www.trendmicro.com/tmctf  |
| - Raimund Genes Cup  |              2017, 04:00 UTC |            On-line |                                  |
| - Online Qualifier   |                              |                    |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
| CTFZone 2017         |  24 June, 09:00 UTC  25 June |           Jeopardy | https://ctf.bi.zone/             |
|                      |              2017, 21:00 UTC |            On-line |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
| Nuit du Hack CTF     |  24 June, 19:30 UTC  25 June |     Attack-Defense | https://www.nuitduhack.com/      |
| Finals 2017          |              2017, 04:00 UTC |      Paris, France |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
| AltayCTF-2017        |  26 June, 10:00 UTC  26 June |           Jeopardy | https://university.altayctf.ru/  |
|                      |              2017, 18:00 UTC |            On-line |                                  |
+----------------------+------------------------------+--------------------+----------------------------------+
