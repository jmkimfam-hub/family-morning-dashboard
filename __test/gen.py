import json, time, calendar, datetime
src = open('index.html', encoding='utf-8').read()
open('__test/candidate.html','w',encoding='utf-8').write(src)
j = src.index('<meta charset="utf-8">') + len('<meta charset="utf-8">')
old = {
 "seoyun": ["이불 정리","세수·양치·머리 묶어 단정히","아침밥 먹기","교복·가방·교재·태블릿 챙기기","휴대폰·교통카드·이어폰 확인","물병·우산 챙기고 출발!"],
 "chaeyun": ["내 물건 챙기기","양치하기","밥 먹기","가방 챙기기","물 마시기","방 정리"],
 "seungyun": ["눈 뜨고 기지개·이불 펴기","세수하고 치카치카 양치","아침밥 냠냠 먹기","알림장·가방·필통 챙기기","물통·손수건·우산 확인","씩씩하게 인사하고 출발!"]
}
seed = {"seoyun":{"time":"07:50","tasks":old["seoyun"]},"chaeyun":{"time":"08:00","tasks":old["chaeyun"]},"seungyun":{"time":"08:20","tasks":old["seungyun"]}}
checks = {"date":"2026-11-22","data":{"seoyun":[True,True,False,False,False,False],"chaeyun":[False]*6,"seungyun":[False]*6}}
block = """<script>
(function(){try{localStorage.removeItem('wdash.settings.v2');localStorage.removeItem('wdash.checks.v2');
localStorage.setItem('wdash.settings.v1', %s);localStorage.setItem('wdash.checks.v1', %s);
localStorage.setItem('wdash.active.v1','seoyun');}catch(e){}})();
</script>
""" % (json.dumps(json.dumps(seed, ensure_ascii=False), ensure_ascii=False), json.dumps(json.dumps(checks, ensure_ascii=False), ensure_ascii=False))
open('__test/migrate.html','w',encoding='utf-8').write(src[:j]+'\n'+block+src[j:])

tz = """<script>
(function(){var P=Date.prototype;P.getHours=P.getUTCHours;P.getMinutes=P.getUTCMinutes;P.getSeconds=P.getUTCSeconds;P.getFullYear=P.getUTCFullYear;P.getMonth=P.getUTCMonth;P.getDate=P.getUTCDate;P.getDay=P.getUTCDay;P.getMilliseconds=P.getUTCMilliseconds;P.getTimezoneOffset=function(){return 0;};})();
</script>
"""
open('__test/tz-utc.html','w',encoding='utf-8').write(src[:j]+'\n'+tz+src[j:])
target = calendar.timegm(datetime.datetime(2026,11,23,0,30,0).timetuple()) - 9*3600
edge = """<script>
(function(){var T0=Date.now();var TARGET=%d;var RN=Date.now;Date.now=function(){return TARGET+(RN()-T0);};})();
</script>
""" % (target*1000,)
open('__test/tz-utc-edge.html','w',encoding='utf-8').write(src[:j]+'\n'+tz+edge+src[j:])
print('ok')
