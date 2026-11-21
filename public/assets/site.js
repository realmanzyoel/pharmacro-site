(function(){
var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches,fine=matchMedia('(pointer:fine)').matches;
function fmt(n,dec,comma){var s=n.toFixed(dec);return comma?Number(s).toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec}):s}
function count(el){var to=parseFloat(el.dataset.to),dec=+el.dataset.dec,pre=el.dataset.pre||'',suf=el.dataset.suf||'',cm=el.dataset.comma==='1';
 if(rm){return}var t0=performance.now(),D=1500;(function f(t){var p=Math.min(1,(t-t0)/D),e=1-Math.pow(1-p,4);el.textContent=pre+fmt(to*e,dec,cm)+suf;if(p<1)requestAnimationFrame(f)})(t0)}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var el=e.target;el.classList.add('in');io.unobserve(el);
 el.querySelectorAll('.cnt').forEach(count);setTimeout(function(){el.classList.add('done')},1600)})},{threshold:.12,rootMargin:'0px 0px -5% 0px'});
d.querySelectorAll('.reveal,.tl,.ringw').forEach(function(el){io.observe(el)});
/* tilt + glow */
if(fine&&!rm){d.querySelectorAll('.tilt').forEach(function(el){el.addEventListener('pointermove',function(e){var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
 el.style.setProperty('--ry',((x-.5)*6).toFixed(2)+'deg');el.style.setProperty('--rx',((.5-y)*6).toFixed(2)+'deg');el.style.setProperty('--mx',(x*100)+'%');el.style.setProperty('--my',(y*100)+'%')});
 el.addEventListener('pointerleave',function(){el.style.setProperty('--rx','0deg');el.style.setProperty('--ry','0deg')})});
 d.querySelectorAll('.cine').forEach(function(h){h.addEventListener('pointermove',function(e){var r=h.getBoundingClientRect();h.style.setProperty('--mx',(e.clientX-r.left)+'px');h.style.setProperty('--my',(e.clientY-r.top)+'px')})})}
/* parallax + progress + nav shadow */
var px=[].slice.call(d.querySelectorAll('.px')),cb=[].slice.call(d.querySelectorAll('.cine .cb')),nav=d.querySelector('nav.top'),bar=d.getElementById('prog'),tick=false;
function up(){tick=false;var y=scrollY,h=d.documentElement.scrollHeight-innerHeight;if(bar)bar.style.transform='scaleX('+(h>0?Math.min(1,y/h):0)+')';if(nav)nav.classList.toggle('sc',y>8);
 if(rm)return;px.forEach(function(el){var r=el.parentNode.getBoundingClientRect();if(r.bottom<-100||r.top>innerHeight+100)return;var m=r.height*.11,v=((r.top+r.height/2)-innerHeight/2)*-parseFloat(el.dataset.px||.1);v=Math.max(-m,Math.min(m,v));el.style.transform='translate3d(0,'+v.toFixed(1)+'px,0)'});
 cb.forEach(function(el){el.style.translate='0 '+(y*.12).toFixed(1)+'px'})}
addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(up)}},{passive:true});addEventListener('resize',up);up();

/* constellation canvas */
(function(){var c=d.getElementById('net');if(!c)return;var x=c.getContext('2d'),W=0,H=0,N=[],run=false,mx=-999,my=-999,dpr=Math.min(2,devicePixelRatio||1),cols=['#5ac8fa','#2f6bff','#7ddf00','#ff9f80','#c79bff','#ffd400'];
function size(){var r=c.getBoundingClientRect();W=r.width;H=r.height;c.width=W*dpr;c.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);var n=Math.min(110,Math.round(W*H/15000));N=[];for(var i=0;i<n;i++)N.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.28,vy:(Math.random()-.5)*.28,r:1.2+Math.random()*2.2,c:cols[i%6]})}
function draw(){x.clearRect(0,0,W,H);for(var i=0;i<N.length;i++){var a=N[i];if(!rm){a.x+=a.vx;a.y+=a.vy;if(a.x<0||a.x>W)a.vx*=-1;if(a.y<0||a.y>H)a.vy*=-1;var dx=a.x-mx,dy=a.y-my,q=dx*dx+dy*dy;if(q<14400){var f=(1-q/14400)*.6;a.x+=dx*f*.04;a.y+=dy*f*.04}}
 for(var j=i+1;j<N.length;j++){var b=N[j],ex=a.x-b.x,ey=a.y-b.y,dd=ex*ex+ey*ey;if(dd<16900){x.globalAlpha=(1-dd/16900)*.35;x.strokeStyle=a.c;x.lineWidth=1;x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b.x,b.y);x.stroke()}}
 x.globalAlpha=.9;x.fillStyle=a.c;x.shadowColor=a.c;x.shadowBlur=10;x.beginPath();x.arc(a.x,a.y,a.r,0,6.283);x.fill();x.shadowBlur=0}x.globalAlpha=1}
function loop(){if(!run)return;draw();requestAnimationFrame(loop)}
size();draw();if(rm)return;
new IntersectionObserver(function(es){var v=es[0].isIntersecting;if(v&&!run){run=true;loop()}else if(!v)run=false}).observe(c);
c.parentNode.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top});c.parentNode.addEventListener('pointerleave',function(){mx=my=-999});
var rt;addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(size,200)})})();
/* scrollytelling */
(function(){var st=d.querySelector('.story');if(!st)return;var im=st.querySelectorAll('.st-img'),dt=st.querySelectorAll('.st-dot'),steps=st.querySelectorAll('.st-step');
var o=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var i=+e.target.dataset.i;im.forEach(function(m,k){m.classList.toggle('on',k===i)});dt.forEach(function(m,k){m.classList.toggle('on',k===i)});steps.forEach(function(m,k){m.classList.toggle('on',k===i)});st.style.setProperty('--ac',e.target.dataset.c)})},{rootMargin:'-42% 0px -42% 0px'});
steps.forEach(function(s){o.observe(s)});if(steps[0])steps[0].classList.add('on')})();
})();

/* PharmaCRO behaviours (runs after il.js: reveal/count/tilt/parallax already wired). Vanilla, no dependencies. */
(function(){
var d=document,W=window,rm=matchMedia('(prefers-reduced-motion:reduce)').matches,fine=matchMedia('(pointer:fine)').matches,ROOT=d.body.dataset.root||'';
function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
function ls(k,v){try{if(v===undefined)return localStorage.getItem(k);localStorage.setItem(k,v)}catch(e){return null}}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function addDays(n){var t=new Date(),k=0;while(k<n){t.setDate(t.getDate()+1);var w=t.getDay();if(w&&w<6)k++}return t}
function fmtD(t){return t.toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short',year:'numeric'})}
function ref(){var t=new Date();return 'RFQ-'+String(t.getFullYear()).slice(2)+('0'+(t.getMonth()+1)).slice(-2)+('0'+t.getDate()).slice(-2)+'-'+Math.random().toString(36).slice(2,6).toUpperCase()}
/* make sure late-added reveal elements also animate */
if('IntersectionObserver' in W){var io2=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io2.unobserve(e.target)}})},{threshold:.15});
 $$('.sig,.num,.icard,.audit,.gantt,.hs-i,.pull,.tick-in').forEach(function(el){io2.observe(el)})}
/* animate count-ups that are not inside a .reveal */
$$('.cs-c .cnt').forEach(function(){});

/* ---------- theme, region ---------- */
var html=d.documentElement;
$$('.thm').forEach(function(b){b.addEventListener('click',function(e){var dark=getComputedStyle(html).colorScheme.indexOf('dark')>-1;var n=dark?'light':'dark';
 function go(){html.dataset.theme=n;ls('pc-theme',n)}
 if(d.startViewTransition&&!rm){var r=b.getBoundingClientRect();html.style.setProperty('--vx',(r.left+r.width/2)+'px');html.style.setProperty('--vy',(r.top+r.height/2)+'px');d.startViewTransition(go)}else go()})});
function region(r){html.dataset.region=r;ls('pc-region',r);$$('[data-region]').forEach(function(s){s.value=r});
 $$('.rg').forEach(function(g){var k=g.dataset.reg;g.classList.toggle('lit',r==='global'?k==='global'||k==='us'||k==='eu':k===r||k==='global')})}
$$('[data-region]').forEach(function(s){s.addEventListener('change',function(){region(s.value)})});region(ls('pc-region')||'global');

/* ---------- nav: burger, mega-menu panel, labs mini-map ---------- */
var bg=$('.burger'),mn=$('#mnav');if(bg&&mn)bg.addEventListener('click',function(){var o=mn.hidden;mn.hidden=!o;bg.setAttribute('aria-expanded',o)});
var mf=$('.mm-f');if(mf){var MM=JSON.parse(mf.dataset.mmdata),im=$('img',mf),h=$('.mm-h',mf),t=$('.mm-t',mf),k=$('.mm-k',mf),bt=$('.btn',mf);
 $$('[data-mm]').forEach(function(a){function show(){var s=MM[+a.dataset.mm];im.src=ROOT+'img/'+s.img+'.jpg';k.textContent='Typical TAT '+s.tat;h.textContent=s.h;t.textContent='Key test: '+s.t+'.';bt.textContent='Request a quote';bt.href=ROOT+'request-quote.html?service='+a.dataset.mm}
 a.addEventListener('mouseenter',show);a.addEventListener('focus',show)})}
$$('.lab-dd').forEach(function(p){var c=$('.mi-c',p),f=$('.mi-f',p),ph=$('.mi-p',p);$$('.mp',p).forEach(function(a){function s(){c.textContent=a.dataset.c;f.textContent=a.dataset.f;ph.textContent='Planned opening: '+a.dataset.p}a.addEventListener('mouseenter',s);a.addEventListener('focus',s)})});

/* ---------- search overlay (press /) ---------- */
var so=$('.srch-o'),IDX=null;
function loadIdx(cb){if(IDX)return cb(IDX);fetch(ROOT+'assets/search.json').then(function(r){return r.json()}).then(function(j){IDX=j;cb(j)}).catch(function(){IDX=[];cb(IDX)})}
var SYN={nitrosamine:'nitrosamine ndsri',ivb:'zone ivb stability 30 75',zone:'stability climatic zone',lal:'endotoxin',sterility:'sterility microbiology',mrna:'mrna lnp capping',aav:'aav capsid gene therapy',cgt:'cell gene therapy',el:'extractables leachables',ada:'immunogenicity ada',pk:'bioanalytical pk'};
function score(q,e){var w=q.toLowerCase().split(/\s+/).filter(Boolean),s=0;w.forEach(function(x){if(SYN[x])x=x+' '+SYN[x];x.split(' ').forEach(function(y){if(y.length<2)return;if(e.t.toLowerCase().indexOf(y)>-1)s+=6;if(e.d.toLowerCase().indexOf(y)>-1)s+=3;if(e.k.indexOf(y)>-1)s+=1})});return s}
function search(q){return IDX.map(function(e){return [score(q,e),e]}).filter(function(x){return x[0]>2}).sort(function(a,b){return b[0]-a[0]}).map(function(x){return x[1]})}
var GN={services:'Services',solutions:'Services',industries:'Industries',labs:'Labs','method library':'Methods',insights:'Articles',quality:'Quality',tools:'Tools',technology:'Technology',careers:'Company',about:'Company',portal:'Technology'};
function soRender(q){var r=$('.so-r',so);if(!q){r.innerHTML='<p class="so-g">Popular</p><a href="'+ROOT+'services/small-molecule-qc-release.html"><b>Small molecule QC and release</b></a><a href="'+ROOT+'tools/stability-study-designer.html"><b>Stability Study Designer</b></a><a href="'+ROOT+'method-library/index.html"><b>Method Library</b></a><a href="'+ROOT+'request-quote.html"><b>Request a quote</b></a>';return}
 var res=search(q).slice(0,18),g={};res.forEach(function(e){var k=GN[e.s]||'Pages';(g[k]=g[k]||[]).push(e)});
 r.innerHTML=res.length?['Services','Methods','Labs','Articles','Tools','Quality','Industries','Technology','Company','Pages'].filter(function(k){return g[k]}).map(function(k){return '<p class="so-g">'+k+'</p>'+g[k].slice(0,6).map(function(e){return '<a href="'+ROOT+e.p+'"><b>'+esc(e.t)+'</b><span>'+esc(e.d.slice(0,120))+'</span></a>'}).join('')}).join(''):'<p class="so-g">No results</p><a href="'+ROOT+'request-quote.html"><b>Ask us anyway</b><span>We run many methods that are not listed yet.</span></a>'}
function soOpen(){if(!so)return;so.hidden=false;var i=$('input',so);i.value='';loadIdx(function(){soRender('')});setTimeout(function(){i.focus()},30)}
function soClose(){if(so)so.hidden=true}
$$('.srch').forEach(function(b){b.addEventListener('click',soOpen)});
if(so){$('input',so).addEventListener('input',function(e){var v=e.target.value;loadIdx(function(){soRender(v)})});so.addEventListener('click',function(e){if(e.target===so)soClose()})}
d.addEventListener('keydown',function(e){var tg=(e.target.tagName||'').toLowerCase();if(e.key==='/'&&tg!=='input'&&tg!=='textarea'&&tg!=='select'){e.preventDefault();soOpen()}if(e.key==='Escape'){soClose();var cd=$('.cn-d');if(cd)cd.hidden=true}});

/* ---------- mail forms (no backend: open the visitor's mail app) ---------- */
function mailto(to,subj,lines){location.href='mailto:'+to+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(lines.join('\n'))}
$$('form.mf').forEach(function(f){f.addEventListener('submit',function(e){e.preventDefault();var bad=$$('[required]',f).filter(function(x){return x.type==='checkbox'?!x.checked:!x.value.trim()||(x.type==='email'&&!/^\S+@\S+\.\S+$/.test(x.value))});
 $$('[aria-invalid]',f).forEach(function(x){x.removeAttribute('aria-invalid')});if(bad.length){bad.forEach(function(x){x.setAttribute('aria-invalid','true')});bad[0].focus();return}
 var id=ref(),L=['Reference: '+id,'Page: '+location.pathname,''];$$('input,select,textarea',f).forEach(function(x){if(!x.name||x.type==='file')return;var l=(x.closest('label')||{}).textContent||x.name;L.push(l.trim().split('\n')[0].slice(0,60)+': '+(x.type==='checkbox'?(x.checked?'yes':'no'):x.value))});
 mailto(f.dataset.mail,(f.dataset.kind||'Enquiry')+' '+id,L);var ok=$('.mf-ok',f);if(ok)ok.hidden=false;var b=$('button[type=submit]',f);if(b)b.classList.add('sent')})});

/* quick-quote tab, cookie banner */
var qb=$('.qt-b'),qf=$('.qt-f');if(qb&&qf)qb.addEventListener('click',function(){qf.hidden=!qf.hidden;qb.setAttribute('aria-expanded',!qf.hidden);if(!qf.hidden)$('input',qf).focus()});
var ck=$('.ck');if(ck&&!ls('pc-ck')){ck.hidden=false;$$('[data-ck]',ck).forEach(function(b){b.addEventListener('click',function(){ls('pc-ck',b.dataset.ck);ck.hidden=true})})}

/* ---------- Ask the Lab (retrieval over this site's own pages) ---------- */
var ab=$('.ask-b'),ap=$('#askp');
if(ab&&ap){var al=$('.ask-l',ap);function say(h,c){var p=d.createElement('p');p.className='am '+c;p.innerHTML=h;al.appendChild(p);al.scrollTop=al.scrollHeight}
 function ask(q){say(esc(q),'me');if(/emergenc|patient|dose me|diagnos/i.test(q)){say('I can only answer questions about our testing services. For medical questions please speak to a clinician.','bot');return}
  loadIdx(function(){var r=search(q).slice(0,3);if(!r.length){say('I could not find that on our pages. A scientist can answer it: <a href="'+ROOT+'request-quote.html">send it to a scientist</a>.','bot');return}
   var top=r[0];say('Here is what our pages say. <b>'+esc(top.t)+'</b>: '+esc(top.d)+'<span class="src">Source: <a href="'+ROOT+top.p+'">'+esc(top.t)+'</a>'+(r[1]?' &middot; also <a href="'+ROOT+r[1].p+'">'+esc(r[1].t)+'</a>':'')+'</span>'+
    '<span class="src"><a href="'+ROOT+'request-quote.html?q='+encodeURIComponent(q)+'">Send this to a scientist with a pre-filled quote request &rsaquo;</a></span>','bot')})}
 ab.addEventListener('click',function(){ap.hidden=!ap.hidden;ab.setAttribute('aria-expanded',!ap.hidden);if(!ap.hidden)$('input',ap).focus()});
 $('.ask-x',ap).addEventListener('click',function(){ap.hidden=true;ab.setAttribute('aria-expanded','false');ab.focus()});
 $$('.ask-q button',ap).forEach(function(b){b.addEventListener('click',function(){ask(b.textContent)})});
 $('.ask-f',ap).addEventListener('submit',function(e){e.preventDefault();var i=$('input',ap);if(i.value.trim())ask(i.value.trim());i.value=''})}

/* ---------- magnetic buttons ---------- */
if(fine&&!rm)$$('.mag').forEach(function(b){b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.18).toFixed(1)+'px,'+((e.clientY-r.top-r.height/2)*.28).toFixed(1)+'px)'});b.addEventListener('pointerleave',function(){b.style.transform=''})});

/* ---------- molecule / chromatogram canvases (hero + quote bands) ---------- */
function field(c,o){var x=c.getContext('2d'),dpr=Math.min(2,W.devicePixelRatio||1),Wd=0,H=0,N=[],mx=-999,my=-999,run=false,t=0;
 function size(){var r=c.getBoundingClientRect();Wd=r.width;H=r.height;c.width=Wd*dpr;c.height=H*dpr;x.setTransform(dpr,0,0,dpr,0,0);var n=Math.min(o.max||90,Math.round(Wd*H/(o.den||14000)));N=[];for(var i=0;i<n;i++)N.push({x:Math.random()*Wd,y:Math.random()*H,vx:(Math.random()-.5)*.25,vy:(Math.random()-.5)*.25,r:1+Math.random()*2.4})}
 function draw(){x.clearRect(0,0,Wd,H);t+=.006;
  if(o.waves){for(var k=0;k<3;k++){x.beginPath();for(var px=0;px<=Wd;px+=6){var b=H*(.62+k*.09),dx=px-mx,dy=b-my,pull=Math.exp(-(dx*dx+dy*dy)/26000)*40,pk=0;
    [.18,.42,.66,.84].forEach(function(p,j){var c0=Wd*p+Math.sin(t*2+j+k)*20,w=18+j*6;pk+=Math.exp(-Math.pow(px-c0,2)/(2*w*w))*(60+j*25)*(1-k*.3)});
    var y=b-pk-pull+Math.sin(px*.01+t*3+k)*4;px?x.lineTo(px,y):x.moveTo(px,y)}x.strokeStyle='rgba(0,184,169,'+(.55-k*.15)+')';x.lineWidth=1.6-k*.4;x.shadowColor='#00B8A9';x.shadowBlur=k?0:10;x.stroke();x.shadowBlur=0}}
  for(var i=0;i<N.length;i++){var a=N[i];if(!rm){a.x+=a.vx;a.y+=a.vy;if(a.x<0||a.x>Wd)a.vx*=-1;if(a.y<0||a.y>H)a.vy*=-1;var ex=mx-a.x,ey=my-a.y,q=ex*ex+ey*ey;if(q<32000){a.x+=ex*.004;a.y+=ey*.004}}
   for(var j=i+1;j<N.length;j++){var b2=N[j],fx=a.x-b2.x,fy=a.y-b2.y,dd=fx*fx+fy*fy;if(dd<11000){x.globalAlpha=(1-dd/11000)*.4;x.strokeStyle='#7fe7dc';x.lineWidth=1;x.beginPath();x.moveTo(a.x,a.y);x.lineTo(b2.x,b2.y);x.stroke()}}
   x.globalAlpha=.85;x.fillStyle=i%7?'#7fe7dc':'#F2A900';x.beginPath();x.arc(a.x,a.y,a.r,0,6.283);x.fill()}x.globalAlpha=1}
 function loop(){if(!run)return;draw();requestAnimationFrame(loop)}
 size();draw();if(rm)return;new IntersectionObserver(function(es){var v=es[0].isIntersecting;if(v&&!run){run=true;loop()}else if(!v)run=false}).observe(c);
 c.parentNode.addEventListener('pointermove',function(e){var r=c.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top});c.parentNode.addEventListener('pointerleave',function(){mx=my=-999});
 var rt;W.addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(size,200)});return {stop:function(){run=false},start:function(){if(!run){run=true;loop()}}}}
var hero=$('.hero3 canvas');if(hero){var hf=field(hero,{waves:1,max:110,den:12000});var hp=$('.hpause');if(hp&&hf)hp.addEventListener('click',function(){var p=hp.getAttribute('aria-pressed')==='true';hp.setAttribute('aria-pressed',!p);hp.textContent=p?'Pause motion':'Play motion';p?hf.start():hf.stop()})}
$$('canvas.mol').forEach(function(c){field(c,{max:60,den:9000})});

/* live ticker on the home hero (demo numbers that tick) */
$$('[data-tick]').forEach(function(el){var v=parseFloat(el.dataset.tick);if(rm)return;setInterval(function(){v+=Math.random()<.6?1:0;el.textContent=Math.round(v).toLocaleString('en-US')},2600)});

/* ---------- audience router ---------- */
$$('.router').forEach(function(r){var D=JSON.parse(r.dataset.r),o=$('.rt-o',r);
 function show(m,name){if(m==='unsure'){location.href=ROOT+'tools/test-finder.html';return}var L=D[m]||[];$('h3',o).textContent='Tests for '+name.toLowerCase();
  $('.rt-l',o).innerHTML=L.map(function(s){return '<a href="'+ROOT+s.u.slice(1)+'"><b>'+esc(s.n)+'</b><span>'+esc(s.t)+'</span><small>'+esc(s.tat)+'</small></a>'}).join('');
  r.classList.add('open');o.hidden=false;ls('pc-mod',m);ls('pc-modn',name);d.body.dataset.mod=m}
 $$('.rt',r).forEach(function(b){b.addEventListener('click',function(){show(b.dataset.mod,$('b',b).textContent)})});
 $('.rt-back',o).addEventListener('click',function(){r.classList.remove('open');o.hidden=true});
 var m=ls('pc-mod');if(m&&m!=='unsure'&&D[m])show(m,ls('pc-modn')||m)});
/* personalise: highlight service cards for the remembered modality */
(function(){var m=ls('pc-mod');if(m)$$('.svc[data-mod]').forEach(function(c){if(c.dataset.mod.split(' ').indexOf(m)>-1)c.classList.add('lit')})})();

/* ---------- constellation drawer ---------- */
$$('.const').forEach(function(c){var dr=$('.cn-d',c),bd=$('div',dr);
 $$('.cn-n',c).forEach(function(n){n.addEventListener('click',function(){var t=$('template[data-i="'+n.dataset.i+'"]',c);bd.innerHTML='';bd.appendChild(t.content.cloneNode(true));$$('a',bd).forEach(function(a){var h=a.getAttribute('href');if(h&&h[0]==='/')a.setAttribute('href',ROOT+h.slice(1))});dr.hidden=false;$('.cn-x',dr).focus()})});
 $('.cn-x',dr).addEventListener('click',function(){dr.hidden=true})});

/* ---------- network map ---------- */
$$('.lmap').forEach(function(m){var L=JSON.parse(m.dataset.labs),svg=$('svg',m),g=$('.pins',svg),ag=$('.arcs',svg),card=$('.lm-card',m),NS='http://www.w3.org/2000/svg',sel=null,reg={},svc='',els=[];
 function q(s){var h=0;for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))%997;return h}
 function info(l){var qd=3+q(l.s)%9,slot=addDays(2+q(l.s)%5);card.innerHTML='<p class="ey">'+esc(l.r)+' &middot; planned '+esc(l.ph)+'</p><h3>'+esc(l.c)+', '+esc(l.co)+'</h3><p>'+esc(l.f)+'</p><ul>'+l.sp.map(function(s){return '<li>'+esc(s)+'</li>'}).join('')+'</ul>'+
  '<p class="q"><span>Queue: '+qd+' batches</span><span>Next slot: '+fmtD(slot)+'</span></p><p><a class="btn sm" href="'+ROOT+'labs/'+l.s+'.html">Lab page</a> <a class="btn sm o" href="'+ROOT+'request-quote.html">Quote</a></p><p class="cn">Planned site. Queue and slot are simulated.</p>'}
 L.forEach(function(l){var e=d.createElementNS(NS,'g');e.setAttribute('class','pin');e.setAttribute('tabindex','0');e.setAttribute('role','button');e.setAttribute('aria-label',l.c+', '+l.co+': '+l.f);
  var h=d.createElementNS(NS,'circle'),c=d.createElementNS(NS,'circle');h.setAttribute('class','halo');c.setAttribute('class','core');[h,c].forEach(function(x){x.setAttribute('cx',l.x);x.setAttribute('cy',l.y);x.setAttribute('r',5.5);e.appendChild(x)});
  e.style.setProperty('--sp',(1.4+(q(l.s)%10)/6).toFixed(2)+'s');
  function pick(){if(sel)sel.classList.remove('sel');sel=e;e.classList.add('sel');info(l)}
  e.addEventListener('mouseenter',function(){info(l)});e.addEventListener('focus',pick);e.addEventListener('click',pick);e.addEventListener('keydown',function(k){if(k.key==='Enter'){location.href=ROOT+'labs/'+l.s+'.html'}});g.appendChild(e);els.push([e,l])});
 function filt(){var any=Object.keys(reg).some(function(k){return reg[k]});els.forEach(function(x){var l=x[1],ok=(!any||reg[l.r])&&(!svc||l.spk.indexOf(svc)>-1);x[0].classList.toggle('dim',!ok)})}
 $$('[data-mr]',m).forEach(function(b){b.addEventListener('click',function(){reg[b.dataset.mr]=!reg[b.dataset.mr];b.setAttribute('aria-pressed',!!reg[b.dataset.mr]);filt()})});
 var ms=$('[data-ms]',m);if(ms)ms.addEventListener('change',function(){svc=ms.value;filt()});
 var ab=$('[data-arcs]',m);if(ab)ab.addEventListener('click',function(){var on=ab.getAttribute('aria-pressed')!=='true';ab.setAttribute('aria-pressed',on);ag.innerHTML='';if(!on)return;var hub=L[0];
  L.slice(1).forEach(function(l,i){var p=d.createElementNS(NS,'path'),mx=(hub.x+l.x)/2,my=Math.min(hub.y,l.y)-Math.abs(hub.x-l.x)*.25-20;p.setAttribute('d','M'+hub.x+','+hub.y+' Q'+mx+','+my+' '+l.x+','+l.y);p.setAttribute('class','arc');p.style.animationDelay=(i*.1)+'s';ag.appendChild(p)});
  card.innerHTML='<p class="ey">Method transfer</p><h3>Validated once. Run anywhere.</h3><p>Methods developed at the Hyderabad flagship transfer to every site on the same SOPs, instruments and LIMS, so a transfer takes days instead of months.</p>'});
 var nf=$('.lm-near',m);if(nf)nf.addEventListener('submit',function(e){e.preventDefault();var v=$('input',nf).value.trim().toLowerCase(),C=W.PC_CITIES||{},k=Object.keys(C).filter(function(c){return c.toLowerCase()===v||c.toLowerCase().indexOf(v)===0})[0];
  if(!k){card.innerHTML='<h3>City not found</h3><p>Try a nearby major city, for example Ahmedabad, Basel or Boston.</p>';return}var p=C[k],best=null,bd=1e9;
  L.forEach(function(l){var R=Math.PI/180,a=Math.sin((l.la-p[0])*R/2),b=Math.sin((l.lo-p[1])*R/2),dd=12742*Math.asin(Math.sqrt(a*a+Math.cos(p[0]*R)*Math.cos(l.la*R)*b*b));if(dd<bd){bd=dd;best=l}});
  $$('.you,.yl',svg).forEach(function(x){x.remove()});var yx=(p[1]+180)*2.7778,yy=(80-p[0])*2.7778,ln=d.createElementNS(NS,'path');ln.setAttribute('d','M'+yx+','+yy+' L'+best.x+','+best.y);ln.setAttribute('class','yl');svg.appendChild(ln);
  var yc=d.createElementNS(NS,'circle');yc.setAttribute('cx',yx);yc.setAttribute('cy',yy);yc.setAttribute('r',5);yc.setAttribute('class','you');svg.appendChild(yc);
  info(best);card.insertAdjacentHTML('afterbegin','<p class="ey">Nearest to '+esc(k)+': about '+Math.round(bd).toLocaleString('en-US')+' km</p>')})});

/* ---------- vial journey ---------- */
$$('.vj').forEach(function(v){var S=$$('.vj-s',v),I=$$('.vj-im',v),M=$$('.vj-m',v),st=$('.vj-state',v),fl=$('.vj-fl',v),vial=$('.vj-vial',v),pts=$('.vj-tr',v).getAttribute('points').split(' ').map(function(p){return p.split(',').map(Number)});
 var NM={sealed:'Sealed',opened:'Opened and logged',instrument:'On instrument',reported:'Reported, CoA e-signed'};
 function at(f){var n=pts.length-1,s=Math.min(n-1e-6,Math.max(0,f*n)),i=Math.floor(s),t=s-i,a=pts[i],b=pts[i+1];return [a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t]}
 function up(){var r=$('.vj-st',v).getBoundingClientRect(),f=Math.min(1,Math.max(0,(innerHeight*.5-r.top)/(r.height-innerHeight*.3)));var p=at(f);vial.setAttribute('transform','translate('+p[0]+','+(p[1]-6)+')');fl.style.setProperty('--o',1-f);
  var k=Math.min(S.length-1,Math.round(f*(S.length-1)));S.forEach(function(s,i){s.classList.toggle('on',i===k)});I.forEach(function(s,i){s.classList.toggle('on',i===k)});M.forEach(function(s,i){s.classList.toggle('on',i<=k)});var sd=S[k].dataset.st;v.dataset.st=sd;st.textContent=NM[sd]||sd}
 W.addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});up()});

/* ---------- step line ---------- */
$$('.sline').forEach(function(o){var l=$('.sl-l span',o),it=$$('.sl-i',o);function up(){var r=o.getBoundingClientRect(),f=Math.min(1,Math.max(0,(innerHeight*.6-r.top)/r.height));l.style.setProperty('--p',(f*100)+'%');it.forEach(function(x,i){x.classList.toggle('on',f>=(i+.2)/it.length)})}
 W.addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});up()});

/* ---------- clock sweep ---------- */
$$('.tclock').forEach(function(c){var sw=$('.tc-sw',c),hd=$('.tc-h',c),lb=$('.tc-l',c);function up(){var r=c.getBoundingClientRect(),f=Math.min(1,Math.max(0,(innerHeight-r.top)/(innerHeight+r.height*.6))),a=f*.999*2*Math.PI,x=100+88*Math.sin(a),y=100-88*Math.cos(a);
 sw.setAttribute('d','M100 100L100 12A88 88 0 '+(a>Math.PI?1:0)+' 1 '+x.toFixed(1)+' '+y.toFixed(1)+'Z');hd.style.setProperty('--rot',(f*360)+'deg');lb.textContent=Math.round(72-f*48)+' h'}
 W.addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});up()});

/* ---------- turnaround tiers + TAT estimator ---------- */
$$('.tiers').forEach(function(t){var B=$$('[role=tab]',t);function sel(b){B.forEach(function(x){x.setAttribute('aria-selected',x===b)});$('.ti-d',t).textContent=fmtD(addDays(+b.dataset.d));$('.ti-x',t).textContent=b.dataset.x;$('.ti-m',t).textContent='Indicative price multiplier '+b.dataset.m+' · '+b.dataset.d+' business days';var f=t.closest('form');if(f)f.dataset.tier=b.textContent}
 B.forEach(function(b){b.addEventListener('click',function(){sel(b)})});sel(B[0])});
$$('.tcalc').forEach(function(c){var di=$('[data-tq=d]',c),s=$('[data-tq=s]',c),t=$('[data-tq=t]',c),o=$('.tq-o',c),base=[6,7,30,10,8,7,9,4,40,20,6,20];di.valueAsDate=new Date();
 function up(){var dd=di.valueAsDate||new Date(),n=Math.max(1,Math.round(base[+s.value]*parseFloat(t.value))),r=new Date(dd),k=1;while(k<=n+1){r.setDate(r.getDate()+1);if(r.getDay()&&r.getDay()<6)k++}
  o.innerHTML='Ship on '+fmtD(dd)+', results by <b>'+fmtD(r)+'</b> ('+n+' business days in the lab plus one for receipt).'}[di,s,t].forEach(function(x){x.addEventListener('input',up)});up()});

/* ---------- portal mock: scroll-scrubbed statuses, toasts, tilt ---------- */
$$('.pmock').forEach(function(p){var R=$$('.pm-r',p),T=$('.pm-toasts',p),k2=$('.pm-k2',p),k1=$('.pm-k1',p),dev=$('.pm-dev',p),N=['Received','In analysis','Under review','Released'],last={};
 function toast(h,b){var e=d.createElement('div');e.className='toast';e.innerHTML='<b>'+h+'</b>'+b;T.appendChild(e);if(T.children.length>2)T.removeChild(T.firstChild);setTimeout(function(){if(e.parentNode)e.remove()},5200)}
 function up(){var r=p.getBoundingClientRect(),f=Math.min(1,Math.max(0,(innerHeight*.85-r.top)/(r.height+innerHeight*.3))),rel=0;
  R.forEach(function(x,i){var s=Math.max(0,Math.min(3,Math.floor(f*4.6-i*.35))),el=$('.pm-s',x);if(+el.dataset.st!==s){el.dataset.st=s;el.textContent=N[s];if(last[i]!==undefined&&s>last[i])toast(N[s],$('.pm-id',x).textContent+' · '+$('.pm-n',x).firstChild.textContent);last[i]=s}if(last[i]===undefined)last[i]=s;$('.pm-b i',x).style.setProperty('--p',(8+s*30.6)+'%');if(s===3)rel++});
  k2.textContent=rel;k1.textContent=R.length-rel}
 W.addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});up();
 if(fine&&!rm)p.addEventListener('pointermove',function(e){var r=p.getBoundingClientRect();dev.style.setProperty('--ty',(((e.clientX-r.left)/r.width-.5)*10).toFixed(1)+'deg');dev.style.setProperty('--tx',((.5-(e.clientY-r.top)/r.height)*8).toFixed(1)+'deg')})});

/* ---------- flips, ALCOA, accordions (one open, deep links) ---------- */
$$('.flip').forEach(function(f){f.addEventListener('click',function(){f.setAttribute('aria-pressed',f.getAttribute('aria-pressed')!=='true')})});
$$('.alcoa').forEach(function(a){var B=$$('.al-l',a),P=$$('.al-p',a);B.forEach(function(b){b.addEventListener('click',function(){B.forEach(function(x){x.setAttribute('aria-pressed',x===b)});P.forEach(function(p){p.classList.toggle('on',p.dataset.i===b.dataset.i)})})})});
$$('.accs.one').forEach(function(g){var D=$$('details',g);D.forEach(function(x){x.addEventListener('toggle',function(){if(x.open)D.forEach(function(y){if(y!==x)y.open=false})})})});
if(location.hash){var tg=d.getElementById(location.hash.slice(1));if(tg&&tg.tagName==='DETAILS')tg.open=true}

/* ---------- case carousel: drag with momentum, centred card counts up, expand ---------- */
$$('.cases').forEach(function(c){var t=$('.cs-t',c),C=$$('.cs-c',c),dlg=c.nextElementSibling&&c.nextElementSibling.tagName==='DIALOG'?c.nextElementSibling:$('.cs-d'),down=false,sx=0,sl=0,v=0,lx=0,moved=0;
 t.addEventListener('pointerdown',function(e){if(e.pointerType!=='mouse')return;down=true;moved=0;sx=lx=e.clientX;sl=t.scrollLeft;t.classList.add('drag')});
 W.addEventListener('pointermove',function(e){if(!down)return;v=e.clientX-lx;lx=e.clientX;moved+=Math.abs(v);t.scrollLeft=sl-(e.clientX-sx)});
 W.addEventListener('pointerup',function(){if(!down)return;down=false;t.classList.remove('drag');(function m(){if(Math.abs(v)<.5||rm)return;t.scrollLeft-=v;v*=.92;requestAnimationFrame(m)})()});
 function ctr(){var r=t.getBoundingClientRect(),mid=r.left+r.width/2;C.forEach(function(x){var b=x.getBoundingClientRect(),on=Math.abs(b.left+b.width/2-mid)<b.width/2;if(on&&!x.classList.contains('ctr')){var n=$('.cnt',x);if(n&&!rm){var to=+n.dataset.to,t0=performance.now();(function f(tt){var p=Math.min(1,(tt-t0)/900);n.textContent=Math.round(to*(1-Math.pow(1-p,3)));if(p<1)requestAnimationFrame(f)})(t0)}}x.classList.toggle('ctr',on)})}
 t.addEventListener('scroll',function(){requestAnimationFrame(ctr)},{passive:true});ctr();
 $('.cs-p',c).addEventListener('click',function(){t.scrollBy({left:-460,behavior:'smooth'})});$('.cs-nx',c).addEventListener('click',function(){t.scrollBy({left:460,behavior:'smooth'})});
 function open(x){if(moved>8)return;var b=$('.cs-b',dlg);b.innerHTML='';b.appendChild($('template',x).content.cloneNode(true));$$('a',b).forEach(function(a){var h=a.getAttribute('href');if(h&&h[0]==='/')a.setAttribute('href',ROOT+h.slice(1))});
  function go(){dlg.showModal()}if(d.startViewTransition&&!rm)d.startViewTransition(go);else go()}
 C.forEach(function(x){x.addEventListener('click',function(){open(x)});x.addEventListener('keydown',function(e){if(e.key==='Enter')open(x)})});
 if(dlg){$('.cs-cl',dlg).addEventListener('click',function(){dlg.close()});dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()})}});

/* ---------- lifecycle highlight (scroll) ---------- */
$$('.lcyc').forEach(function(l){var C=$$('.lc-c',l),b=$('.lc-bar',l);function up(){var r=l.getBoundingClientRect(),f=Math.min(.999,Math.max(0,(innerHeight*.75-r.top)/(innerHeight*.9))),k=Math.floor(f*C.length);b.style.setProperty('--k',k);C.forEach(function(c,i){c.classList.toggle('on',i===k)})}
 W.addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});up()});

/* ---------- service grid filters + hub search ---------- */
$$('.sf').forEach(function(f){var g=f.nextElementSibling,cards=$$('.svc',g),none=g.nextElementSibling,st={mod:'',stg:''};
 function ap(q){var n=0;cards.forEach(function(c){var ok=(!st.mod||c.dataset.mod.split(' ').indexOf(st.mod)>-1)&&(!st.stg||c.dataset.stg.split(' ').indexOf(st.stg)>-1)&&(!q||c.dataset.q.indexOf(q)>-1);
  function s(){c.classList.toggle('hide',!ok)}if(d.startViewTransition&&!rm){c.style.viewTransitionName='svc'+cards.indexOf(c)}s();if(ok)n++});if(none)none.hidden=!!n}
 W.PC_SVCQ=function(q){if(d.startViewTransition&&!rm)d.startViewTransition(function(){ap(q)});else ap(q)};
 $$('[data-f]',f).forEach(function(b){b.addEventListener('click',function(){var k=b.dataset.f;if(k==='clear'){st={mod:'',stg:''}}else{st[k]=st[k]===b.dataset.v?'':b.dataset.v}
  $$('[data-f]',f).forEach(function(x){if(x.dataset.v)x.setAttribute('aria-pressed',st[x.dataset.f]===x.dataset.v)});W.PC_SVCQ(($('[data-svcq]')||{}).value||'')})})});
$$('[data-svcq]').forEach(function(i){i.addEventListener('input',function(){if(W.PC_SVCQ)W.PC_SVCQ(i.value.trim().toLowerCase())})});

/* ---------- sortable table ---------- */
$$('table.sort').forEach(function(t){$$('th button',t).forEach(function(b){b.addEventListener('click',function(){var k=+b.dataset.k,tb=$('tbody',t),R=$$('tr',tb),dir=b.dataset.dir==='a'?-1:1;b.dataset.dir=dir>0?'a':'d';
 R.sort(function(x,y){var a=x.children[k],c=y.children[k],va=a.dataset.v?+a.dataset.v:a.textContent,vc=c.dataset.v?+c.dataset.v:c.textContent;return (va>vc?1:va<vc?-1:0)*dir}).forEach(function(r){tb.appendChild(r)})})})});

/* ---------- tests table ---------- */
$$('.tt').forEach(function(t){var q=$('[data-tt=q]',t),s=$('[data-tt=s]',t),R=$$('.tt-r',t),c=$('.tt-c',t),nr=$('.nores',t);if(!q||!s)return;function up(){var v=q.value.toLowerCase(),sv=s.value,n=0;R.forEach(function(r){var ok=(!v||r.textContent.toLowerCase().indexOf(v)>-1)&&(!sv||r.dataset.s.indexOf(sv)>-1);r.classList.toggle('hide',!ok);if(ok)n++});c.textContent=n+' of '+R.length+' tests';nr.hidden=!!n}
 q.addEventListener('input',up);s.addEventListener('change',up);up()});

/* ---------- checklist ring ---------- */
$$('.cring').forEach(function(c){var X=$$('[data-cr]',c),f=$('.cr-f',c),b=$('.cr-r b',c),u=$('.cr-u',c);function up(){var n=X.filter(function(x){return x.checked}).length,p=Math.round(n/X.length*100);f.style.setProperty('--p',p);b.textContent=p+'%';u.setAttribute('aria-disabled',p<100)}X.forEach(function(x){x.addEventListener('change',up)});up()});

/* ---------- matrix column highlight ---------- */
$$('.mtx').forEach(function(m){$$('td',m).forEach(function(td){td.addEventListener('mouseenter',function(){var c=td.dataset.c;$$('td.col',m).forEach(function(x){x.classList.remove('col')});$$('td[data-c="'+c+'"]',m).forEach(function(x){x.classList.add('col')})})});m.addEventListener('mouseleave',function(){$$('td.col',m).forEach(function(x){x.classList.remove('col')})})});

/* ---------- masonry lightbox ---------- */
$$('.mas').forEach(function(m){var lb=m.nextElementSibling;if(!lb)return;$$('.ms-i',m).forEach(function(b){b.addEventListener('click',function(){$('img',lb).src=$('img',b).src;$('img',lb).alt=$('img',b).alt;$('p',lb).textContent=b.dataset.cap;lb.showModal()})});$('.lb-x',lb).addEventListener('click',function(){lb.close()});lb.addEventListener('click',function(e){if(e.target===lb)lb.close()})});

/* ---------- RFQ (4 steps) ---------- */
$$('.rfq').forEach(function(f){var S=$$('.rq-s',f),P=$$('.rq-p li',f),k=0,bk=$('.rq-b',f),nx=$('.rq-x',f),go=$('.rq-go',f),er=$('.rq-err',f),sug=$('.rq-sug',f),u=new URLSearchParams(location.search);
 var SUG={'Small Molecule QC and Release':'Customers who order release testing often add Stability Studies and Microbiology.','Biologics Characterization and Release':'Biosimilar programmes usually add Bioanalytical and Immunogenicity.','mRNA and Vaccine Testing':'mRNA release normally includes Microbiology and Sterility (endotoxin, sterility).','Cell and Gene Therapy Testing':'CGT release usually includes rapid sterility and mycoplasma.','Stability Studies':'Stability programmes often need Method Validation first.'};
 if(u.get('service')!==null){var cb=$$('input[name=tests]',f)[+u.get('service')];if(cb)cb.checked=true}if(u.get('q'))$('[name=detail]',f).value=u.get('q');var m=ls('pc-modn');if(m)$$('input[name=modality]',f).forEach(function(r){if(r.value===m)r.checked=true});
 $$('input[name=tests]',f).forEach(function(c){c.addEventListener('change',function(){var s=$$('input[name=tests]:checked',f).map(function(x){return SUG[x.value]}).filter(Boolean);sug.textContent=s[0]||''})});
 function val(){var bad=$$('[required]',S[k]).filter(function(x){return x.type==='checkbox'?!x.checked:!x.value.trim()||(x.type==='email'&&!/^\S+@\S+\.\S+$/.test(x.value))});if(k===0&&!$$('input[name=tests]:checked',f).length&&!$('[name=detail]',f).value.trim()){er.textContent='Choose at least one service or describe the tests.';return false}
  if(bad.length){er.textContent='Please complete: '+bad.map(function(x){return (x.closest('label').querySelector('span')||{}).textContent||x.name}).join(', ');bad[0].focus();return false}er.textContent='';return true}
 function data(){var v=function(n){var e=$('[name='+n+']',f);return e?e.value:''};return [['Product type',($('input[name=modality]:checked',f)||{}).value],['Services',$$('input[name=tests]:checked',f).map(function(x){return x.value}).join('; ')||'Not specified'],['Details',v('detail')],['File',($('[name=file]',f).files[0]||{}).name||'None'],
  ['Tier',f.dataset.tier||'Standard'],['Target date',v('date')||'Earliest'],['Samples',v('n')],['Name',v('name')],['Email',v('email')],['Company',v('company')],['Role',v('role')],['Phone',v('phone')],['Country',v('country')],['Existing client',$('[name=existing]',f).checked?'Yes':'No']]}
 function show(){S.forEach(function(s,i){s.classList.toggle('on',i===k)});P.forEach(function(p,i){p.classList.toggle('on',i<=k)});bk.hidden=!k;nx.hidden=k===3;go.hidden=k!==3;
  if(k===3)$('.rq-sum',f).innerHTML='<dl>'+data().map(function(r){return '<dt>'+r[0]+'</dt><dd>'+esc(r[1]||'-')+'</dd>'}).join('')+'</dl>';var lg=$('legend',S[k]);if(lg&&k)lg.scrollIntoView({block:'nearest',behavior:rm?'auto':'smooth'})}
 nx.addEventListener('click',function(){if(val()){k++;show()}});bk.addEventListener('click',function(){k--;er.textContent='';show()});
 f.addEventListener('submit',function(e){e.preventDefault();if(!val())return;var id=ref();mailto(f.dataset.mail,'Quote request '+id,['Reference: '+id,''].concat(data().map(function(r){return r[0]+': '+r[1]})).concat(['','(If you selected a file, please attach it to this email.)']));
  $$('.rq-s,.rq-n,.rq-p',f).forEach(function(x){x.hidden=true;x.classList.remove('on')});var ok=$('.rq-ok',f);$('.rq-id',ok).textContent=id;ok.hidden=false;ok.focus()});show()});

/* ---------- article: TOC, reading progress ---------- */
$$('.art').forEach(function(a){var t=$('.toc ol',a),H=$$('.art-b h2',a);H.forEach(function(h,i){if(!h.id)h.id='s'+(i+1);var li=d.createElement('li');li.innerHTML='<a href="#'+h.id+'">'+esc(h.textContent)+'</a>';t.appendChild(li)});var A=$$('a',t);
 var bar=d.createElement('div');bar.id='rprog';d.body.appendChild(bar);function up(){var r=a.getBoundingClientRect(),f=Math.min(1,Math.max(0,-r.top/(r.height-innerHeight)));bar.style.width=(f*100)+'%';var k=0;H.forEach(function(h,i){if(h.getBoundingClientRect().top<140)k=i});A.forEach(function(x,i){x.classList.toggle('on',i===k)})}
 W.addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});up()});

/* ---------- footer wordmark + back to top ---------- */
var wm=$('.wm span');if(wm&&fine)$('.wm').addEventListener('pointermove',function(e){var r=wm.getBoundingClientRect();wm.style.setProperty('--wx',(e.clientX-r.left)+'px');wm.style.setProperty('--wy',(e.clientY-r.top)+'px')});
$$('.totop').forEach(function(b){b.addEventListener('click',function(){scrollTo({top:0,behavior:rm?'auto':'smooth'})})});
})();

/* Company, careers, partner, conversion and utility pages (c_company.py, c_convert.py). */
(function(){
var d=document,W=window,rm=matchMedia('(prefers-reduced-motion:reduce)').matches,ROOT=d.body.dataset.root||'';
function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function mailto(to,subj,lines){location.href='mailto:'+to+'?subject='+encodeURIComponent(subj)+'&body='+encodeURIComponent(lines.join('\n'))}
function bad(scope){return $$('[required]',scope).filter(function(x){return x.type==='checkbox'?!x.checked:!x.value.trim()||(x.type==='email'&&!/^\S+@\S+\.\S+$/.test(x.value))})}
function fields(f){var L=[];$$('input,select,textarea',f).forEach(function(x){if(!x.name||x.type==='file'||(x.type==='checkbox'&&x.name!=='line'&&x.name!=='consent'))return;if(x.type==='checkbox'&&!x.checked)return;var l=x.closest('label'),t=l&&$('span',l)?$('span',l).textContent:x.name;L.push(t+': '+x.value)});return L}
/* wall-clock time in time zone tz -> real instant */
function zoned(y,m,dd,h,mi,tz){var g=Date.UTC(y,m,dd,h,mi),p=new Date(new Date(g).toLocaleString('en-US',{timeZone:tz})),u=new Date(new Date(g).toLocaleString('en-US',{timeZone:'UTC'}));return new Date(g-(p-u))}
function dl(name,type,text){var a=d.createElement('a');a.href=URL.createObjectURL(new Blob([text],{type:type}));a.download=name;d.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500)}

/* generic stepper: steps (fieldsets), dots, back/next/submit buttons */
function stepper(f,stepSel,dotSel,b,n,g,onShow){var S=$$(stepSel,f),D=$$(dotSel,f),k=0,er=$('.co-err',f);
 function show(){S.forEach(function(s,i){s.classList.toggle('on',i===k)});D.forEach(function(x,i){x.classList.toggle('on',i<=k)});b.hidden=!k;n.hidden=k===S.length-1;if(g)g.hidden=k!==S.length-1;if(onShow)onShow(k,S.length)}
 n.addEventListener('click',function(){var x=bad(S[k]);if(x.length){er.textContent='Please complete the highlighted fields.';x[0].focus();return}er.textContent='';k++;show()});
 b.addEventListener('click',function(){k--;er.textContent='';show()});show();return {valid:function(){var x=bad(f);if(x.length){er.textContent='Please complete the highlighted fields.';x[0].focus();return false}return true},k:function(){return k},show:show,set:function(v){k=v;show()}}}

/* careers: apply flow */
$$('.co-apply').forEach(function(f){var st=stepper(f,'.co-as','.co-dots li',$('[data-ab]',f),$('[data-an]',f),$('[data-ag]',f));
 f.addEventListener('submit',function(e){e.preventDefault();if(!st.valid())return;mailto(f.dataset.mail,'Application: '+$('[name=role]',f).value,fields(f));$$('fieldset,.co-an,.co-dots',f).forEach(function(x){x.hidden=true});var ok=$('.co-ok',f);ok.hidden=false;ok.focus()})});

/* partner: horizontal sliding steps */
$$('.co-pf').forEach(function(f){var t=$('.co-pt',f),bar=$('.co-pbar i',f);var st=stepper(f,'.co-ps','.co-none',$('[data-pb]',f),$('[data-pn]',f),$('[data-pg]',f),function(k,n){t.style.transform='translateX('+(-k*100)+'%)';bar.style.width=((k+1)/n*100)+'%'});
 f.addEventListener('submit',function(e){e.preventDefault();if(!st.valid())return;mailto(f.dataset.mail,'Confidential: lab partnership enquiry',fields(f));$$('.co-pv,.co-an,.co-pbar',f).forEach(function(x){x.hidden=true});var ok=$('.co-ok',f);ok.hidden=false;ok.focus()})});
$$('.co-quotes').forEach(function(q){var Q=$$('.co-q',q),i=0;if(rm||Q.length<2)return;setInterval(function(){Q[i].classList.remove('on');i=(i+1)%Q.length;Q[i].classList.add('on')},7000)});

/* careers: ladder region switch, role filters */
$$('.co-lad').forEach(function(l){$$('[data-lr]',l).forEach(function(b){b.addEventListener('click',function(){$$('[data-lr]',l).forEach(function(x){x.setAttribute('aria-pressed',x===b)});$$('.co-pay',l).forEach(function(p){p.textContent=JSON.parse(p.dataset.p)[+b.dataset.lr]})})})});
$$('.co-rf').forEach(function(f){var R=$$('.co-role'),c=$('.co-rc',f),nr=$('.co-rn');function up(){var v={loc:$('[data-rf=loc]',f).value,fn:$('[data-rf=fn]',f).value,lv:$('[data-rf=lv]',f).value},n=0;
 R.forEach(function(r){var ok=(!v.loc||r.dataset.loc===v.loc)&&(!v.fn||r.dataset.fn===v.fn)&&(!v.lv||r.dataset.lv===v.lv);r.hidden=!ok;if(ok)n++});c.textContent=n+' of '+R.length+' roles';if(nr)nr.hidden=!!n}
 $$('select',f).forEach(function(s){s.addEventListener('change',up)});up()});

/* book a call: slots for the next 10 business days in the scientist's time zone */
$$('.co-book').forEach(function(b){var G=$('.co-grid',b),tl=$('.co-tzl',b),f=$('.co-pre',b),sel=null,cur=$('.co-sp[aria-pressed=true]',b);
 function hash(s){var h=7;for(var i=0;i<s.length;i++)h=(h*31+s.charCodeAt(i))%9973;return h}
 function render(){var tz=cur.dataset.tz,days=[],t=new Date();while(days.length<10){t=new Date(t.getTime()+864e5);var w=t.getDay();if(w&&w<6)days.push(new Date(t))}
  tl.textContent='Times shown in your time zone. '+cur.dataset.n+' works in '+cur.dataset.tzn+'; slots are 09:00 to 17:00 there.';G.innerHTML='';sel=null;$('.co-sel',f).textContent='No time selected yet.';
  days.forEach(function(day){var col=d.createElement('div');col.className='co-day';col.setAttribute('role','row');col.innerHTML='<b>'+day.toLocaleDateString(undefined,{weekday:'short',day:'numeric',month:'short'})+'</b>';
   for(var h=9;h<17;h+=1.5){var real=zoned(day.getFullYear(),day.getMonth(),day.getDate(),Math.floor(h),h%1?30:0,tz);
    if(hash(cur.dataset.n+day.toDateString()+h)%3===0)continue;var s=d.createElement('button');s.type='button';s.className='co-slot';s.setAttribute('role','gridcell');s.dataset.t=real.toISOString();s.textContent=real.toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'});
    s.addEventListener('click',function(){$$('.co-slot',G).forEach(function(x){x.setAttribute('aria-pressed','false')});this.setAttribute('aria-pressed','true');sel=new Date(this.dataset.t);$('.co-sel',f).textContent='Selected: '+sel.toLocaleString([],{weekday:'long',day:'numeric',month:'long',hour:'2-digit',minute:'2-digit'})+' (your time)'});col.appendChild(s)}
   G.appendChild(col)})}
 $$('.co-sp',b).forEach(function(x){x.addEventListener('click',function(){$$('.co-sp',b).forEach(function(y){y.setAttribute('aria-pressed',y===x)});cur=x;render()})});render();
 f.addEventListener('submit',function(e){e.preventDefault();var er=$('.co-err',f),x=bad(f);if(x.length){er.textContent='Please complete the highlighted fields.';x[0].focus();return}if(!sel){er.textContent='Pick a time slot first.';return}er.textContent='';
  mailto(b.dataset.mail,'Scientist call request: '+cur.dataset.spec,['Specialty: '+cur.dataset.spec,'Scientist: '+cur.dataset.n,'Requested time (UTC): '+sel.toISOString()].concat(fields(f)));
  function ic(t){return t.toISOString().replace(/[-:]/g,'').replace(/\.\d+/,'')}var en=new Date(sel.getTime()+18e5);
  $('.co-ics',f).href=URL.createObjectURL(new Blob(['BEGIN:VCALENDAR\r\nVERSION:2.0\r\nPRODID:-//PharmaCRO//Call//EN\r\nBEGIN:VEVENT\r\nUID:'+ic(sel)+'@pharma.eliteleadgrow.com\r\nDTSTAMP:'+ic(new Date())+'\r\nDTSTART:'+ic(sel)+'\r\nDTEND:'+ic(en)+'\r\nSUMMARY:PharmaCRO scientist call ('+cur.dataset.spec+')\r\nDESCRIPTION:Requested time. The scientist confirms by email.\r\nEND:VEVENT\r\nEND:VCALENDAR\r\n'],{type:'text/calendar'}));
  var ok=$('.co-ok',f);ok.hidden=false;ok.focus()})});

/* submit samples wizard */
$$('.co-wz').forEach(function(w){var P=$('[data-wp]',w),M=$('[data-wm]',w),id='';
 function code(s){var h=0,c='',n=21;for(var i=0;i<s.length;i++)h=(h*131+s.charCodeAt(i))>>>0;for(var y=0;y<n;y++)for(var x=0;x<n;x++){var fin=(x<7&&y<7)||(x>=n-7&&y<7)||(x<7&&y>=n-7),on;
  if(fin){var a=x%14<7?x:x-(n-7),b=y<7?y:y-(n-7);on=(a===0||a===6||b===0||b===6)||(a>1&&a<5&&b>1&&b<5)}else{h=(h*1103515245+12345)>>>0;on=(h>>>16)&1}if(on)c+='<rect x="'+x+'" y="'+y+'" width="1" height="1"/>'}return '<svg viewBox="-1 -1 23 23" aria-hidden="true">'+c+'</svg>'}
 function v(n){var e=$('[name='+n+']',w);return e?e.value:''}
 var st=stepper(w,'.co-ws','.co-dots li',$('[data-wb]',w),$('[data-wn]',w),null,function(k,n){var last=k===n-1;P.hidden=M.hidden=!last;if(!last)return;
  var t=new Date();id='PC-'+String(t.getFullYear()).slice(2)+'-'+(1000+Math.floor(Math.random()*9000));var N=Math.max(1,Math.min(12,+v('n')||1)),lines=$$('[name=line]:checked',w).map(function(x){return x.value});
  var labels='';for(var i=1;i<=N;i++){var sid=id+'-'+('0'+i).slice(-2);labels+='<div class="co-lab">'+code(sid)+'<div><b>'+esc(sid)+'</b><span>'+esc(v('product'))+' &middot; '+esc(v('batch'))+'</span><span>'+esc(v('storage'))+'</span></div></div>'}
  $('.co-out',w).innerHTML='<p>Your sample ID is <b class="mono-v">'+esc(id)+'</b>. Write it on the box and keep it for tracking.</p><div class="co-pl"><h4>Packing list</h4><table><tr><th>Sample ID</th><th>Product</th><th>Batch</th><th>Storage</th><th>Hazard</th></tr>'+
   Array.apply(null,Array(N)).map(function(_,i){return '<tr><td>'+esc(id+'-'+('0'+(i+1)).slice(-2))+'</td><td>'+esc(v('product'))+'</td><td>'+esc(v('batch'))+'</td><td>'+esc(v('storage'))+'</td><td>'+esc(v('hazard'))+'</td></tr>'}).join('')+'</table><p>Tests: '+esc(lines.join('; ')||'as per quote '+v('quote'))+'</p></div><div class="co-labs">'+labels+'</div>'});
 P.addEventListener('click',function(){W.print()});
 M.addEventListener('click',function(){mailto(w.dataset.mail,'Sample submission '+id,['Sample ID: '+id].concat(fields(w)).concat(['','(Attach your CoA or protocol if you selected one.)']))})});
$$('[data-csv]').forEach(function(b){b.addEventListener('click',function(){dl('pharmacro-sample-submission-sheet.csv','text/csv','Sample ID,Product,Batch or lot,Container count,Storage condition,Tests requested,Hazard class,Notes\r\nPC-YY-NNNN-01,,,,Refrigerated (2 to 8 C),,Not hazardous,\r\n')})});

/* contact route chooser */
$$('.co-routes').forEach(function(r){var B=$$('[data-rt]',r);B.forEach(function(b){b.addEventListener('click',function(){B.forEach(function(x){var on=x===b;x.setAttribute('aria-selected',on);x.setAttribute('aria-pressed',on)});$$('.co-rp').forEach(function(p){p.hidden=p.dataset.rp!==b.dataset.rt});var i=$('.co-rp:not([hidden]) input,.co-rp:not([hidden]) textarea');if(i)i.focus()})})});

/* support: sample lookup demo, help search */
var DEMO={'PC-24-0918':['Metformin 500 mg tablets, B2291',4],'PC-24-0919':['Adalimumab DS, Lot 77A',2],'PC-24-0920':['mRNA-LNP, ENG-04',1],'PC-24-0921':['WFI loop, Room 2B',5],'PC-24-0922':['Amoxicillin API, 24-118',3]},
 STEPS=['Received','Queued','In analysis','Under review','Approved','Released'];
$$('.co-look').forEach(function(f){var o=f.parentNode.querySelector('.co-lr');f.addEventListener('submit',function(e){e.preventDefault();var v=$('input',f).value.trim().toUpperCase(),r=DEMO[v];
 if(!r){o.innerHTML=/^PC-\d{2}-\d{4}$/.test(v)?'<p>No sample with that ID in the demo. Real lookups open with the portal at launch.</p>':'<p>Sample IDs look like <b>PC-24-0918</b>: PC, the year, then four digits. You will find it on your receipt email and the box label.</p>';return}
 var t=new Date();o.innerHTML='<p><b>'+esc(v)+'</b> &middot; '+esc(r[0])+'</p><ol class="co-tl">'+STEPS.map(function(s,i){var dd=new Date(t.getTime()-(r[1]-i)*36e5*9);return '<li class="'+(i<=r[1]?'done':'')+'"><b>'+s+'</b><span>'+(i<=r[1]?dd.toLocaleString([],{day:'numeric',month:'short',hour:'2-digit',minute:'2-digit'}):'Pending')+'</span></li>'}).join('')+'</ol><p class="cn">Simulated timeline.</p>'})});
$$('.co-hs').forEach(function(i){var A=$$('.co-hl details'),nr=$('.co-hn');i.addEventListener('input',function(){var v=i.value.toLowerCase(),n=0;A.forEach(function(a){var ok=a.textContent.toLowerCase().indexOf(v)>-1;a.hidden=!ok;if(ok)n++});nr.hidden=!!n})});

/* full-page search (search page and 404) */
$$('.co-search').forEach(function(s){var i=$('input',s),o=$('.co-sres',s),IDX=null,q=new URLSearchParams(location.search).get('q');
 function score(w,e){var t=0;w.forEach(function(x){if(x.length<2)return;if(e.t.toLowerCase().indexOf(x)>-1)t+=6;if(e.d.toLowerCase().indexOf(x)>-1)t+=3;if(e.k.indexOf(x)>-1)t+=1});return t}
 function run(){if(!IDX)return;var w=i.value.toLowerCase().split(/\s+/).filter(Boolean);if(!w.length){o.innerHTML='';return}var R=IDX.map(function(e){return [score(w,e),e]}).filter(function(x){return x[0]>2}).sort(function(a,b){return b[0]-a[0]}).slice(0,40),G={};
  R.forEach(function(x){var k=x[1].s;(G[k]=G[k]||[]).push(x[1])});o.innerHTML=R.length?Object.keys(G).map(function(k){return '<p class="so-g">'+esc(k)+'</p>'+G[k].map(function(e){return '<a href="'+ROOT+e.p+'"><b>'+esc(e.t)+'</b><span>'+esc(e.d.slice(0,140))+'</span></a>'}).join('')}).join(''):'<p class="so-g">No results</p><a href="'+ROOT+'request-quote.html"><b>Ask a scientist instead</b><span>We run many methods that are not listed yet.</span></a>'}
 fetch(ROOT+'assets/search.json').then(function(r){return r.json()}).then(function(j){IDX=j;run()}).catch(function(){o.innerHTML='<p class="so-g">Search needs the site to be served over http.</p>'});
 if(q)i.value=q;i.addEventListener('input',function(){run();if(history.replaceState&&$('.p-search'))history.replaceState(null,'','?q='+encodeURIComponent(i.value))})});
})();

/* industries module: pain/answer scroll reveal, expanding tiles, matcher, cost-of-delay mini */
(function(){
var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches,root=d.body.dataset.root||'';
function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
var rows=$$('.ind-pr');
if(rows.length){var up=function(){var h=innerHeight;rows.forEach(function(r){var b=r.getBoundingClientRect(),p=rm?1:Math.min(1,Math.max(0,(h*.85-b.top)/(h*.45)));r.style.setProperty('--p',p.toFixed(3))})};
 addEventListener('scroll',function(){requestAnimationFrame(up)},{passive:true});addEventListener('resize',up);up()}
$$('.ind-tiles').forEach(function(w){var pv=$('.ind-pv',w),last=null;
 function vt(f){if(d.startViewTransition&&!rm){w.classList.add('vt');d.startViewTransition(f).finished.then(function(){w.classList.remove('vt')})}else f()}
 function close(){vt(function(){w.classList.remove('open');pv.hidden=true});if(last)last.focus()}
 function open(b){last=b;vt(function(){pv.innerHTML='';pv.appendChild($('template[data-k="'+b.dataset.k+'"]',w).content.cloneNode(true));
  $$('a,img',pv).forEach(function(a){['href','src'].forEach(function(k){var v=a.getAttribute(k);if(v&&v[0]==='/')a.setAttribute(k,root+v.slice(1))})});
  w.classList.add('open');pv.hidden=false;$('.ind-close',pv).addEventListener('click',close)});setTimeout(function(){pv.focus()},50)}
 $$('.ind-t',w).forEach(function(b){b.addEventListener('click',function(){open(b)})});
 w.addEventListener('keydown',function(e){if(e.key==='Escape'&&!pv.hidden)close()})});
var MAP={'small|mfr':'generics','small|nolab':'biotech-startups','small|cdmo':'cdmos','small|global':'big-pharma','small|api':'api-manufacturers','bio|mfr':'biosimilars','bio|nolab':'biotech-startups','bio|cdmo':'cdmos','bio|global':'big-pharma','bio|api':'biosimilars',
 'vax|mfr':'vaccine-makers','vax|nolab':'biotech-startups','vax|cdmo':'cdmos','vax|global':'vaccine-makers','vax|api':'vaccine-makers','ing|mfr':'excipient-packaging-suppliers','ing|nolab':'excipient-packaging-suppliers','ing|cdmo':'excipient-packaging-suppliers','ing|global':'excipient-packaging-suppliers','ing|api':'api-manufacturers'};
$$('.ind-match').forEach(function(m){var N=JSON.parse(m.dataset.n),a=$('[data-m=a]',m),b=$('[data-m=b]',m),o=$('.ind-m-o',m);
 function up(){if(!a.value||!b.value){o.textContent='Choose both to see your page.';return}var k=MAP[a.value+'|'+b.value];o.innerHTML='You sound like <a href="'+root+'industries/'+k+'.html">'+N[k]+' &rsaquo;</a>'}
 a.addEventListener('change',up);b.addEventListener('change',up)});
$$('.ind-cod').forEach(function(c){var v=$('[data-cod=v]',c),a=$('[data-cod=a]',c),b=$('[data-cod=b]',c),o=$('.ind-cod-o',c);
 function up(){var days=Math.max(0,(+a.value||0)-(+b.value||0)),cal=Math.round(days*7/5),val=cal*(+v.value||0);
  o.innerHTML='Cutting '+days+' business days (about '+cal+' calendar days) is worth roughly <b>$'+val.toLocaleString('en-US')+'</b> per batch or launch.'}
 [v,a,b].forEach(function(x){x.addEventListener('input',up)});up()});
})();

/* labs module: photo tour, lab card sort/filter, route draw */
(function(){var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
$$('.lb-tour').forEach(function(t){var F=$$('.lb-tf',t),b=t.querySelector('.lb-tbar i'),p=t.querySelector('.lb-tp'),k=0,el=0,paused=rm,STEP=4000;
 if(rm){p.textContent='Play tour';p.setAttribute('aria-pressed','true')}
 setInterval(function(){if(paused)return;el+=100;b.style.setProperty('--p',(((k*STEP)+el)/(F.length*STEP)*100)+'%');if(el>=STEP){el=0;F[k].classList.remove('on');k=(k+1)%F.length;F[k].classList.add('on')}},100);
 p.addEventListener('click',function(){paused=!paused;p.setAttribute('aria-pressed',paused);p.textContent=paused?'Play tour':'Pause tour'})});
var g=d.querySelector('.lb-cards');if(g){var C=$$('.lb-card',g),reg={},key='ph';
 function ap(){var any=Object.keys(reg).some(function(k){return reg[k]});function go(){C.slice().sort(function(a,b){var x=a.dataset[key],y=b.dataset[key];return x>y?1:x<y?-1:0}).forEach(function(c){g.appendChild(c);c.classList.toggle('hide',any&&!reg[c.dataset.r])})}
  if(d.startViewTransition&&!rm){C.forEach(function(c,i){c.style.viewTransitionName='lbc'+i});d.startViewTransition(go)}else go()}
 $$('[data-ls]').forEach(function(b){b.addEventListener('click',function(){key=b.dataset.ls;$$('[data-ls]').forEach(function(x){x.setAttribute('aria-pressed',x===b)});ap()})});
 $$('[data-lr]').forEach(function(b){b.addEventListener('click',function(){reg[b.dataset.lr]=!reg[b.dataset.lr];b.setAttribute('aria-pressed',!!reg[b.dataset.lr]);ap()})})}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.3});$$('.lb-route').forEach(function(x){io.observe(x)})}
})();

/* Method Library search and filters (c_methods.py) */
(function(){
var x=document.querySelector('.ml-x');if(!x)return;
var D=JSON.parse(x.querySelector('.ml-json').textContent),C=[].slice.call(x.querySelectorAll('.ml-c')),q=x.querySelector('[data-mlq]'),F=[].slice.call(x.querySelectorAll('[data-mlf]')),B=[].slice.call(x.querySelectorAll('[data-mlm]')),n=x.querySelector('.ml-n'),none=x.querySelector('.ml-none'),mod='';
var byS={};D.forEach(function(d){byS[d.s]=d;d.h=(d.n+' '+d.f+' '+d.p+' '+d.st.join(' ')).toLowerCase().replace(/[<>]/g,'')});
var rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
function run(){var w=q.value.toLowerCase().replace(/[<>]/g,'').split(/\s+/).filter(Boolean),f={},k=0;F.forEach(function(s){f[s.dataset.mlf]=s.value});
 C.forEach(function(c){var d=byS[c.dataset.s],ok=w.every(function(t){return d.h.indexOf(t)>-1})&&(!f.f||d.f===f.f)&&(!f.sf||d.sf.indexOf(f.sf)>-1)&&(!mod||d.m.indexOf(mod)>-1);
  var was=!c.classList.contains('hide');c.classList.toggle('hide',!ok);if(ok){if(!was&&!rm){c.classList.remove('pop');void c.offsetWidth;c.style.setProperty('--k',k);c.classList.add('pop')}k++}});
 n.textContent=k+' of '+D.length+' methods';none.hidden=!!k}
q.addEventListener('input',run);F.forEach(function(s){s.addEventListener('change',run)});
B.forEach(function(b){b.addEventListener('click',function(){mod=mod===b.dataset.mlm?'':b.dataset.mlm;B.forEach(function(o){o.setAttribute('aria-pressed',o.dataset.mlm===mod)});run()})});
var p=new URLSearchParams(location.search).get('q');if(p)q.value=p;run();
})();

/* quality + technology module: process flow, VQP ring, certificate wall, feature tabs, login preview, API demo */
(function(){var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
if('IntersectionObserver' in window){var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.3});$$('.qx-flow').forEach(function(x){io.observe(x)})}
/* vendor pack: ring + tick once the (mail) form is valid and submitted */
$$('.qx-vqp').forEach(function(v){var f=$('form',v);if(f)f.addEventListener('submit',function(){if(f.checkValidity())v.classList.add('done')})});
/* certificate wall */
$$('.qx-cert').forEach(function(c){c.addEventListener('click',function(){c.setAttribute('aria-pressed',c.getAttribute('aria-pressed')!=='true')})});
var wl=$('[data-wl]'),ws=$('[data-ws]');if(wl&&ws){var C=$$('.qx-cert'),cn=$('.qx-wc');function up(){var n=0;C.forEach(function(c){var ok=(!wl.value||c.dataset.l===wl.value)&&(!ws.value||c.dataset.s===ws.value);c.classList.toggle('hide',!ok);if(ok)n++});cn.textContent=n+' of '+C.length}
 wl.addEventListener('change',up);ws.addEventListener('change',up);up()}
/* feature tabs */
$$('.qx-tabs').forEach(function(t){var B=$$('[role=tab]',t),P=$$('.qx-tp',t);function sel(b){B.forEach(function(x){x.setAttribute('aria-selected',x===b)});P.forEach(function(p){p.classList.toggle('on',p.dataset.i===b.dataset.i)})}
 B.forEach(function(b,i){b.addEventListener('click',function(){sel(b)});b.addEventListener('keydown',function(e){var k=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;if(k){var n=B[(i+k+B.length)%B.length];n.focus();sel(n)}})})});
/* login preview: never authenticates */
$$('.qx-lf').forEach(function(f){var a=$('.qx-l1',f),b=$('.qx-l2',f),c=$('.qx-l3',f);function done(){a.hidden=b.hidden=true;c.hidden=false;var s=$('.sig',c);if(s)setTimeout(function(){s.classList.add('in')},30);$('h3',c).setAttribute('tabindex','-1');$('h3',c).focus()}
 f.addEventListener('submit',function(e){e.preventDefault();var bad=$$('[required]',a).filter(function(x){return !x.value.trim()});if(bad.length){bad[0].focus();bad[0].setAttribute('aria-invalid','true');return}a.hidden=true;b.hidden=false;$('.qx-otp input',b).focus()});
 $('[data-sso]',f).addEventListener('click',done);$('[data-mfa]',f).addEventListener('click',done);
 var O=$$('.qx-otp input',f);O.forEach(function(o,i){o.addEventListener('input',function(){o.value=o.value.replace(/\D/g,'').slice(0,1);if(o.value&&O[i+1])O[i+1].focus()});o.addEventListener('keydown',function(e){if(e.key==='Backspace'&&!o.value&&O[i-1])O[i-1].focus()})})});
/* API demo: typed request, simulated response */
$$('.qx-api').forEach(function(a){var t=$('.qx-type',a),r=$('.qx-resp',a),s=$('.qx-state',a),btn=$('[data-send]',a),typed=false;
 function type(el,txt,cb){if(rm){el.textContent=txt;el.classList.add('done');if(cb)cb();return}var i=0;el.textContent='';(function f(){i+=2;el.textContent=txt.slice(0,i);if(i<txt.length)setTimeout(f,14);else{el.classList.add('done');if(cb)cb()}})()}
 function start(){if(typed)return;typed=true;type(t,t.dataset.code)}
 if('IntersectionObserver' in window){var o=new IntersectionObserver(function(es){if(es[0].isIntersecting){o.disconnect();start()}},{threshold:.4});o.observe(a)}else start();
 btn.addEventListener('click',function(){start();btn.disabled=true;s.className='qx-state';s.textContent='Request sent…';r.textContent='';setTimeout(function(){s.textContent='201 Created · 184 ms';s.classList.add('ok');type(r,r.dataset.code,function(){btn.disabled=false})},rm?0:900)})});
})();

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

/* services module widgets (.sv1-*) */
(function(){
var d=document,$=function(s,c){return (c||d).querySelector(s)},$$=function(s,c){return [].slice.call((c||d).querySelectorAll(s))},rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function bd(n){var t=new Date(),k=0;while(k<n){t.setDate(t.getDate()+1);if(t.getDay()%6)k++}return t.toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'})}
/* instrument slider */
$$('.sv1-sl').forEach(function(s){var I=$$('.sv1-sl-i',s),D=$$('.sv1-d button',s),k=0;function go(n){k=(n+I.length)%I.length;I.forEach(function(x,i){x.classList.toggle('on',i===k)});D.forEach(function(x,i){if(i===k)x.setAttribute('aria-current','true');else x.removeAttribute('aria-current')})}
 $('.sv1-p',s).addEventListener('click',function(){go(k-1)});$('.sv1-n',s).addEventListener('click',function(){go(k+1)});D.forEach(function(x,i){x.addEventListener('click',function(){go(i)})})});
/* availability by local office hours */
$$('.sv1-av').forEach(function(a){try{var f=new Intl.DateTimeFormat('en-GB',{timeZone:a.dataset.tz,hour:'2-digit',minute:'2-digit',weekday:'short',hour12:false}),p=f.formatToParts(new Date()),h=+p.filter(function(x){return x.type==='hour'})[0].value,w=p.filter(function(x){return x.type==='weekday'})[0].value,on=h>=9&&h<18&&w!=='Sat'&&w!=='Sun';
 a.classList.toggle('on',on);var l=$('.sv1-lt',a);l.textContent=l.textContent+' · '+f.format(new Date()).replace(/^\w+ /,'')+(on?' · online':' · back in office hours')}catch(e){}});
/* Batch Release Planner */
$$('.sv1-brp').forEach(function(b){var T=JSON.parse(b.dataset.t),F=JSON.parse(b.dataset.f),f=$('[data-b=f]',b),m=$('[data-b=m]',b),o=$('.sv1-out',b);
 function up(){var L=F[f.value],mx=0,r=L.map(function(k){var t=T[k];mx=Math.max(mx,t[2]);return '<tr><td>'+esc(t[0])+'</td><td class="mono">'+esc(t[1][m.value])+'</td><td>'+t[2]+' d</td></tr>'}).join('');
  o.innerHTML='<div class="sv1-sum"><div><b>'+L.length+'</b>release tests</div><div><b>'+(mx+2)+' days</b>estimated turnaround</div><div><b>'+bd(mx+2)+'</b>results if shipped today</div></div><table><thead><tr><th>Test</th><th>Reference</th><th>Lab time</th></tr></thead><tbody>'+r+'</tbody></table>'}
 f.addEventListener('change',up);m.addEventListener('change',up);up()});
/* Stability mini designer */
$$('.sv1-sd').forEach(function(s){var o=$('.sv1-out',s);function v(k){return $('[data-s='+k+']',s)}
 function up(){var dur=+v('dur').value,pk=+v('pk').value,u=+v('u').value,ph=v('ph').checked;$('[data-o=pk]',s).textContent=pk;$('[data-o=u]',s).textContent=u;
  var LT=[0,3,6,9,12,18,24].concat([36,48,60].filter(function(x){return x<=dur})).filter(function(x){return x<=dur}),rows=[],conds={};
  $$('.sv1-zs input:checked',s).forEach(function(c){conds[c.dataset.c]=1});var C=Object.keys(conds);if(!C.length){o.innerHTML='<p>Choose at least one long-term condition.</p>';return}
  C.forEach(function(c){rows.push(['Long-term '+c,LT])});if(conds['25 °C / 60% RH'])rows.push(['Intermediate 30 °C / 65% RH',[0,6,9,12]]);rows.push(['Accelerated 40 °C / 75% RH',[0,3,6]]);if(ph)rows.push(['Photostability (ICH Q1B)',[0]]);
  var pulls=0;rows.forEach(function(r){pulls+=r[1].length});var batches=3,units=Math.ceil(pulls*batches*pk*u*1.2),tp=pulls*batches*pk,lo=tp*450,hi=tp*800;
  o.innerHTML='<div class="sv1-sum"><div><b>'+tp+'</b>time points to test</div><div><b>'+units.toLocaleString('en-US')+'</b>units to place (incl. 20% spare)</div><div><b>USD '+lo.toLocaleString('en-US')+' to '+hi.toLocaleString('en-US')+'</b>indicative cost</div></div>'+
   '<table><thead><tr><th>Condition</th><th>Pull points (months)</th></tr></thead><tbody>'+rows.map(function(r){return '<tr><td>'+r[0]+'</td><td class="mono">'+r[1].join(', ')+'</td></tr>'}).join('')+'</tbody></table>'}
 $$('input,select',s).forEach(function(x){x.addEventListener('input',up);x.addEventListener('change',up)});up()});
/* chip groups: Validation Wizard and CGT matrix */
function chips(root,render){var B=$$('.sv1-chs .ch',root);B.forEach(function(b){b.addEventListener('click',function(){B.forEach(function(x){x.setAttribute('aria-pressed',x===b)});render(b.textContent)})});var on=B.filter(function(b){return b.getAttribute('aria-pressed')==='true'})[0]||B[0];render(on.textContent)}
$$('.sv1-vw').forEach(function(w){var V=JSON.parse(w.dataset.v),o=$('.sv1-out',w);chips(w,function(k){var v=V[k],wk=v[1]+2;
 o.innerHTML='<ul class="sv1-par">'+v[0].map(function(p,i){return '<li style="--i:'+i+'">'+esc(p)+'</li>'}).join('')+'</ul><div class="sv1-sum"><div><b>'+v[0].length+'</b>characteristics</div><div><b>~'+wk+' weeks</b>protocol, execution, report</div><div><b>'+bd(wk*5)+'</b>report if started today</div></div>'})});
$$('.sv1-cg').forEach(function(c){var C=JSON.parse(c.dataset.c),o=$('.sv1-out',c);chips(c,function(k){o.innerHTML='<table><thead><tr><th>Release test</th><th>Method</th><th>Time to result</th></tr></thead><tbody>'+C[k].map(function(r){return '<tr><td>'+esc(r[0])+'</td><td>'+esc(r[1])+'</td><td class="mono">'+esc(r[2])+'</td></tr>'}).join('')+'</tbody></table>'})});
/* Biosimilar similarity explorer */
$$('.sv1-bs').forEach(function(b){var R=$$('.sv1-bsr',b),st=$('.sv1-bss',b);function up(){var out=0;R.forEach(function(r){var a=+r.dataset.a,z=+r.dataset.b,lo=+r.dataset.lo,hi=+r.dataset.hi,i=$('input',r),v=+i.value,sp=z-a,bar=$('.sv1-bsb',r);
  bar.style.setProperty('--l',((lo-a)/sp*100)+'%');bar.style.setProperty('--w',((hi-lo)/sp*100)+'%');bar.style.setProperty('--m','calc('+((v-a)/sp*100)+'% - 2px)');var o=v<lo||v>hi;r.classList.toggle('out',o);if(o)out++;$('output',r).textContent=v.toFixed(1)+'%'});
  st.textContent=out?out+' of '+R.length+' attributes fall outside the reference range. Each needs a scientific justification or process work.':'All '+R.length+' attributes sit inside the reference quality ranges.'}
 R.forEach(function(r){$('input',r).addEventListener('input',up)});up()});
/* mRNA quality attribute map */
$$('.sv1-qa').forEach(function(q){var Q=JSON.parse(q.dataset.q),p=$('.sv1-qa-p',q),K=$$('.sv1-qk',q);function show(g){var a=Q[g.dataset.k];K.forEach(function(x){x.classList.toggle('on',x.dataset.k===g.dataset.k)});
 p.innerHTML='<p class="ey">'+esc(a[0])+'</p><h3>'+esc(a[1])+'</h3><p><b>Method:</b> '+esc(a[2])+'</p><p>'+esc(a[3])+'</p>'+(a[4]?'<p><a href="'+(d.body.dataset.root||'')+a[4].slice(1)+'">Method Library entry &rsaquo;</a></p>':'')}
 K.forEach(function(g){g.addEventListener('click',function(){show(g)});g.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();show(g)}})})});
})();

/* services 7-12 tools (c_services2.py) */
(function(){
var d=document,rm=matchMedia('(prefers-reduced-motion:reduce)').matches;
function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
function num(x){return parseFloat(x.value)}
function f(n){return n>=100?Math.round(n).toLocaleString('en-US'):n>=1?(+n.toFixed(2)).toString():(+n.toPrecision(3)).toString()}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}

/* petri colony counter */
$$('[data-sv2-count]').forEach(function(t){var n=+t.dataset.sv2Count;if(rm){t.textContent=n;return}var k=0;setInterval(function(){k=k>=n?0:k+1;t.textContent=k},9000/(n*2.2))});

/* instrument slider buttons */
$$('.sv2-ins').forEach(function(w){var t=$('.sv2-trk',w);$('.sv2-prev',w).addEventListener('click',function(){t.scrollBy({left:-400,behavior:rm?'auto':'smooth'})});$('.sv2-next',w).addEventListener('click',function(){t.scrollBy({left:400,behavior:rm?'auto':'smooth'})})});

/* endotoxin limit: limit = K/M, M = dose/kg/h; MVD = limit*conc/lambda */
$$('[data-sv2=endo]').forEach(function(w){var g=function(k){return $('[data-e='+k+']',w)};
 function up(){var dose=num(g('dose')),hrs=num(g('hrs'))||1,kg=num(g('kg'))||70,K=parseFloat(g('route').value),u=g('unit').value,c=num(g('conc')),lam=parseFloat(g('lam').value);
  if(g('route').selectedIndex===2)K=175/kg; // radiopharmaceuticals: 175 EU per dose (V = max dose)
  if(!(dose>0)){g('lim').textContent='Enter a dose';return}
  var M=dose/kg/hrs,lim=K/M;g('lim').textContent=f(lim)+' EU/'+u;
  var mvd=c>0?lim*c/lam:0;g('mvd').textContent=c>0?'Maximum valid dilution: 1 in '+f(mvd)+' (λ = '+lam+' EU/mL)':'Add concentration to calculate the MVD';
  g('rec').textContent=mvd&&mvd<10?'Low MVD: interference is likely to be hard to dilute out. Use the most sensitive kinetic chromogenic LAL or rFC method and run interference screening early.':'Recommended: kinetic chromogenic LAL (USP <85>) or recombinant factor C (USP <86>, Ph. Eur. 2.6.32), with positive product controls at a dilution within the MVD.'}
 $$('input,select',w).forEach(function(x){x.addEventListener('input',up)});up()});

/* EM programme builder: Annex 1 (2022) limits, ISO 14644-1:2015 Table A.1 locations */
var LOC=[[2,1],[4,2],[6,3],[8,4],[10,5],[24,6],[28,7],[32,8],[36,9],[52,10],[56,11],[64,12],[68,13],[72,14],[76,15],[104,16],[108,17],[116,18],[148,19],[156,20],[192,21],[232,22],[276,23],[352,24],[436,25],[636,26],[1000,27]];
function locs(a){for(var i=0;i<LOC.length;i++)if(a<=LOC[i][0])return LOC[i][1];return Math.ceil(27*a/1000)}
var G={A:{p:['3,520','3,520'],p5:['not specified','not specified'],air:'No growth',settle:'No growth',contact:'No growth',glove:'No growth',f:'Continuous particles; viable for the full duration of critical processing'},
 B:{p:['3,520','352,000'],p5:['not specified','2,930'],air:'10 CFU/m³',settle:'5 CFU/4 h',contact:'5 CFU/plate',glove:'5 CFU/glove',f:'Particles continuously or at similar frequency; viable each shift'},
 C:{p:['352,000','3,520,000'],p5:['2,930','29,300'],air:'100 CFU/m³',settle:'50 CFU/4 h',contact:'25 CFU/plate',glove:'n/a',f:'Suggested: weekly viable and particles, per CCS risk'},
 D:{p:['3,520,000','not predetermined'],p5:['29,300','not predetermined'],air:'200 CFU/m³',settle:'100 CFU/4 h',contact:'50 CFU/plate',glove:'n/a',f:'Suggested: monthly, per CCS risk'}};
$$('[data-sv2=em]').forEach(function(w){var o=$('.sv2-emo',w);
 function up(){var a=Math.max(1,num($('[data-m=area]',w))||1),op=$('[data-m=op]',w).value==='op'?1:0,L=locs(a),rows='',tot=0;
  ['A','B','C','D'].forEach(function(g){var n=Math.max(0,Math.round(num($('[data-g='+g+']',w))||0));if(!n)return;var x=G[g];tot+=n*L;
   rows+='<tr><td><b>Grade '+g+'</b><br>'+n+' room'+(n>1?'s':'')+'</td><td>'+n*L+' ('+L+' per room)</td><td>≥0.5 µm: <b>'+x.p[op]+'</b>/m³<br>≥5 µm: <b>'+x.p5[op]+'</b></td><td>Air '+x.air+'<br>Settle '+x.settle+'<br>Contact '+x.contact+'<br>Glove '+x.glove+'</td><td>'+x.f+'</td></tr>'});
  o.innerHTML=rows?'<div class="tw"><table><thead><tr><th>Grade</th><th>Particle locations (ISO 14644-1)</th><th>Particle limits ('+(op?'in operation':'at rest')+')</th><th>Viable action limits</th><th>Monitoring frequency</th></tr></thead><tbody>'+rows+'</tbody></table></div><p class="cn">'+tot+' classification locations in total for '+a+' m² rooms. <a href="'+(d.body.dataset.root||'')+'request-quote.html?service=7">Send this plan to a scientist</a>.</p>':'<p class="cn">Add at least one room.</p>'}
 $$('input,select',w).forEach(function(x){x.addEventListener('input',up)});up()});

/* E&L risk screener: FDA 1999 route concern x interaction likelihood; PQRI SCT */
$$('[data-sv2=el]').forEach(function(w){var g=function(k){return $('[data-l='+k+']',w)};
 function up(){var c=+g('c').value,p=+g('p').value,r=+g('r').value,v=num(g('v'))||1,inh=g('r').selectedIndex===0,
  like=Math.round((c+p)/2),sc=r*like,lvl=sc>=7?'High':sc>=4?'Medium':'Low',sct=inh?0.15:1.5,aet=sct/v;
  var b=g('risk');b.textContent=lvl+' risk';b.className=lvl==='High'?'hi':lvl==='Medium'?'md':'lo';
  g('aet').textContent='Estimated AET: '+f(aet)+' µg/mL (SCT '+sct+' µg/day ÷ '+v+' mL/day), before analytical uncertainty factor';
  var plan=lvl==='High'?['Controlled extraction study on every product-contact component (USP <1663>)','HS-GC-MS, GC-MS, LC-HRMS and ICP-MS screening to the AET','Simulation study with product or a worst-case simulant','Validated targeted leachables methods on stability at each pull (USP <1664>)','Toxicological assessment of every compound above the AET']:
   lvl==='Medium'?['Risk assessment using supplier extractables data','Confirmatory extractables study on the highest-risk components','Leachables screen at release and end of shelf life','Toxicology review of compounds above the AET']:
   ['Material compliance (USP <661.1>/<661.2>, food-contact status)','Supplier extractables data and a documented risk assessment','Targeted testing only if the assessment flags a concern'];
  g('plan').innerHTML=plan.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')}
 $$('input,select',w).forEach(function(x){x.addEventListener('input',up)});up()});

/* ADA tiered flow */
$$('[data-sv2=ada]').forEach(function(w){var g=function(k){return $('[data-a='+k+']',w)};
 function up(){var n=Math.max(1,Math.round(num(g('n'))||1)),tp=num(g('pos'))/100,fpr=+g('fpr').value/100,cf=+g('cfpr').value/100;g('poso').textContent=Math.round(tp*100)+'%';
  var neg=n*(1-tp),scr=n*tp+neg*fpr,con=n*tp+neg*cf,v={all:n,scr:scr,con:con,tit:con,nab:con};
  $$('li',w).forEach(function(li){var x=Math.round(v[li.dataset.t]);$('em',li).textContent=x.toLocaleString('en-US');$('.sv2-bar i',li).style.width=(x/n*100).toFixed(1)+'%'})}
 $$('input,select',w).forEach(function(x){x.addEventListener('input',up)});
 if('IntersectionObserver' in window&&!rm){var o=new IntersectionObserver(function(e){if(e[0].isIntersecting){o.disconnect();up()}});o.observe(w)}else up()});

/* excipient compendial checker */
$$('[data-sv2=xc]').forEach(function(w){var X=JSON.parse(w.dataset.x),q=$('[data-x=q]',w),m=$('[data-x=m]',w),o=$('.sv2-xo',w),N={us:'USP-NF',eu:'Ph. Eur.',jp:'JP'};
 function up(){var v=q.value.trim().toLowerCase(),e=X.filter(function(x){return v&&(x.n.toLowerCase().indexOf(v)>-1||x.us.toLowerCase().indexOf(v)>-1||x.eu.toLowerCase().indexOf(v)>-1)})[0];
  if(!e){o.innerHTML='<p class="cn">'+(v?'Not in this short list yet. We test against any current monograph: <a href="'+(d.body.dataset.root||'')+'request-quote.html?service=10">ask us</a>.':'Choose an excipient to see the monograph names and key tests.')+'</p>';return}
  var ks=m.value==='all'?['us','eu','jp']:[m.value];
  o.innerHTML='<div class="tw"><table><thead><tr><th>Pharmacopoeia</th><th>Monograph title</th></tr></thead><tbody>'+ks.map(function(k){return '<tr><td>'+N[k]+'</td><td><b>'+esc(e[k])+'</b></td></tr>'}).join('')+'</tbody></table></div><p><b>Key tests:</b> '+esc(e.t)+'.</p>'}
 q.addEventListener('input',up);m.addEventListener('change',up);up()});

/* inspection readiness mini score */
$$('[data-sv2=irs]').forEach(function(w){var Q=$$('.sv2-qs li',w),s=$('[data-i=s]',w),t=$('[data-i=t]',w);
 w.addEventListener('change',function(){var a=Q.map(function(li){var c=$('input:checked',li);return c?+c.value:null});var done=a.filter(function(x){return x!==null});
  if(done.length<Q.length){s.textContent=done.length+' of '+Q.length+' answered';t.textContent='';return}
  var p=Math.round(done.reduce(function(x,y){return x+y},0)/(Q.length*2)*100),no=a.map(function(x,i){return x===0?i:-1}).filter(function(i){return i>-1});
  s.textContent=p+'%';t.textContent=p>=85?'Strong foundations. A mock inspection would test whether practice matches procedure.':p>=60?'Some gaps an inspector would likely find. Fix the "No" answers first'+(no.length?' (questions '+no.map(function(i){return i+1}).join(', ')+')':'')+'.':'Significant risk. Start with access control and audit trail review, then book a gap assessment.'})});
})();

/* PharmaCRO tools (c_tools.py). Everything client-side; nothing is sent unless the user presses "Send this to a scientist". */
(function(){
var d=document,W=window,ROOT=(d.body&&d.body.dataset.root)||'',rm=W.matchMedia&&matchMedia('(prefers-reduced-motion:reduce)').matches;
/*calc-start*/
var C={
 bdays:function(t,n){var r=new Date(t.getTime()),k=0;while(k<n){r.setDate(r.getDate()+1);var w=r.getDay();if(w&&w<6)k++}return r},
 km:function(a,b,c,e){var R=Math.PI/180,x=Math.sin((c-a)*R/2),y=Math.sin((e-b)*R/2);return 12742*Math.asin(Math.sqrt(x*x+Math.cos(a*R)*Math.cos(c*R)*y*y))},
 quote:function(cat,qty,tier){var M={std:1,pri:1.5,crit:2.25}[tier],F={std:1,pri:.55,crit:.3}[tier],lo=0,hi=0,t=0,n=0;
  qty.forEach(function(q,i){if(!(q>0))return;var disc=q>=10?.9:1;lo+=cat[i][1]*q*disc;hi+=cat[i][2]*q*disc;t=Math.max(t,cat[i][3]);n+=q});
  return {lo:Math.round(lo*M),hi:Math.round(hi*M),tat:n?Math.max(1,Math.round(t*F)):0,n:n}},
 tat:function(ship,base,transit,hold){var rec=C.bdays(ship,transit+(hold?2:0));return [['Standard',1],['Priority',.55],['Critical',.3]].map(function(x){var n=Math.max(1,Math.round(base*x[1]));return {tier:x[0],days:n,date:C.bdays(rec,n)}})},
 stab:function(o){var LT={II:'25 °C ± 2 °C / 60% RH ± 5%',III:'30 °C ± 2 °C / 35% RH ± 5%',IVa:'30 °C ± 2 °C / 65% RH ± 5%',IVb:'30 °C ± 2 °C / 75% RH ± 5%'},rows=[],notes=[];
  var lt=[0,3,6,9,12,18,24,36,48,60].filter(function(m){return m<=o.dur});
  if(o.store==='rt'){rows.push({c:'Long-term '+LT[o.zone],p:lt});
   if(o.inter&&o.zone==='II')rows.push({c:'Intermediate 30 °C ± 2 °C / 65% RH ± 5% (contingency)',p:[0,6,9,12]});
   rows.push({c:'Accelerated 40 °C ± 2 °C / 75% RH ± 5%',p:[0,3,6]});
   if(o.inter&&o.zone!=='II')notes.push('Long-term at 30 °C already covers the intermediate condition for Zone '+o.zone+'.')}
  else if(o.store==='fridge'){rows.push({c:'Long-term 5 °C ± 3 °C',p:lt});rows.push({c:'Accelerated 25 °C ± 2 °C / 60% RH ± 5%',p:[0,3,6]});notes.push('For hot-climate markets, consider 30 °C / 65% RH as accelerated for refrigerated products (WHO TRS 1010).')}
  else{rows.push({c:'Long-term −20 °C ± 5 °C',p:lt});notes.push('No accelerated condition for frozen products; test one batch at 5 °C ± 3 °C or 25 °C to cover excursions (ICH Q1A(R2) 2.2.7.4).')}
  if(o.pack==='semi')notes.push('Semi-permeable pack: monitor weight loss. For aqueous products ICH allows 25 °C / 40% RH (Zone II) or 30 °C / 35% RH long-term with a 5% water-loss criterion.');
  var pulls=0,cm=0;rows.forEach(function(r,i){r.n=r.p.filter(function(m){return i===0||m>0}).length;pulls+=r.n;cm+=Math.max.apply(null,r.p)*o.bat});
  var samples=pulls*o.bat*o.units;if(o.photo){rows.push({c:'Photostability ICH Q1B Option 2 (≥1.2 million lux h, ≥200 W h/m² UVA), 1 batch, exposed + dark control',p:[],n:1});samples+=2*o.units}
  return {rows:rows,pulls:pulls,samples:samples,cm:cm,lo:pulls*o.bat*900+cm*25+(o.photo?2500:0),hi:pulls*o.bat*1600+cm*45+(o.photo?4500:0),notes:notes}},
 nitro:function(a){var w={amine:3,ndsri:4,nitrite:4,solv:3,recov:2,water:1,excn:2,ph:2,lid:2,heat:1},s=0,mx=0;Object.keys(w).forEach(function(k){s+=w[k]*(a[k]||0);mx+=w[k]});
  var src=(a.nitrite||0)>0||a.solv===1||a.excn===1||a.lid===1||a.water===1,lvl=(a.ndsri===1||(a.amine===1&&src)||s>=10)?'High':s>=4?'Moderate':'Low';return {score:s,max:mx,level:lvl}},
 nlimit:function(ai,mdd){var l=ai/mdd;return {ppm:l,loq:l*.3}},
 endo:function(o){var lim,M=null,unit;if(o.k==='r175'||o.k==='r14'){lim=(o.k==='r175'?175:14)/o.dose;unit='mL';return {lim:lim,unit:'EU/mL',M:null,mvd:lim/o.lam}}
  var K=parseFloat(o.k);M=o.basis==='kg'?o.dose:o.dose/o.wt;lim=K/M;unit=o.unit;return {lim:lim,unit:'EU/'+unit,M:M,mvd:unit==='mL'?lim/o.lam:lim*o.conc/o.lam}},
 irs:function(ans){var A={},t=0;ans.forEach(function(x){A[x.a]=A[x.a]||[0,0];A[x.a][0]+=x.v;A[x.a][1]+=2;t+=x.v});var o={};Object.keys(A).forEach(function(k){o[k]=Math.round(A[k][0]/A[k][1]*100)});return {total:Math.round(t/(2*ans.length)*100),areas:o}},
 cod:function(o){var daily=o.val+o.inv*o.rate/100/365,gap=Math.max(0,o.typ-o.ours);return {daily:daily,typCost:daily*o.typ*o.n,ourCost:daily*o.ours*o.n,saving:gap*daily*o.n,perBatch:gap*daily}},
 finder:function(cfg,mod,stg,mk,q){var byk={};cfg.svc.forEach(function(s){byk[s.k]=s});var cand=(cfg.q[q]||[]).map(function(k){return byk[k]}),f=cand.filter(function(s){return mod==='unsure'||s.mod.indexOf(mod)>-1});if(!f.length)f=cand;
  f.sort(function(a,b){return (b.stg.indexOf(stg)>-1)-(a.stg.indexOf(stg)>-1)});var R={in:'India',eu:'Europe',us:'United States',apac:'Southeast Asia'}[mk];
  return f.map(function(s){var L=cfg.labs.filter(function(l){return l.sp.indexOf(s.k)>-1}).sort(function(a,b){return (b.r===R)-(a.r===R)}).slice(0,2);return {s:s,labs:L,stageFit:s.stg.indexOf(stg)>-1}})}
};
/*calc-end*/
if(!d.body)return;
function $(s,c){return (c||d).querySelector(s)}function $$(s,c){return [].slice.call((c||d).querySelectorAll(s))}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function cfg(el){return JSON.parse(el.dataset.cfg||'null')}
function fd(t){return t.toLocaleDateString('en-GB',{weekday:'short',day:'numeric',month:'short',year:'numeric'})}
function usd(n){return '$'+Math.round(n).toLocaleString('en-US')}
function num(f,n){var v=parseFloat((f.elements[n]||{}).value);return isNaN(v)?0:v}
function val(f,n){var e=f.elements[n];if(!e)return '';if(e.length&&!e.tagName){for(var i=0;i<e.length;i++)if(e[i].checked)return e[i].value;return ''}return e.value}
function send(t,q){$$('.tk-send',t.closest('.tk-wrap')||t).forEach(function(a){a.href=ROOT+'request-quote.html?q='+encodeURIComponent(q.slice(0,1500))})}
function live(f,fn){f.addEventListener('input',fn);f.addEventListener('change',fn);fn()}
function dl(name,text,type){var b=new Blob([text],{type:type||'text/plain'}),a=d.createElement('a');a.href=URL.createObjectURL(b);a.download=name;d.body.appendChild(a);a.click();setTimeout(function(){URL.revokeObjectURL(a.href);a.remove()},500)}
function bars(rows){return rows.map(function(r){return '<div class="tk-bar"><span>'+esc(r[0])+'</span><i><u style="width:'+Math.max(1,Math.min(100,r[1])).toFixed(1)+'%;background:'+(r[3]||'var(--teal)')+'"></u></i><b>'+esc(r[2])+'</b></div>'}).join('')}

/* Test Finder */
$$('[data-tk=finder]').forEach(function(t){var c=cfg(t),S=$$('.tk-step',t),P=$$('.tk-prog li',t),k=0,b=$('.tk-b',t),n=$('.tk-n',t),o=$('.tk-out',t);
 function v(name){var e=$('input[name='+name+']:checked',t);return e?e.value:''}
 function lab(name){var e=$('input[name='+name+']:checked',t);return e?e.nextElementSibling.textContent:''}
 function show(){S.forEach(function(s,i){s.classList.toggle('on',i===k)});P.forEach(function(p,i){p.classList.toggle('on',i<=k)});b.hidden=!k;n.textContent=k===3?'Show my tests':'Next'}
 n.addEventListener('click',function(){var need=['mod','stg','mk','q'][k];if(!v(need)){var f=$('input',S[k]);f.focus();return}if(k<3){k++;show();var i=$('input',S[k]);if(i)i.focus();return}
  var R=C.finder(c,v('mod'),v('stg'),v('mk'),v('q')),sum='Test Finder: '+lab('mod')+'; '+lab('stg')+'; '+lab('mk')+'; '+lab('q')+'. Suggested: '+R.map(function(r){return r.s.n}).join(', ');
  o.innerHTML='<h3>Recommended for '+esc(lab('mod').toLowerCase())+', '+esc(lab('q').toLowerCase())+'</h3>'+R.map(function(r){return '<div class="tk-rec"><div><a href="'+ROOT+r.s.u.slice(1)+'"><b>'+esc(r.s.n)+'</b></a><ul>'+r.s.tests.map(function(x){return '<li>'+esc(x)+'</li>'}).join('')+'</ul>'+
   (r.stageFit?'':'<p class="cn">Less common at this stage; a scientist will confirm whether you need it.</p>')+'</div><div class="tk-rl2"><small>Typical TAT</small><b>'+esc(r.s.tat)+'</b><small>Labs (planned)</small>'+r.labs.map(function(l){return '<a href="'+ROOT+'labs/'+l.s+'.html">'+esc(l.c)+', '+esc(l.co)+'</a>'}).join('')+
   '<a class="btn sm" href="'+ROOT+'request-quote.html?service='+r.s.i+'&q='+encodeURIComponent(sum)+'">Quote</a></div></div>'}).join('')+'<p><a class="btn tk-send" href="#">Send this to a scientist</a> <button type="button" class="btn o tk-again">Start again</button></p>';
  send(t,sum);o.hidden=false;o.focus&&o.setAttribute('tabindex','-1');o.focus();$('.tk-again',o).addEventListener('click',function(){k=0;o.hidden=true;show();$('input',S[0]).focus()})});
 b.addEventListener('click',function(){k--;show()});show()});

/* Quote estimator */
$$('[data-tk=quote]').forEach(function(t){var cat=cfg(t),Q=$$('.tk-qty',t);function up(){var tier=($('input[name=qtier]:checked',t)||{}).value||'std',q=Q.map(function(x){return Math.max(0,parseInt(x.value,10)||0)}),r=C.quote(cat,q,tier);
  $('.tk-qp',t).textContent=r.n?usd(r.lo)+' to '+usd(r.hi):'Add tests';$('.tk-qt',t).textContent=r.n?r.n+' samples · results in about '+r.tat+' business days':'';
  var L=q.map(function(n,i){return n>0?n+' × '+cat[i][0]:null}).filter(Boolean);$('.tk-ql',t).innerHTML=L.map(function(x){return '<li>'+esc(x)+'</li>'}).join('');
  send(t,'Quote estimate ('+tier+'): '+L.join('; ')+'. Band '+usd(r.lo)+' to '+usd(r.hi)+'.')}live(t,up)});

/* Turnaround calculator */
$$('[data-tk=tat]').forEach(function(t){var S=cfg(t),f=$('form',t);f.elements.d.valueAsDate=new Date();function up(){var sd=f.elements.d.value?new Date(f.elements.d.value+'T12:00'):new Date(),s=S[+f.elements.s.value],R=C.tat(sd,s.b,+f.elements.tr.value,f.elements.hold.checked);
  $('.tk-tb',t).innerHTML=R.map(function(r){return '<tr><td>'+r.tier+'</td><td>'+r.days+'</td><td><b>'+fd(r.date)+'</b></td></tr>'}).join('');
  $('.tk-note',t).textContent='Samples received and accepted by '+fd(C.bdays(sd,+f.elements.tr.value+(f.elements.hold.checked?2:0)))+'. Weekends skipped; public holidays at origin and destination are not included.';
  send(t,'Turnaround check: '+s.n+', shipping '+fd(sd)+'. Standard result '+fd(R[0].date)+', Critical '+fd(R[2].date)+'.')}live(f,up)});

/* Stability designer */
$$('[data-tk=stab]').forEach(function(t){var f=$('form',t),last=null;function o(){return {zone:val(f,'zone'),store:val(f,'store'),pack:val(f,'pack'),dur:+val(f,'dur'),bat:Math.max(1,Math.round(num(f,'bat'))),units:Math.max(1,Math.round(num(f,'units'))),inter:f.elements.inter.checked,photo:f.elements.photo.checked}}
 function up(){var p=o(),r=C.stab(p);last=[p,r];$('.tk-sn',t).textContent=r.samples.toLocaleString('en-US')+' units';$('.tk-ss',t).textContent=r.pulls+' pulls per batch × '+p.bat+' batches · '+r.cm+' chamber-months';
  $('.tk-sc',t).textContent='Indicative cost '+usd(r.lo)+' to '+usd(r.hi);$('.tk-stb',t).innerHTML=r.rows.map(function(x){return '<tr><td>'+esc(x.c)+'</td><td>'+(x.p.length?x.p.join(', '):'once')+'</td><td>'+x.n+'</td></tr>'}).join('');
  $('.tk-snote',t).innerHTML=r.notes.map(esc).join('<br>');send(t,'Stability study: zone '+p.zone+', '+p.store+', '+p.dur+' months, '+p.bat+' batches. '+r.samples+' units, '+r.pulls+' pulls per batch.')}
 live(f,up);
 $('.tk-dl',t).addEventListener('click',function(){var p=last[0],r=last[1],L=['STABILITY PROTOCOL DRAFT (generated by PharmaCRO Stability Study Designer, '+new Date().toISOString().slice(0,10)+')','Status: DRAFT for discussion. Not approved. Complete and approve under your QA system.','',
  '1. Objective: support a '+p.dur+'-month shelf life for climatic zone '+p.zone+' markets, labelled storage: '+p.store+'.','2. Batches: '+p.bat+' (ICH Q1A(R2) expects at least three primary batches for registration).','3. Container closure: '+(p.pack==='semi'?'semi-permeable':'impermeable')+', as proposed for marketing.','4. Storage conditions and pull points (months):'];
  r.rows.forEach(function(x){L.push('   - '+x.c+': '+(x.p.length?x.p.join(', '):'single exposure'))});L.push('5. Units per pull per batch per condition: '+p.units,'6. Tests at each pull: full shelf-life specification (assay, degradation products, dissolution or equivalent, water, microbial limits where applicable).','7. Total units required: '+r.samples+' (plus 10% reserve recommended).','8. Significant change criteria per ICH Q1A(R2) 2.2.7.1; evaluation per ICH Q1E.');
  r.notes.forEach(function(n){L.push('Note: '+n)});dl('stability-protocol-draft.txt',L.join('\n'))});
 $('.tk-csv',t).addEventListener('click',function(){var r=last[1],L=['condition,month,batches,units_per_batch'];r.rows.forEach(function(x){(x.p.length?x.p:['photo']).forEach(function(m){L.push('"'+x.c+'",'+m+','+last[0].bat+','+last[0].units)})});dl('stability-pull-schedule.csv',L.join('\n'),'text/csv')})});

/* Nitrosamine risk */
$$('[data-tk=nitro]').forEach(function(t){var f=$('form',t),lf=$('.tk-lim',t);var PLAN={High:['Confirmatory testing of at least 3 batches (or 10% of annual batches) with a validated LC-MS/MS or GC-MS/MS method','Method LOQ at or below 30% of the acceptable limit','Root-cause and mitigation: change of supplier, excipient grade, process step or packaging','Notify regulators per FDA, EMA or CDSCO timelines if a nitrosamine is found above the limit'],
  Moderate:['Targeted confirmatory testing on representative batches','Request nitrite data from excipient and water suppliers','Re-assess after any change of supplier, process or packaging'],Low:['Document the risk assessment and its rationale','Re-assess on change control and when new guidance is issued']};
 function up(){var a={};$$('.tk-yn',f).forEach(function(q){var e=$('input:checked',q);a[q.dataset.k]=e?parseFloat(e.value):0});var r=C.nitro(a),m=$('.tk-meter i',t);
  $('.tk-nr',t).textContent=r.level;$('.tk-nr',t).dataset.l=r.level;m.style.width=(100-Math.round(r.score/r.max*100))+'%';$('.tk-nx',t).textContent='Weighted score '+r.score+' of '+r.max+'. '+(r.level==='High'?'An amine and a nitrosating source together, or an NDSRI-prone API, need confirmatory testing.':r.level==='Moderate'?'Some risk factors present; targeted testing is sensible.':'Few risk factors; document the assessment.');
  $('.tk-np',t).innerHTML=PLAN[r.level].map(function(x){return '<li>'+esc(x)+'</li>'}).join('');var L=C.nlimit(parseFloat(val(lf,'cat')),Math.max(.001,num(lf,'mdd')));
  $('.tk-nl',t).innerHTML='Acceptable limit <b>'+L.ppm.toPrecision(3)+' ppm</b> ('+(L.ppm*1000).toPrecision(3)+' ng/g). Target LOQ ≤ <b>'+L.loq.toPrecision(2)+' ppm</b>.';
  send(t,'Nitrosamine risk screen: '+r.level+' ('+r.score+'/'+r.max+'). Limit '+L.ppm.toPrecision(3)+' ppm at MDD '+num(lf,'mdd')+' mg/day.')}live(f,up);live(lf,up)});

/* Endotoxin */
$$('[data-tk=endo]').forEach(function(t){var f=$('form',t);function up(){var k=val(f,'route'),radio=k[0]==='r';$$('[name=basis],[name=unit],[name=wt],[name=conc]',f).forEach(function(e){e.closest('label').style.display=radio?'none':''});
  var r=C.endo({k:k,basis:val(f,'basis'),dose:Math.max(1e-6,num(f,'dose')),unit:val(f,'unit'),wt:Math.max(.1,num(f,'wt')),conc:num(f,'conc'),lam:parseFloat(val(f,'lam'))});
  $('.tk-el',t).textContent=r.lim.toPrecision(3)+' '+r.unit;$('.tk-ef',t).textContent=radio?'Limit = '+(k==='r175'?175:14)+' / V, V = '+num(f,'dose')+' mL':'K / M = '+k+' / '+r.M.toPrecision(3)+' '+val(f,'unit')+'/kg/h';
  $('.tk-mvd',t).textContent=r.mvd>=1?'1 in '+Math.floor(r.mvd).toLocaleString('en-US'):'Below 1: increase test sensitivity';
  $('.tk-em',t).textContent=r.mvd<10?'Small MVD: interference is hard to dilute out. Use a kinetic chromogenic or rFC method at λ 0.005 EU/mL and plan careful method suitability.':r.mvd<100?'Moderate MVD: kinetic methods recommended; gel clot possible if the product does not interfere.':'Large MVD: any compendial method works; kinetic chromogenic or rFC give quantitative trending.';
  send(t,'Endotoxin limit: '+r.lim.toPrecision(3)+' '+r.unit+', MVD '+Math.floor(r.mvd)+'.')}live(f,up)});

/* Inspection readiness */
$$('[data-tk=irs]').forEach(function(t){var A=cfg(t),f=$('form',t),g=$('.tk-gate',t);var ACT={di:'Lock down shared logins and switch on audit-trail review before approval on every chromatography data system.',doc:'Run a documentation walk-through: SOP versus practice, blank fields, logbook gaps.',trn:'Add practical competency checks for each method and an annual data integrity refresher.',
  capa:'Verify effectiveness of every open and recent CAPA, starting with past inspection observations.',eq:'Close qualification and periodic-review gaps for instruments and computerised systems.',oos:'Re-train on the two-phase OOS investigation and define retest rules in the SOP.'};
 function up(){var ans=$$('.tk-yn',f).map(function(q){var e=$('input:checked',q);return {a:q.dataset.a,v:e?+e.value:0}}),r=C.irs(ans);$('.tk-is',t).textContent=r.total+'%';
  $('.tk-il',t).textContent=r.total>=85?'Mature: keep testing it with mock inspections.':r.total>=65?'Mostly ready, with gaps an inspector would find.':'Significant gaps: act before your next inspection.';
  $('.tk-bars',t).innerHTML=bars(A.map(function(x){var v=r.areas[x[0]];return [x[1],v,v+'%',v<50?'var(--amb)':'var(--teal)']}));
  var low=A.map(function(x){return x[0]}).sort(function(a,b){return (r.areas[a]-(a==='di'?10:0))-(r.areas[b]-(b==='di'?10:0))}).filter(function(k){return r.areas[k]<100}).slice(0,3);
  $('.tk-ia',t).innerHTML=(low.length?low:['di']).map(function(k){return '<li>'+esc(ACT[k])+'</li>'}).join('');var s='Total '+r.total+'%; '+A.map(function(x){return x[1]+' '+r.areas[x[0]]+'%'}).join(', ');g.elements.score.value=s}live(f,up)});

/* Lab locator */
$$('[data-tk=loc]').forEach(function(t){var c=cfg(t),f=$('form',t);function up(){var q=f.elements.city.value.trim().toLowerCase(),k=Object.keys(c.cities).filter(function(x){return x.toLowerCase()===q})[0]||Object.keys(c.cities).filter(function(x){return q&&x.toLowerCase().indexOf(q)===0})[0];
  if(!k){$('.tk-ln',t).innerHTML='<li>Choose a city from the list (for example Ahmedabad, Basel or Boston).</li>';$('.tk-lc',t).innerHTML='';return}var p=c.cities[k],cold=c.cold[+val(f,'cold')];
  var countryOf={};c.labs.forEach(function(l){countryOf[l.c]=l.co});var R=c.labs.map(function(l){return {l:l,km:C.km(p[0],p[1],l.la,l.lo)}}).sort(function(a,b){return a.km-b.km}).slice(0,3);
  function lane(r){var same=(countryOf[k]||'')===r.l.co,km=r.km;return same||km<900?'1 to 2':km<3500?'2 to 3':'3 to 5'}
  $('.tk-ln',t).innerHTML=R.map(function(r){return '<li><a href="'+ROOT+'labs/'+r.l.s+'.html"><b>'+esc(r.l.c)+', '+esc(r.l.co)+'</b></a><span>'+Math.round(r.km).toLocaleString('en-US')+' km · '+lane(r)+' business days by express courier · opens '+esc(r.l.ph)+'</span><small>'+esc(r.l.f)+'</small></li>'}).join('');
  var top=R[0].l;$('.tk-lc',t).innerHTML='<h3>Shipping to '+esc(top.c)+'</h3><p><b>Customs:</b> '+esc(c.customs[top.co]||'Our logistics team confirms requirements before you ship.')+'</p><p><b>Packing for '+esc(cold[0].toLowerCase())+':</b> '+esc(cold[1])+'</p><p><b>Courier options:</b> specialist clinical couriers (for example World Courier, Marken, Cryoport, DHL Medical Express) for temperature-controlled lanes; standard express for room-temperature samples. Examples only, not partnerships.</p><p><b>Tips:</b> ship Monday to Wednesday, put the sample submission sheet inside and outside the box, and email the airway bill.</p>';
  send(t,'Shipping plan: from '+k+' to '+top.c+' ('+Math.round(R[0].km)+' km), '+cold[0]+'.')}live(f,up)});

/* Method search and compare */
$$('[data-tk=meth]').forEach(function(t){var M=cfg(t),q=$('.tk-mq',t),mm=$('.tk-mm',t),a=$('.tk-ma',t),b=$('.tk-mb',t);b.selectedIndex=1;
 function list(){var v=q.value.toLowerCase().trim(),m=mm.value,R=M.filter(function(x){return (!v||(x.n+' '+x.t+' '+x.p+' '+x.st).toLowerCase().indexOf(v)>-1)&&(!m||(m==='All modalities'?x.mo==='All':x.mo.indexOf(m)>-1||x.mo==='All'))});
  $('.tk-ml',t).innerHTML=R.length?R.map(function(x){return '<li><a href="'+ROOT+'method-library/'+x.s+'.html"><b>'+esc(x.n)+'</b></a><span>'+esc(x.t)+' · '+esc(x.st)+'</span><button type="button" class="ch" data-i="'+M.indexOf(x)+'">Compare</button></li>'}).join(''):'<li>No method matches. <a href="'+ROOT+'request-quote.html">Ask us anyway</a>.</li>';
  $$('.tk-ml .ch',t).forEach(function(x){x.addEventListener('click',function(){b.value=a.value;a.value=x.dataset.i;cmp();$('.tk-mt',t).scrollIntoView({block:'nearest',behavior:rm?'auto':'smooth'})})})}
 function cmp(){var A=M[+a.value],B=M[+b.value],F=[['Method','n'],['Technique','t'],['Purpose','p'],['Standards','st'],['Typical sample','sa'],['Typical turnaround','tat'],['Modality','mo']];
  $('.tk-mt tbody',t).innerHTML='<tr><th></th><th>A</th><th>B</th></tr>'+F.map(function(r){return '<tr><th scope="row">'+r[0]+'</th><td>'+esc(A[r[1]])+'</td><td>'+esc(B[r[1]])+'</td></tr>'}).join('')+'<tr><th scope="row">Library entry</th><td><a href="'+ROOT+'method-library/'+A.s+'.html">Open</a></td><td><a href="'+ROOT+'method-library/'+B.s+'.html">Open</a></td></tr>'}
 [q,mm].forEach(function(e){e.addEventListener('input',list)});[a,b].forEach(function(e){e.addEventListener('change',cmp)});list();cmp()});

/* Regulatory impact */
$$('[data-tk=reg]').forEach(function(t){var R=cfg(t),f=$('form',t);function up(){var p=val(f,'p'),m=val(f,'m'),pt={small:['small'],sterile:['small','sterile'],bio:['bio','sterile'],mrna:['mrna','bio','sterile'],cgt:['cgt','sterile']}[p];
  var L=R.filter(function(r){return (r.m==='all'&&m!=='who'||r.m===m||(m==='who'&&r.m==='all'&&r.t.indexOf('ICH')===0))&&(r.p==='all'||pt.indexOf(r.p)>-1)});
  $('.tk-rc',t).textContent=L.length+' rules and guidelines apply';$('.tk-rl',t).innerHTML=L.map(function(r){return '<li class="reveal in"><b>'+esc(r.t)+'</b><span>'+esc(r.w)+'</span><a href="'+ROOT+r.u.slice(1)+'">'+esc(r.s)+' &rsaquo;</a></li>'}).join('');
  send(t,'Regulatory check for '+$('select[name=p]',f).selectedOptions[0].text+' in '+$('select[name=m]',f).selectedOptions[0].text+'.')}live(f,up)});

/* Cost of delay */
$$('[data-tk=cod]').forEach(function(t){var f=$('form',t);function up(){var r=C.cod({val:num(f,'val'),n:num(f,'n'),typ:num(f,'typ'),ours:num(f,'ours'),inv:num(f,'inv'),rate:num(f,'rate')}),mx=Math.max(r.typCost,1);
  $('.tk-cd',t).textContent=usd(r.daily);$('.tk-cs',t).textContent=usd(r.saving);
  $('.tk-cbars',t).innerHTML=bars([['Waiting cost a year at '+num(f,'typ')+' days',r.typCost/mx*100,usd(r.typCost),'#8b97a8'],['Waiting cost a year at '+num(f,'ours')+' days',r.ourCost/mx*100,usd(r.ourCost)],['Saving',r.saving/mx*100,usd(r.saving),'var(--amb)']]);
  $('.tk-cx',t).textContent='Each batch saves '+usd(r.perBatch)+' by clearing '+Math.max(0,num(f,'typ')-num(f,'ours'))+' days sooner.';send(t,'Cost of delay: '+usd(r.daily)+' per batch per day; annual saving '+usd(r.saving)+' for '+num(f,'n')+' batches.')}live(f,up)});

/* Ask the Lab (full page) */
$$('[data-tk=ask]').forEach(function(t){var L=$('.tk-al',t),IDX=null;function load(cb){if(IDX)return cb();fetch(ROOT+'assets/search.json').then(function(r){return r.json()}).then(function(j){IDX=j;cb()}).catch(function(){IDX=[];cb()})}
 function say(h,c){var p=d.createElement('p');p.className='am '+c;p.innerHTML=h;L.appendChild(p);L.scrollTop=L.scrollHeight}
 function sc(q,e){var s=0;q.toLowerCase().split(/\W+/).forEach(function(y){if(y.length<3)return;if(e.t.toLowerCase().indexOf(y)>-1)s+=6;if(e.d.toLowerCase().indexOf(y)>-1)s+=3;if(e.k.indexOf(y)>-1)s+=1});return s}
 function ask(q){say(esc(q),'me');if(/emergenc|patient|diagnos|dose me|should i take/i.test(q)){say('I can only answer questions about our testing services. Please speak to a clinician for medical questions.','bot');return}
  load(function(){var R=IDX.map(function(e){return [sc(q,e),e]}).filter(function(x){return x[0]>3}).sort(function(a,b){return b[0]-a[0]}).slice(0,3).map(function(x){return x[1]});
   var h='<a href="'+ROOT+'request-quote.html?q='+encodeURIComponent(q)+'">Send this to a scientist with a pre-filled quote request &rsaquo;</a>';
   if(!R.length){say('I could not find that on our pages, so I will not guess. '+h,'bot');return}
   say('Here is what our pages say. <b>'+esc(R[0].t)+'</b>: '+esc(R[0].d)+'<span class="src">Sources: '+R.map(function(e){return '<a href="'+ROOT+e.p+'">'+esc(e.t)+'</a>'}).join(' · ')+'</span><span class="src">'+h+'</span>','bot')})}
 $$('.tk-aq button',t).forEach(function(b){b.addEventListener('click',function(){ask(b.textContent)})});
 $('.tk-af',t).addEventListener('submit',function(e){e.preventDefault();var i=$('input',e.target);if(i.value.trim())ask(i.value.trim());i.value=''})});

/* Hub: category filter + preview dialog */
$$('.tk-cf').forEach(function(f){var cards=$$('.tk-card');$$('[data-c]',f).forEach(function(b){b.addEventListener('click',function(){$$('[data-c]',f).forEach(function(x){x.setAttribute('aria-pressed',x===b)});cards.forEach(function(c){c.hidden=!!b.dataset.c&&c.dataset.cat!==b.dataset.c})})})});
var dlg=$('.tk-dlg');if(dlg){$$('.tk-pv').forEach(function(b){b.addEventListener('click',function(){var bd=$('.cs-b',dlg);bd.innerHTML='';bd.appendChild($('template',b.closest('.tk-card')).content.cloneNode(true));
  $$('[src],[href]',bd).forEach(function(e){['src','href'].forEach(function(a){var v=e.getAttribute(a);if(v&&v[0]==='/')e.setAttribute(a,ROOT+v.slice(1))})});dlg.showModal()})});
 $('.cs-cl',dlg).addEventListener('click',function(){dlg.close()});dlg.addEventListener('click',function(e){if(e.target===dlg)dlg.close()})}
})();
