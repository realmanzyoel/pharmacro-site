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
