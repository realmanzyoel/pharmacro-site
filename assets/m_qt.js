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
