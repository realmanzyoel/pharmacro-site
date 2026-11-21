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
