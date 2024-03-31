# Трасировка сети
## Описание
выводит промежуточный ip-аддреса, а также страну, автономную систему и влаельца этого ip-аддреса

## Пример работы  
![](https://github.com/syoumzic/TraceRoute/blob/master/tr.gif)

## Пример вывода
```
PS C:\Users\Noname\CodeProject\Python\InetProtocol> python tr.py
введите ip-аддрес или имя хоста: vk.com
ip-аддрес, страна, автономная система, владелец:
10.76.32.1, *, *, *
10.1.83.85, *, *, *
10.8.176.133, *, *, *
10.8.176.86, *, *, *
10.8.176.85, *, *, *
10.8.176.2, *, *, *
10.76.63.254, *, *, *
5.141.114.0, Russia, AS12389 PJSC Rostelecom, Rostelecom networks
79.133.87.167, Russia, AS12389 PJSC Rostelecom, PJSC Rostelecom
188.254.2.4, Russia, AS12389 PJSC Rostelecom, PJSC Rostelecom
87.240.132.67, Russia, AS47541 VKontakte Ltd, VKONTAKTE SPb Net
```
