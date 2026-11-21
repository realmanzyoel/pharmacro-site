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
