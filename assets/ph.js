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
