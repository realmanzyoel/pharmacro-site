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
