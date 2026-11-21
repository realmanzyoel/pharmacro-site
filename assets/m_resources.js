/* Resources: list filters, webinar countdown + .ics, glossary search. */
(function(){
var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
/* filters: each .rs-flt filters items carrying data-<attr>; several groups combine with AND */
var F=$$('.rs-flt');if(F.length){var st={},attrs=F.map(function(f){return f.dataset.attr}),items=$$(attrs.map(function(a){return '[data-'+a+']'}).join(',')).filter(function(e){return !e.classList.contains('big')&&!e.closest('.rs-flt')}),nr=d.querySelector('main .nores');
 function ap(){var n=0;items.forEach(function(e){var ok=attrs.every(function(a){return !st[a]||e.getAttribute('data-'+a)===st[a]});e.hidden=!ok;if(ok)n++});if(nr)nr.hidden=!!n}
 F.forEach(function(f){var B=$$('button',f);B.forEach(function(b){b.addEventListener('click',function(){st[f.dataset.attr]=b.dataset.v;B.forEach(function(x){x.setAttribute('aria-pressed',x===b)});ap()})})})}
/* countdown */
$$('.rs-cd').forEach(function(c){var to=Date.parse(c.dataset.to),U={};$$('[data-u]',c).forEach(function(b){U[b.dataset.u]=b});
 function up(){var s=Math.max(0,Math.floor((to-Date.now())/1000));U.d.textContent=Math.floor(s/86400);U.h.textContent=Math.floor(s%86400/3600);U.m.textContent=Math.floor(s%3600/60);U.s.textContent=s%60}
 up();setInterval(up,rm?60000:1000)});
/* add to calendar: build an .ics file in the browser */
function ic(t){return new Date(t).toISOString().replace(/[-:]/g,'').replace(/\.\d{3}/,'')}
$$('.rs-ics').forEach(function(b){b.addEventListener('click',function(){var s=Date.parse(b.dataset.start),e=s+(+b.dataset.dur||60)*60000,
 txt=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//PharmaCRO//Webinars//EN','BEGIN:VEVENT','UID:'+s+'@pharma.eliteleadgrow.com','DTSTAMP:'+ic(Date.now()),'DTSTART:'+ic(s),'DTEND:'+ic(e),
  'SUMMARY:'+b.dataset.title.replace(/[,;]/g,' '),'DESCRIPTION:PharmaCRO webinar (illustrative schedule). Join link sent after registration.','URL:'+location.href,'END:VEVENT','END:VCALENDAR'].join('\r\n'),
 a=d.createElement('a');a.href=URL.createObjectURL(new Blob([txt],{type:'text/calendar'}));a.download='pharmacro-webinar.ics';d.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500)})});
/* glossary search */
$$('.rs-gq').forEach(function(q){var T=$$('.rs-gt'),S=$$('.rs-gs'),nr=d.querySelector('main .nores');q.addEventListener('input',function(){var v=q.value.trim().toLowerCase(),n=0;
 T.forEach(function(t){var ok=!v||t.textContent.toLowerCase().indexOf(v)>-1;t.hidden=!ok;if(ok)n++});S.forEach(function(s){s.hidden=!s.querySelector('.rs-gt:not([hidden])')});if(nr)nr.hidden=!!n})});
})();
