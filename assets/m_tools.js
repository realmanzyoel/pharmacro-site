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
