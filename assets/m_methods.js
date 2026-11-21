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
