import time, calendar, datetime
src = open('index.html', encoding='utf-8').read()
open('__test/candidate.html','w',encoding='utf-8').write(src)
j = src.index('<meta charset="utf-8">') + len('<meta charset="utf-8">')
tz = """<script>
/* TEST-ONLY: 기기 타임존이 UTC로 잡힌 구형 태블릿 흉내 */
(function(){var P=Date.prototype;P.getHours=P.getUTCHours;P.getMinutes=P.getUTCMinutes;P.getSeconds=P.getUTCSeconds;P.getFullYear=P.getUTCFullYear;P.getMonth=P.getUTCMonth;P.getDate=P.getUTCDate;P.getDay=P.getUTCDay;P.getMilliseconds=P.getUTCMilliseconds;P.getTimezoneOffset=function(){return 0;};})();
</script>
"""
open('__test/tz-utc.html','w',encoding='utf-8').write(src[:j]+'\n'+tz+src[j:])
target = calendar.timegm(datetime.datetime(2026,11,23,7,20,0).timetuple()) - 9*3600
day = """<script>
/* TEST-ONLY: 평일 아침(2026-11-23 07:20 KST) 흉내 */
(function(){var T0=Date.now();var TARGET=%d;var RN=Date.now;Date.now=function(){return TARGET+(RN()-T0);};})();
</script>
""" % (target*1000,)
open('__test/fakeday.html','w',encoding='utf-8').write(src[:j]+'\n'+day+src[j:])
print('regenerated')
