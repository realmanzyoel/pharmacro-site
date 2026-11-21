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
