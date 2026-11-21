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
