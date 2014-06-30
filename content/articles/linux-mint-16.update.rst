Обновил linux mint
##################

:tags: linux, minx, life, xfce
:category: bash
:date: 2014-04-30 10:16

Делается это все очень просто:


* sudo apt-get update
* sudo apt-get upgrade
* Заменя в файлах /etc/apt/sources.list и vim /etc/apt/sources.list.d вхождений названия старого дистрибутива на новый
* sudo apt-get dist-upgrade
* И снова apt-get udpate && apt-get upgrade
* ...
* Выгода.


Единственное что - у меня пакетный менеджер почему-то решил что "некоторые" пакеты *mate* мне больше не нужны, и пометил их как неиспользуемые. В результате я их решил не использоватЬ, и удалил через apt-get autoremove;

 В результате после загрузки у меня не запустился mdm;

Помогло:

* переключится на консольную сессию.
* Написать там startx
* Войти в настройки mdm и увидеть что нет logon тем из mint-15;
* Указать стандартный logon theme для mdm;
* И также перезапустив `service mdm restart` увидеть что mdm logon screen работает.
* В итоге: выставил что теперь мой window manager это xfce;

XFCE оказался не так уж плох, поэтому под ним и сижу. Такие дела.
:wq
